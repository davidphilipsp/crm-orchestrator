"""
transform.py — Normalização e detecção de padrões (Camada 2: local)
Saída: parquet normalizados para analyze.py
"""
import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)
INTERIM = Path("data/interim")


def transform_sms() -> pd.DataFrame:
    path = INTERIM / "sms_disparador.parquet"
    if not path.exists():
        raise FileNotFoundError("Execute: python src/extract.py --source <csv> --type sms")

    df = pd.read_parquet(path)
    df = df.dropna(subset=["data"])
    df["taxa_entrega"] = df["entregues"] / df["enviados"].replace(0, pd.NA)
    df["dia_semana"] = df["data"].dt.day_name()
    df["dia_mes"] = df["data"].dt.day

    # Detecta fadiga: copy repetida por N dias consecutivos
    df_sorted = df.sort_values(["copy", "data"]).copy()
    df_sorted["gap_dias"] = df_sorted.groupby("copy")["data"].diff().dt.days
    # Run length of consecutive days per copy: a gap > 1 day (or the first day) starts a new run.
    novo_bloco = df_sorted["gap_dias"].ne(1)
    bloco = novo_bloco.groupby(df_sorted["copy"]).cumsum()
    df_sorted["dias_consecutivos"] = df_sorted.groupby([df_sorted["copy"], bloco]).cumcount() + 1
    df_sorted["alerta_fadiga"] = df_sorted["dias_consecutivos"] >= 3

    out = INTERIM / "sms_transformado.parquet"
    df_sorted.to_parquet(out, index=False)
    log.info(f"Transformado: {out} ({len(df_sorted)} linhas, "
             f"{df_sorted['alerta_fadiga'].sum()} alertas de fadiga)")
    return df_sorted


if __name__ == "__main__":
    df = transform_sms()
    cols = ["data", "copy", "enviados", "taxa_entrega", "dias_consecutivos", "alerta_fadiga"]
    print(df[cols].to_string(max_rows=20))
