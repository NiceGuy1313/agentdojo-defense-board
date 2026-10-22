"""data/results.csv 형식 검사. 문제가 있으면 줄 번호와 함께 출력하고 exit 1."""
import csv
import sys
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "data" / "results.csv"
COLUMNS = ["paper", "defense", "venue", "method", "model",
           "utility", "utility_under_attack", "asr", "kind", "link", "note"]
REQUIRED = ["paper", "defense", "venue", "method", "model", "kind"]
NUMERIC = ["utility", "utility_under_attack", "asr"]
KINDS = {"proposed", "baseline", "none"}


def main() -> int:
    errors = []
    with PATH.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        if header != COLUMNS:
            print(f"헤더가 다릅니다.\n  기대: {','.join(COLUMNS)}\n  실제: {','.join(header)}")
            return 1
        seen = {}
        for lineno, row in enumerate(reader, start=2):
            if not any(c.strip() for c in row):
                continue
            if len(row) != len(COLUMNS):
                errors.append(f"{lineno}행: 열 개수 {len(row)}개 (기대 {len(COLUMNS)}개). 쉼표가 들어간 값은 큰따옴표로 감싸 주세요.")
                continue
            r = dict(zip(COLUMNS, (c.strip() for c in row)))
            for k in REQUIRED:
                if not r[k]:
                    errors.append(f"{lineno}행: '{k}' 값이 비어 있습니다.")
            if r["kind"] and r["kind"] not in KINDS:
                errors.append(f"{lineno}행: kind는 {sorted(KINDS)} 중 하나여야 합니다 (현재 '{r['kind']}').")
            for k in NUMERIC:
                v = r[k]
                if v in ("", "N/A"):
                    continue
                if v.endswith("%"):
                    errors.append(f"{lineno}행: '{k}'에는 % 없이 숫자만 적어 주세요 (현재 '{v}').")
                    continue
                try:
                    x = float(v)
                except ValueError:
                    errors.append(f"{lineno}행: '{k}' 값 '{v}'이 숫자가 아닙니다.")
                    continue
                if not 0 <= x <= 100:
                    errors.append(f"{lineno}행: '{k}' 값 {x}이 0~100 범위를 벗어났습니다.")
            if all(r[k] in ("", "N/A") for k in NUMERIC):
                errors.append(f"{lineno}행: utility, utility_under_attack, asr 중 하나 이상은 값이 있어야 합니다.")
            if r["link"] and not r["link"].startswith(("http://", "https://")):
                errors.append(f"{lineno}행: link는 http(s):// 로 시작해야 합니다.")
            key = (r["paper"], r["defense"], r["model"], r["method"])
            if key in seen:
                errors.append(f"{lineno}행: {seen[key]}행과 (paper, defense, model, method)가 같습니다. 중복인지 확인해 주세요.")
            else:
                seen[key] = lineno

    if errors:
        print(f"data/results.csv 검사 실패 ({len(errors)}건)")
        for e in errors:
            print("  - " + e)
        return 1
    print(f"data/results.csv OK ({len(seen)}개 행)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
