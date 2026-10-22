"""data/results.csv로 README.md의 표 부분(마커 사이)을 다시 만든다."""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "results.csv"
README = ROOT / "README.md"
BEGIN, END = "<!-- TABLE:BEGIN -->", "<!-- TABLE:END -->"


def pct(v: str) -> str:
    v = v.strip()
    return "–" if v in ("", "N/A") else f"{v}%"


def cell(v: str) -> str:
    return v.replace("|", "\\|").strip()


def main() -> int:
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    out = [
        f"총 {len(rows)}개 결과 · {len({r['paper'] for r in rows})}개 논문\n",
        "| 보고 논문 | 방어 기법 | 학회/연도 | 방식 | 모델 | Utility<br>(no attack) | Utility<br>(under attack) | ASR |",
        "| --- | --- | --- | --- | --- | ---: | ---: | ---: |",
    ]
    prev = None
    for r in rows:
        paper = ""
        if r["paper"] != prev:
            paper = f"[{cell(r['paper'])}]({r['link'].strip()})" if r["link"].strip() else cell(r["paper"])
        prev = r["paper"]
        name = cell(r["defense"])
        if r["kind"] == "proposed":
            name = f"**{name}**"
        elif r["kind"] == "none":
            name = f"_{name}_"
        if r["note"].strip():
            name += f" <sup title=\"{cell(r['note'])}\">*</sup>"
        out.append(f"| {paper} | {name} | {cell(r['venue'])} | {cell(r['method'])} | {cell(r['model'])} | "
                   f"{pct(r['utility'])} | {pct(r['utility_under_attack'])} | {pct(r['asr'])} |")

    text = README.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print("README.md에 표 마커가 없습니다.")
        return 1
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{BEGIN}\n{chr(10).join(out)}\n{END}{tail}", encoding="utf-8")
    print("README.md 표 갱신")
    return 0


if __name__ == "__main__":
    sys.exit(main())
