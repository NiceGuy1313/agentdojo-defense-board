# AgentDojo Defense Board

AgentDojo 벤치마크에서 각 논문이 보고한 prompt injection 방어 기법의 Utility와 공격 성공률(ASR)을 함께 모으는 저장소입니다.

**인터랙티브 페이지: https://OWNER.github.io/REPO/** (필터, 정렬, Utility-ASR 산점도)

> [!NOTE]
> - 수치는 각 논문의 보고값입니다. 논문마다 모델, AgentDojo 버전, 공격 설정이 달라 논문 간 비교는 참고용입니다.
> - **굵은 글씨**는 해당 논문이 제안한 기법, _기울임_은 방어 없음, 나머지는 그 논문이 baseline으로 보고한 결과입니다.

## 기여하기

누락된 논문, 잘못된 수치, 새 결과 모두 환영합니다.

- **간단히 제보:** [Issues → 새 결과 제보](../../issues/new?template=new-result.yml) 양식을 채워 주세요.
- **직접 수정:** [`data/results.csv`](data/results.csv)를 고쳐 PR을 보내 주세요. 형식 검사가 자동으로 돌고, merge되면 페이지와 아래 표가 자동으로 갱신됩니다.

자세한 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해 주세요.

## 지표

- **Utility (no attack)**: 공격이 없을 때 task 성공률
- **Utility (under attack)**: 공격 중 task 성공률
- **ASR**: 공격 성공률 (낮을수록 좋음)

## 전체 결과

아래 표는 `data/results.csv`에서 자동 생성됩니다. 직접 고치지 말고 CSV를 수정해 주세요.

<!-- TABLE:BEGIN -->
총 54개 결과 · 14개 논문

| 보고 논문 | 방어 기법 | 학회/연도 | 방식 | 모델 | Utility<br>(no attack) | Utility<br>(under attack) | ASR |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| AgentDojo | _AgentDojo_ | NeurIPS 2024 | No Defense | GPT-4o | 69.00% | 50.08% | 47.69% |
|  | Spotlighting | arXiv 2024 | Data Delimiting | GPT-4o | 72.66% | 55.64% | 41.65% |
|  | ProtectAI DeBERTa | 2024 | PI Detector | GPT-4o | 41.49% | 21.14% | 7.95% |
|  | Sandwich Defense | 2024 | Prompt Sandwiching | GPT-4o | 85.53% | 67.25% | 27.82% |
|  | SecGPT | arXiv 2024 | Tool Filter | GPT-4o | 73.13% | 56.28% | 6.84% |
| Progent | _AgentDojo_ | NeurIPS 2024 | No Defense | GPT-4o | 79.40% | 54.00% | 39.90% |
|  | Sandwich Defense | 2024 | Repeat User Prompt | GPT-4o | 83.50% | 68.40% | 25.10% |
|  | Spotlighting | arXiv 2024 | Data Delimiting | GPT-4o | 73.20% | 61.50% | 23.30% |
|  | Dual LLM Pattern | 2023 | Tool Filter | GPT-4o | 66.00% | 61.30% | 6.30% |
|  | DeBERTa-v3 | 2024 | PI Detector | GPT-4o | 37.10% | 18.50% | 8.20% |
|  | DataSentinel | IEEE S&P 2025 | Game-Theoretic Detection | GPT-4o | 65.00% | 39.40% | 21.40% |
|  | Llama Prompt Guard 2 | 2025 | PI Detector | GPT-4o | 79.40% | 39.20% | 24.10% |
|  | **Progent** | arXiv 2026 | Privilege Control | GPT-4o | 76.30% | 61.30% | 1.00% |
| MELON | **MELON** | ICML 2025 | Masked Re-execution | GPT-4o | 68.04% | 58.78% | 0.24% |
|  | **MELON-Aug** | ICML 2025 | MELON + Prompt Augmentation | GPT-4o | 76.29% | 68.72% | 0.32% |
|  | **MELON** | ICML 2025 | Masked Re-execution | o3-mini | 50.52% | 36.29% | 0.95% |
|  | **MELON-Aug** | ICML 2025 | MELON + Prompt Augmentation | o3-mini | 55.67% | 37.28% | 0.56% |
|  | **MELON** | ICML 2025 | Masked Re-execution | Llama-3.3-70B | 63.92% | 46.30% | 1.27% |
|  | **MELON-Aug** | ICML 2025 | MELON + Prompt Augmentation | Llama-3.3-70B | 67.01% | 52.94% | 0.72% |
| IPIGuard | **IPIGuard** | EMNLP 2025 | Tool Dependency Graph | GPT-4o-mini | 67.01% | 58.77% | 0.69% |
| LlamaFirewall | **PromptGuard 2 86M** | arXiv 2025 | PI Detector | AgentDojo traces | 47.01% | – | 7.53% |
|  | **AlignmentCheck** | arXiv 2025 | Trajectory Alignment | AgentDojo traces | 43.09% | – | 2.89% |
|  | **Combined** | arXiv 2025 | PromptGuard + AlignmentCheck | AgentDojo traces | 42.68% | – | 1.75% |
| FIDES | **FIDES** | arXiv 2025 | Information Flow Control | GPT-4o | 50.31% | – | 0.11% |
|  | **FIDES** | arXiv 2025 | Information Flow Control | o1 | 61.44% | – | 0.63% |
|  | **FIDES** | arXiv 2025 | Information Flow Control | o3 | 56.91% | – | 0.42% |
|  | **FIDES** | arXiv 2025 | Information Flow Control | o4-mini | 55.67% | – | 0.11% |
|  | **FIDES** | arXiv 2025 | Information Flow Control | Grok-3 | 59.54% | – | 0.32% |
| CaMeL | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | Claude 4 Sonnet | 74.20% | 75.70% | 1.16% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | Claude 4 Sonnet (reasoning) | 70.10% | 72.80% | 1.16% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | Gemini 2.5 Flash | 35.10% | 41.50% | 0.11% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | Gemini 2.5 Pro | 41.20% | 45.30% | 0.00% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | o3 High | 77.30% | 79.80% | 0.00% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | o4-mini High | 76.30% | 76.10% | 0.11% |
|  | **CaMeL** | arXiv 2025 | Dual LLM + Capability Policies | Claude 3.5 Sonnet | 63.92% | 66.70% | 0.00% |
| ControlValve | **ControlValve** | ICLR 2026 | Control-flow Enforcement | o4-mini + GPT-4o | 62% | – | 0% |
| Task Shield | **Task Shield** | ACL 2025 | Task Alignment | GPT-4o | 73.20% | 69.79% | 2.07% |
|  | **Task Shield** | ACL 2025 | Task Alignment | GPT-4o-mini | 68.04% | 54.53% | 2.23% |
| PFI | **PFI** | arXiv 2025 | Trusted/Untrusted Isolation | GPT-4o | – | 61.86% | 0.00% |
|  | **PFI** | arXiv 2025 | Trusted/Untrusted Isolation | GPT-4o-mini | – | 48.45% | 0.00% |
|  | **PFI** | arXiv 2025 | Trusted/Untrusted Isolation | Claude 3.5 Sonnet | – | 64.95% | 0.00% |
|  | **PFI** | arXiv 2025 | Trusted/Untrusted Isolation | Gemini 1.5 Pro 002 | – | 47.42% | 0.00% |
| DRIFT | **DRIFT** | arXiv 2025 | Dynamic Validation + Isolation | GPT-4o | 71.60% | 62.00% | 1.70% |
|  | **DRIFT** | arXiv 2025 | Dynamic Validation + Isolation | GPT-4o-mini | 57.30% | 50.90% | 1.40% |
|  | **DRIFT** | arXiv 2025 | Dynamic Validation + Isolation | Claude 3.5 Sonnet | 73.40% | 64.20% | 1.50% |
|  | **DRIFT** | arXiv 2025 | Dynamic Validation + Isolation | Claude 3.5 Haiku | 52.30% | 42.40% | 3.30% |
| PromptArmor | **PromptArmor-GPT-3.5** | arXiv 2025 | Injection Span Removal | GPT-4.1 + GPT-3.5 Guard | – | 51.35% | 6.84% |
|  | **PromptArmor-GPT-4o** | arXiv 2025 | Injection Span Removal | GPT-4.1 + GPT-4o Guard | – | 68.68% | 0.47% |
|  | **PromptArmor-GPT-4.1** | arXiv 2025 | Injection Span Removal | GPT-4.1 + GPT-4.1 Guard | – | 72.02% | 0.00% |
|  | **PromptArmor-o4-mini** | arXiv 2025 | Injection Span Removal | GPT-4.1 + o4-mini Guard | – | 76.35% | 0.08% |
| AgentArmor | **AgentArmor** | arXiv 2025 | Program Dependence Graph | GPT-4o-mini | 72% | – | 3% |
|  | **AgentArmor** | arXiv 2025 | Program Dependence Graph | GPT-4o | 72% | – | 4% |
| RTBAS | **RTBAS (LM-Judge)** | arXiv 2025 | IFC + LLM Screening | GPT-4o | – | – | 0% |
|  | **RTBAS (Attention)** | arXiv 2025 | IFC + Attention Screening | GPT-4o + Phi-3-Mini | – | – | 0% |
<!-- TABLE:END -->
