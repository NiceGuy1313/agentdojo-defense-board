# 기여 가이드

모든 데이터는 [`data/results.csv`](data/results.csv) 하나에 있습니다. 페이지(`index.html`)와 README 표는 이 파일에서 자동으로 만들어집니다.

## 방법 1: 이슈로 제보

[새 결과 제보](../../issues/new?template=new-result.yml) 양식을 채우면 관리자가 확인 후 CSV에 반영합니다. GitHub 사용이 익숙하지 않다면 이쪽이 편합니다.

## 방법 2: PR로 직접 수정

1. GitHub에서 `data/results.csv`를 열고 연필 아이콘(Edit)을 누릅니다. 포크와 브랜치는 자동으로 만들어집니다.
2. 한 결과당 한 줄을 추가하거나 고칩니다.
3. PR을 보내면 `Validate data` 검사가 자동으로 돕니다. 실패하면 로그에 몇 번째 줄이 왜 틀렸는지 나옵니다.
4. merge되면 몇 분 안에 페이지와 README 표가 갱신됩니다.

## 열 설명

| 열 | 필수 | 설명 | 예 |
| --- | :---: | --- | --- |
| `paper` | O | 이 수치를 보고한 논문 | `MELON` |
| `defense` | O | 방어 기법 이름 | `MELON-Aug` |
| `venue` | O | 방어 기법의 학회/연도 | `ICML 2025` |
| `method` | O | 방어 방식 | `Masked Re-execution` |
| `model` | O | 에이전트 모델 | `GPT-4o` |
| `utility` |  | 공격 없을 때 Utility (%) | `76.29` |
| `utility_under_attack` |  | 공격 중 Utility (%) | `68.72` |
| `asr` |  | 공격 성공률 (%) | `0.32` |
| `kind` | O | `proposed` (그 논문의 제안 기법), `baseline` (그 논문이 비교용으로 보고), `none` (방어 없음) | `proposed` |
| `link` |  | 논문 링크 (arXiv 등) | `https://arxiv.org/abs/...` |
| `note` |  | 비고 (설정 차이, 출처 표/그림 번호 등) | `Table 2, important_instructions 공격` |

- 숫자에는 `%`를 붙이지 않습니다. 보고되지 않은 값은 비워 둡니다.
- 세 숫자 중 하나 이상은 있어야 합니다.
- 값에 쉼표가 들어가면 큰따옴표로 감쌉니다. 예: `"Table 3, GPT-4o"`
- 같은 논문의 행은 붙여서 적어 주세요. 표에서 논문별로 묶여 보입니다.
- 출처 확인을 위해 `note`에 표나 그림 번호를 적어 주시면 리뷰가 빨라집니다.

## 로컬에서 확인

```bash
python scripts/validate.py        # 형식 검사
python scripts/build_readme.py    # README 표 갱신
python -m http.server             # http://localhost:8000 에서 페이지 확인
```
