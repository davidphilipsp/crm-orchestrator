"""
score_copy.py — @copy-analyst via Anthropic API (Camada 3)
Carrega apenas docs/08_disparos.md + docs/10_compliance.md — não o projeto inteiro.
"""
import os, json, argparse, logging
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def _load_context() -> str:
    """Carrega apenas os capítulos necessários para o agente."""
    ctx = ""
    for doc in ["docs/08_disparos.md", "docs/10_compliance.md", "squad/copy_analyst.md"]:
        p = Path(doc)
        if p.exists():
            ctx += f"\n\n--- {doc} ---\n{p.read_text()}"
    return ctx


def score_copy(
    copy_text: str,
    canal: str = "SMS",
    segmento: str = "Low",
    dias_em_uso: int = 0,
    objetivo: str = "missao",
) -> dict:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    context = _load_context()

    system = f"""Você é o @copy-analyst do crm-orchestrator.
Avalie copys de comunicação para a marca (brand-a) seguindo as regras abaixo.
Retorne SOMENTE JSON válido — sem markdown, sem texto adicional.

REGRAS E CONTEXTO:
{context}"""

    user = json.dumps({
        "copy": copy_text,
        "canal": canal,
        "segmento": segmento,
        "dias_em_uso": dias_em_uso,
        "objetivo": objetivo,
    }, ensure_ascii=False)

    user += """

Retorne este JSON preenchido:
{
  "score_total": <float 0-5>,
  "dimensoes": {
    "promessa":   {"score": 0, "justificativa": ""},
    "urgencia":   {"score": 0, "justificativa": ""},
    "tom":        {"score": 0, "justificativa": ""},
    "compliance": {"score": 0, "justificativa": ""},
    "fadiga":     {"score": 0, "justificativa": ""}
  },
  "aprovado": true,
  "alertas": [],
  "sugestao_alternativa": ""
}"""

    log.info("Consultando @copy-analyst...")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system,
        messages=[{"role": "user", "content": user}],
    )

    raw = response.content[0].text.strip()
    # Limpa markdown se vier por engano
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score de copy — @copy-analyst")
    parser.add_argument("--text",     required=True, help="Texto da copy")
    parser.add_argument("--canal",    default="SMS", choices=["SMS","inbox","push","email","whatsapp"])
    parser.add_argument("--segmento", default="Low")
    parser.add_argument("--dias",     type=int, default=0, help="Dias em uso consecutivo")
    parser.add_argument("--objetivo", default="missao")
    args = parser.parse_args()

    result = score_copy(args.text, args.canal, args.segmento, args.dias, args.objetivo)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    status = "✅ APROVADO" if result.get("aprovado") else "❌ REPROVADO"
    print(f"\n{status} — Score total: {result.get('score_total', 0):.1f}/5")

    if result.get("alertas"):
        print("⚠️  Alertas:", ", ".join(result["alertas"]))
