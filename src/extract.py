"""
extract.py — Camada de ingestão (Camada 2: local)
Regra: NUNCA passa dados individuais para a API. Apenas agrega.
"""
import os, argparse, logging
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)


def load_sms_csv(path: str) -> pd.DataFrame:
    """CSV exportado do disparador (plataforma de CRM): sep=; encoding=utf-8-sig"""
    log.info(f"Lendo CSV disparador: {path}")
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig", decimal=",", thousands=".")
    df.columns = [
        c.strip().lower()
        .replace(" ", "_").replace("ã", "a").replace("é", "e")
        .replace("ê", "e").replace("ç", "c")
        for c in df.columns
    ]
    df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")
    for col in ["enviados", "entregues", "nao_entregues", "creditos_utilizados"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
    if "custo_total" in df.columns:
        df["custo_total"] = pd.to_numeric(
            df["custo_total"].astype(str)
            .str.replace("R$", "").str.replace(".", "").str.replace(",", ".").str.strip(),
            errors="coerce"
        )
    out = INTERIM / "sms_disparador.parquet"
    df.to_parquet(out, index=False)
    log.info(f"Salvo: {out} ({len(df)} linhas)")
    return df


def load_ggr_csv(path: str) -> pd.DataFrame:
    """CSV de GGR/Turnover exportado do backoffice."""
    log.info(f"Lendo CSV de GGR/Turnover: {path}")
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig", decimal=",")
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")
    out = INTERIM / "ggr.parquet"
    df.to_parquet(out, index=False)
    log.info(f"Salvo: {out} ({len(df)} linhas)")
    return df


def load_bigquery(query: str) -> pd.DataFrame:
    """
    Query BigQuery — projeto/dataset definidos por env (CRM_BQ_PROJECT_ID / CRM_BQ_DATASET).
    SEMPRE filtre pela partição. NUNCA SELECT *.
    """
    from google.cloud import bigquery
    from google.oauth2 import service_account

    key_path = os.getenv("CRM_BQ_KEY_PATH")
    project = os.getenv("CRM_BQ_PROJECT_ID")
    if not key_path or not project:
        raise EnvironmentError("CRM_BQ_KEY_PATH / CRM_BQ_PROJECT_ID não definidos no .env")

    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = bigquery.Client(credentials=credentials, project=project)
    log.info("Executando query BigQuery...")
    df = client.query(query).to_dataframe()
    log.info(f"BigQuery: {len(df)} linhas retornadas")
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="crm-orchestrator extractor")
    parser.add_argument("--source", required=True)
    parser.add_argument("--type", choices=["sms", "ggr"], default="sms")
    args = parser.parse_args()

    if args.type == "sms":
        df = load_sms_csv(args.source)
    else:
        df = load_ggr_csv(args.source)
    print(df.head())
    print(f"\nShape: {df.shape}")
