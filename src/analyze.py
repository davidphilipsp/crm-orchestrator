"""
analyze.py — Correlações e agregações (Camada 2: local)
Saída: outputs/reports/stats_summary.json
NUNCA expõe dados individuais — apenas agregados para a API.
"""
import json, logging
from pathlib import Path
from datetime import datetime
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

INTERIM  = Path("data/interim")
OUTPUTS  = Path("outputs/reports")
OUTPUTS.mkdir(parents=True, exist_ok=True)


def build_summary() -> dict:
    path = INTERIM / "sms_transformado.parquet"
    if not path.exists():
        raise FileNotFoundError("Execute transform.py primeiro.")

    df = pd.read_parquet(path)

    # Agrega por dia — nunca por usuário
    por_dia = (
        df.groupby(df["data"].dt.date)
        .agg(
            enviados=("enviados", "sum"),
            entregues=("entregues", "sum"),
            taxa_entrega=("taxa_entrega", "mean"),
            n_copys=("copy", "nunique"),
        )
        .reset_index()
        .rename(columns={"data": "date"})
    )

    # Alertas de fadiga por copy
    fadiga = (
        df[df["alerta_fadiga"]]
        .groupby("copy")
        .agg(
            max_dias_consecutivos=("dias_consecutivos", "max"),
            ultima_data=("data", "max"),
        )
        .reset_index()
    )

    summary = {
        "gerado_em": datetime.now().isoformat(),
        "periodo": {
            "inicio": str(df["data"].min().date()),
            "fim":    str(df["data"].max().date()),
            "dias_com_disparo": int(df["data"].dt.date.nunique()),
        },
        "totais": {
            "enviados":              int(df["enviados"].sum()),
            "entregues":             int(df["entregues"].sum()),
            "nao_entregues":         int(df["nao_entregues"].sum()),
            "taxa_entrega_geral":    round(float(df["entregues"].sum() / df["enviados"].sum()), 4),
            "custo_total_brl":       round(float(df["custo_total"].sum()), 2) if "custo_total" in df else None,
            "copys_unicas":          int(df["copy"].nunique()),
        },
        "por_dia": por_dia.to_dict("records"),
        "alertas_fadiga": fadiga.to_dict("records"),
        "top3_melhor_taxa": (
            df.nlargest(3, "taxa_entrega")[["data", "copy", "taxa_entrega", "enviados"]]
            .assign(data=lambda x: x["data"].astype(str))
            .to_dict("records")
        ),
        "top3_pior_taxa": (
            df.nsmallest(3, "taxa_entrega")[["data", "copy", "taxa_entrega", "enviados"]]
            .assign(data=lambda x: x["data"].astype(str))
            .to_dict("records")
        ),
        "dias_sem_disparo": [],  # preencher com cruzamento do calendário
    }

    out = OUTPUTS / "stats_summary.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2, default=str)
    log.info(f"Resumo salvo: {out}")
    return summary


if __name__ == "__main__":
    s = build_summary()
    print("\n📊 TOTAIS")
    print(json.dumps(s["totais"], indent=2, ensure_ascii=False))

    if s["alertas_fadiga"]:
        print("\n⚠️  ALERTAS DE FADIGA")
        for a in s["alertas_fadiga"]:
            print(f"  [{a['max_dias_consecutivos']}d] {str(a['copy'])[:70]}")
    else:
        print("\n✅ Sem alertas de fadiga")
