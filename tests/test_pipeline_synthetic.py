"""Offline tests on a synthetic SMS dispatch file: extract -> transform -> analyze (no API, no real data)."""
import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

CSV = """Data;Copy;Enviados;Entregues;Nao Entregues;Custo Total
01/01/2026;Copy A;1.000;900;100;R$ 10,00
02/01/2026;Copy A;1.000;880;120;R$ 10,00
03/01/2026;Copy A;1.000;850;150;R$ 10,00
04/01/2026;Copy A;1.000;820;180;R$ 10,00
02/01/2026;Copy B;500;450;50;R$ 5,00
05/01/2026;Copy B;500;440;60;R$ 5,00
"""


def run_pipeline(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    src = tmp_path / "disparador.csv"
    src.write_text(CSV, encoding="utf-8")
    for m in ("src.extract", "src.transform", "src.analyze"):
        sys.modules.pop(m, None)
    extract = importlib.import_module("src.extract")
    transform = importlib.import_module("src.transform")
    analyze = importlib.import_module("src.analyze")
    extract.load_sms_csv(str(src))
    df = transform.transform_sms()
    return df, analyze.build_summary()


def test_fatigue_flagged_after_three_consecutive_days(tmp_path, monkeypatch):
    df, _ = run_pipeline(tmp_path, monkeypatch)
    a = df[df["copy"] == "Copy A"].sort_values("data")
    assert list(a["dias_consecutivos"]) == [1, 2, 3, 4]
    assert list(a["alerta_fadiga"]) == [False, False, True, True]
    assert not df[df["copy"] == "Copy B"]["alerta_fadiga"].any()  # not consecutive


def test_summary_is_aggregate_only(tmp_path, monkeypatch):
    _, s = run_pipeline(tmp_path, monkeypatch)
    assert s["totais"]["enviados"] == 5000
    assert s["totais"]["entregues"] == 4340
    assert s["totais"]["custo_total_brl"] == 50.0
    assert s["periodo"]["dias_com_disparo"] == 5
    out = json.loads((tmp_path / "outputs/reports/stats_summary.json").read_text())
    assert "user_id" not in json.dumps(out)
