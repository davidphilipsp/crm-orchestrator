# crm-orchestrator

A small CRM orchestrator for iGaming lifecycle campaigns: it ingests SMS/push dispatch exports, detects copy
fatigue and delivery-rate patterns **locally**, sends only **aggregates** to an LLM copy reviewer, and keeps an
append-only memory of confirmed patterns and open hypotheses. A 9-agent "squad" config splits the method into
focused roles, each loading at most 4 context documents.

> Built while contracted by an iGaming operator; brand names, data and figures removed.
> Built with Claude Code as a pair programmer.

Method docs (`docs/`, 15 chapters) and agent personas (`squad/`) are in Portuguese; code comments are mixed PT/EN.

## Architecture

```text
data/raw/*.csv ──► src/extract.py ──► data/interim/*.parquet ──► src/transform.py ──► src/analyze.py ──► outputs/reports/stats_summary.json
 (dispatch export)   normalise PT-BR numbers,     (local only)       consecutive-day        daily aggregates,
                     dates, R$ currency                              fatigue detection      fatigue alerts, top/bottom 3
                                                                                    │
                                    src/score_copy.py ◄── docs/08 + docs/10 + persona  (Anthropic API: one copy, no user data)
                                                                                    │
                          memory/memory.json (confirmed patterns) · memory/hypothesis_log.md (open hypotheses)
```

Three layers: **ingestion** (`extract.py`, CSV or BigQuery), **local analysis** (`transform.py`, `analyze.py`:
pandas, never per-user output), **LLM layer** (`score_copy.py`: scores a copy on promise, urgency, tone,
compliance and fatigue, returns strict JSON).

Squad (`squad/config.yaml`, 9 agents): `copy_analyst`, `journey_builder`, `data_engineer`, `analyst`,
`segment_planner`, `calendar_optimizer`, `gamification_manager`, `tournament_manager`, `compliance_tc`.
Persona files for 7 of them are in `squad/`; `copy_analyst.md` and `journey_builder.md` were never written in the
original project (`score_copy.py` skips a missing persona file).

## Stack

Python 3.10+, pandas, pyarrow, DuckDB (listed), Google BigQuery / gspread (optional sources), python-dotenv, rich,
pytest. AI: **Anthropic Python SDK, model `claude-sonnet-4-20250514`**, `max_tokens=1000` (`src/score_copy.py`,
`squad/config.yaml`).

## Contracts / invariants

- `api_receives_aggregates_only`: individual rows never leave the machine; the API sees one copy text plus channel,
  segment, days in use and goal.
- Copy fatigue: the same copy on **3+ consecutive days** for a segment raises `alerta_fadiga`.
- `memory_append_only`: patterns and hypotheses are never deleted, only marked `deprecated` / updated with a result.
- `web_search_requires_hypothesis`, `max_context_docs_per_agent: 4`.
- The LLM reply must be valid JSON in a fixed schema (`score_total`, five dimensions, `aprovado`, `alertas`,
  `sugestao_alternativa`).
- Offer thresholds (VIP minimum spin value, delivery-rate threshold) are configuration, not code.

## Tests

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

`tests/test_pipeline_synthetic.py` runs extract → transform → analyze on a synthetic 6-row file and checks the
fatigue counter and the aggregate-only summary. While preparing this release that test found an off-by-one in
the consecutive-day counter (it also did not reset after a gap); `src/transform.py` carries the fix.

## How to run

```bash
cp .env.example .env            # fill in placeholders: ANTHROPIC_API_KEY, optional BigQuery / Sheets ids
pip install -r requirements.txt

python src/extract.py --source data/raw/<dispatch-export>.csv --type sms
python src/transform.py
python src/analyze.py           # writes outputs/reports/stats_summary.json

python src/score_copy.py --text "<your copy>" --canal SMS --segmento Low --dias 1
```

Expected dispatch CSV columns (`;`-separated, PT-BR numbers): `Data`, `Copy`, `Enviados`, `Entregues`,
`Nao Entregues`, optional `Custo Total`.

## Security

- Secrets only via environment (`.env`, git-ignored); `.env.example` holds placeholders only.
- No real data is included: `data/`, `outputs/`, spreadsheets and CSVs are git-ignored; `memory/` ships as empty
  templates (the original entries were operator results and were removed).
- Brand names, warehouse/project identifiers, sheet ids, campaign figures and the original analyses were removed.
