# 8시간 수업 교안 — Codex × Claude Code 기반 AI 협업 개발 워크플로우

> 대상: 삼성전자 MX 사업부 실무 개발자
> 문서 유형: 학생용 실습 가이드  
> 수업 목표: 단순 AI 도구 사용법이 아니라, **AI 코딩 에이전트를 실무 개발 워크플로우에 어떻게 배치하고 통제할지** 체험한다.  
>
> 핵심 산출물:  
> 1. Codex 기반 Streamlit 프로젝트 스캐폴딩 결과물 1건  
> 2. Claude Code 기반 코드 분석·리팩토링·테스트 자동화 워크플로우 결과물 1건  
> 3. Git commit tree를 매개로 한 Codex ↔ Claude Code 협업 오케스트레이션 기록 1건  

---

## 1. 전체 시간표

> 총 8시간 기준  
> 점심 1시간 별도 가정  
> 강의 상황에 따라 실습 지연 시 "선택 실습"은 생략 가능

| 파트 | 주제 | 목표 | 사용 도구 |
|---|---|---|---|
| PART 1 | 왜 AI 코딩 에이전트를 배우는가 | 수업 방향, 개발자 역할 변화, 오늘의 산출물 이해 | 슬라이드 |
| PART 2 | LLM 기초 최소화 + 에이전틱 코딩 개념 + MCP 한 줄 예고 | Agent Loop 중심 이해 | 슬라이드 |
| PART 3 | 설치 및 환경 세팅 | VS Code, Python, Streamlit, Codex, Claude Code 준비 | VS Code, Terminal |
| 휴식 |  |  |  |
| PART 4 | Codex로 빠르게 생성하기 | Streamlit 프로젝트 초안 생성 | Codex |
| PART 5 | Claude Code로 기존 코드 분석하기 | 구조 분석, 문제점 도출, 리팩토링 계획 | Claude Code |
| 점심 |  |  |  |
| PART 6 | Codex 멀티 파일 스캐폴딩 | 단일 파일 앱을 프로젝트 구조로 확장 | Codex |
| PART 7 | Claude Code 디버깅·리팩토링 | 로그 분석, 코드 개선, 검증 루프 | Claude Code |
| 휴식 |  |  |  |
| PART 8 | 테스트 자동화와 Git Tree | pytest 생성, 실패 수정, commit 정리 | Claude Code, Git |
| PART 9 | MCP와 도구 연결 개념 | "AI가 어떻게 도구를 쓰는가" 이해 | Claude/Codex |
| PART 10 | Codex × Claude 오케스트레이션 | 생성 AI와 분석 AI의 역할 분리 | Codex, Claude |
| PART 11 | 마무리 | 비용·보안·실무 적용 기준 정리 | 슬라이드 |

---

## 2. 수업 전 준비물 안내

### 필수 준비

- VS Code
- Python 3.11 이상
- Node.js 18 이상 또는 22 이상 권장
- Git
- Codex 사용 가능한 계정
- Claude API 또는 Claude Console 기반 사용 계정
- 인터넷 연결
- 터미널 실행 권한

### 교육 환경 관련 주의

이번 교육 환경에서는 Codex와 Claude가 모두 종량제 기반으로 운영된다.

- Codex는 인당 약 10,000원 수준의 크레딧이 제공된다.
- Claude는 인당 약 4,000원 수준의 크레딧이 제공되며, 사용할 수 있는 횟수가 제한적이다.
- 따라서 Claude는 모든 실습에 남발하지 않고, **코드 분석·리팩토링·최종 검토 단계에서만 제한적으로 사용**한다.
- Codex는 상대적으로 초안 생성, 반복 구현, 간단한 파일 생성 실습에 사용한다.


---

## 3. PART 1 — 왜 AI 코딩 에이전트를 배우는가

### 시간

20분

### 학습 목표

- AI 코딩 도구를 단순 자동완성이 아니라 개발 워크플로우의 일부로 이해한다.
- Codex와 Claude Code의 역할 차이를 이해한다.
- 오늘 수업의 최종 산출물을 이해한다.

### 

### 오늘의 핵심 한 줄

```text
Codex로 빠르게 만들고,
Claude Code로 분석하고,
개발자가 최종 검토한다.
```

### 도구 역할 비교

| 도구 | 오늘의 역할 | 잘 맞는 작업 |
|---|---|---|
| Codex | 빠른 생성, 초안 구현, 멀티 파일 스캐폴딩 | 신규 기능, UI 초안, 반복 구현 |
| Claude Code | 기존 코드 분석, 리팩토링, 테스트 자동화, 품질 검토 | 레거시 코드 분석, 디버깅, 구조 개선 |
| Streamlit | 결과를 눈으로 확인하는 실행 환경 | Python 기반 빠른 웹앱 |
| Git | 변경 이력과 협업 기준점 | commit, diff, review |
| MCP 개념 | AI와 외부 도구 연결 이해 | 파일, 터미널, Git, 테스트, API 연결 |

---

## 4. PART 2 — LLM 기초는 짧게, Agent Loop는 명확하게

### 시간

25분

### 이 파트의 방향

LLM 이론을 깊게 들어가지 않는다. 수강자 피드백 기준으로 LLM 기초는 토큰 이해 정도로 축약하고, 에이전틱 코딩과 에이전트 루프를 강화한다.

### 4-1. 토큰 설명


### 4-2. 에이전틱 코딩 설명

```text
일반 ChatGPT 사용:
질문 → 답변

에이전틱 코딩:
목표 입력
→ AI가 파일 읽기
→ 계획 세우기
→ 코드 수정
→ 터미널 실행
→ 테스트 결과 확인
→ 다시 수정
```

### 4-3. Agent Loop

```text
Observe
현재 코드와 로그를 본다.

Plan
무엇을 바꿀지 계획한다.

Act
파일 수정, 명령 실행, 테스트 실행을 한다.

Verify
결과를 확인한다.

Iterate
실패하면 다시 수정한다.
```

### 4-4. MCP 한 줄 예고 

---

## 5. PART 3 — 설치 및 환경 세팅

### 시간

40분


### 목표

- Streamlit 실행 가능 상태 만들기
- Codex와 Claude Code 실행 확인
- VS Code에서 오른쪽 패널 또는 터미널 기반으로 AI 도구를 사용할 준비 완료

---

### 5-1. 설치 전 주의사항


### 5-2. Python / Streamlit 설치 확인

#### Windows

```powershell
python --version
pip --version
pip install streamlit
streamlit hello
```

#### Mac

```bash
python3 --version
pip3 --version
pip3 install streamlit
streamlit hello
```

### 5-3. Streamlit 첫 앱

파일명: `app.py`

```python
import streamlit as st

st.title("AI Workflow First App")
st.write("Codex와 Claude Code를 활용한 AI 협업 개발 실습입니다.")
```

실행:

```bash
streamlit run app.py
```


> ✅ **PART 3 완료 체크**: 브라우저에 "AI Workflow First App" 제목이 보이면 이 파트 완료. 완료 확인 후 다음 단계로 넘어간다.

---

### 5-4. Claude Code 설치 요약

> 상세 설치는 별도 Claude Code 설치 가이드를 따른다.

#### Mac 권장 설치

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

설치 후 새 터미널에서 확인:

```bash
claude --version
claude doctor
```

#### Windows PowerShell 권장 설치

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
irm https://claude.ai/install.ps1 | iex
```

설치 후 새 PowerShell에서 확인:

```powershell
claude --version
claude doctor
```

### Claude Code 설치 주의사항

- 설치 후 반드시 터미널을 새로 연다.
- `command not found` 또는 인식 오류가 나면 PATH 문제일 가능성이 높다.
- Claude는 오늘 크레딧이 적으므로 설치 확인 이후 불필요한 대화를 하지 않는다.
- Claude Code는 파일 수정이나 명령 실행 전에 권한 요청이 뜰 수 있다. 허용 전 반드시 어떤 명령인지 확인한다.

---

### 5-5. Codex 설치 요약

> 상세 설치는 별도 Codex 설치 가이드를 따른다.

#### Mac 권장 설치

Homebrew 사용 가능 시:

```bash
brew install codex
codex --version
```

Node.js 사용 시:

```bash
npm install -g @openai/codex
codex --version
```

#### Windows 권장 설치

Node.js 확인:

```powershell
node --version
npm --version
```

Codex 설치:

```powershell
npm install -g @openai/codex
codex --version
```

### Codex 설치 주의사항

- Node.js 버전이 낮으면 설치가 실패할 수 있다.
- Windows PowerShell에서 `npm.ps1 cannot be loaded` 오류가 나면 실행 정책 문제일 수 있다.
- 사내 네트워크에서는 프록시나 인증서 문제로 npm 설치가 막힐 수 있다 → 개인 핫스팟으로 설치 후 사내 네트워크로 전환.
- 설치 후 반드시 `codex --version`으로 확인한다.

---

### 5-6. VS Code 권장 배치

| 위치 | 역할 |
|---|---|
| 왼쪽 | Explorer |
| 가운데 | 코드 편집 |
| 오른쪽 | Claude Code / Codex 패널 |
| 아래 | Terminal |
| 브라우저 | Streamlit 실행 결과 |


---

## 6. PART 4 — Codex로 빠르게 생성하기

### 시간

45분

### 목표

- Codex로 Streamlit 앱 초안을 생성한다.
- 자연어 요구사항이 코드로 변환되는 과정을 본다.
- 프롬프트 구조를 이해한다.

---

### 6-1. Codex에 적합한 상황

Codex를 우선 사용하는 상황:

| 상황 | 이유 |
|---|---|
| 새 프로젝트 초안 생성 | 빠르게 여러 파일 생성 가능 |
| UI/화면 구성 초안 | 반복 구현에 적합 |
| 단순 CRUD 생성 | 구조가 명확하면 빠름 |
| 여러 파일 스캐폴딩 | 파일 구조를 한 번에 만들기 좋음 |
| 저비용 반복 실습 | Claude 대비 더 많이 사용 가능 |


---

> 💡 **Codex 실행 화면이 낯설다면**: 부록 B를 먼저 확인한다. Codex CLI를 처음 켜는 방법부터 프롬프트 입력 위치, 파일 생성 화면, 승인 방법까지 단계별로 정리되어 있다.

### 6-2. 프롬프트 작성 공식

```text
[ROLE]
AI가 어떤 역할을 맡을지 정의한다.

[TASK]
무엇을 해야 하는지 정의한다.

[ENV]
개발 환경을 정의한다.

[OUTPUT]
어떤 결과 형식으로 받을지 정의한다.

[CONSTRAINT]
금지사항과 제한 조건을 정의한다.
```

### 6-3. 나쁜 프롬프트 예시

```text
병원 앱 만들어줘
```

문제점:

- 어떤 언어인지 모른다.
- 어떤 화면인지 모른다.
- 단일 파일인지 멀티 파일인지 모른다.
- 실행 방법이 없다.
- 비용과 난이도 통제가 안 된다.

### 6-4. 좋은 프롬프트 예시 — 복붙용

```text
[ROLE]
너는 Python Streamlit 개발자다.

[TASK]
실습용 병원 환자 관리 대시보드 앱을 만들어줘.

[ENV]
- Python 3.11 이상
- Streamlit
- VS Code
- 로컬 실행 환경
- 교육용 실습 프로젝트

[OUTPUT]
- app.py 전체 코드
- 필요한 설치 명령어
- 실행 명령어
- 화면 구성 설명

[CONSTRAINT]
- 외부 DB 사용 금지
- 클래스 사용 금지
- pandas 사용 가능
- 초안 생성이 목적이므로 과도한 기능 추가 금지
- 코드에는 초보자도 이해 가능한 주석 포함
```

### 6-5. 실행 확인

Codex가 생성한 `app.py`를 저장하고 실행한다.

```bash
streamlit run app.py
```


## 7. PART 5 — Claude Code로 기존 코드 분석하기

### 시간

35분

### 목표

- Codex가 만든 기존 코드를 Claude Code로 분석한다.
- 코드의 실행 흐름, 문제점, 개선 방향을 도출한다.
- Claude는 제한된 크레딧이 있으므로 핵심 분석 단계에서만 사용한다.

---

### 7-1. Claude Code에 적합한 상황

| 상황 | 이유 |
|---|---|
| 기존 코드 분석 | 전체 흐름 설명에 강함 |
| 레거시 코드 이해 | 파일 간 관계 분석에 적합 |
| 리팩토링 계획 | 구조 개선 제안에 강함 |
| 디버깅 | 로그와 코드 원인 연결에 강함 |
| 테스트 자동화 | 함수 분석 후 테스트 생성 가능 |
| 아키텍처 리뷰 | 결합도, 책임 분리 분석에 적합 |


---

> 💡 **Claude Code 실행 화면이 낯설다면**: 부록 C를 먼저 확인한다. 프로젝트 폴더에서 실행하는 방법, 파일 인식 화면, Plan Mode 사용법, 수정 승인 화면까지 단계별로 정리되어 있다.

### 7-2. Claude 분석 프롬프트 — 복붙용

```text
현재 프로젝트를 분석해줘.

[분석 범위]
- app.py 전체 실행 흐름
- Streamlit 화면 구성
- 데이터 흐름
- 함수 분리 가능성
- 유지보수 관점의 문제점

[출력 형식]
1. 프로젝트 요약
2. 실행 흐름
3. 좋은 점
4. 개선이 필요한 점
5. 리팩토링 제안

[주의사항]
- 아직 파일을 수정하지 마
- 먼저 분석과 계획만 제시해
- 수정이 필요하면 어떤 파일을 어떻게 바꿀지 계획만 알려줘
```

### 7-3. Claude Plan Mode 사용 멘트

```text
Claude Code를 사용할 때 바로 수정시키는 것보다
처음에는 Plan Mode 또는 Ask before edits를 사용하는 것이 안전합니다.

실무에서는 AI가 자동으로 수정하는 속도보다
수정 전에 사람이 변경 의도를 이해하는 것이 더 중요합니다.
```

### 7-4. Claude 리팩토링 프롬프트 — 복붙용

```text
방금 분석한 내용을 바탕으로 app.py를 리팩토링해줘.

[목표]
- 초보자도 읽기 쉬운 구조로 변경
- 함수로 책임 분리
- 변수명 명확화
- 중복 코드 제거
- 화면 동작은 기존과 동일하게 유지

[제약]
- 외부 DB 추가 금지
- 클래스 사용 금지
- 기능을 과도하게 추가하지 말 것
- 수정 전 변경 계획을 먼저 보여주고 승인 후 진행

[검증]
- 수정 후 streamlit run app.py 기준으로 실행 가능해야 함
```

> ✅ **PART 5 완료 체크**: Claude가 분석 리포트를 출력했고, 리팩토링 계획이 화면에 보이면 완료. Claude Code 화면 기준은 **부록 C-3** 참고. 브라우저 앱은 수정 전과 동일하게 동작해야 한다.

---

## 8. PART 6 — Codex 멀티 파일 스캐폴딩

### 시간

50분

### 목표

- 단일 파일 Streamlit 앱을 멀티 파일 구조로 확장한다.
- 실무 프로젝트에서 파일 구조가 왜 필요한지 이해한다.
- Codex가 여러 파일을 생성하는 흐름을 확인한다.

---

### 8-1. 왜 멀티 파일 구조로 가는가


### 8-2. 목표 파일 구조 (신규 추가)

> 💡 **왜 목표 구조를 먼저 보여주는가**: 수강생이 "완성된 상태"를 모르면 실습 도중 방향을 잃는다. 아래 구조를 슬라이드에 크게 띄워두고 "우리가 만들 구조가 이겁니다"라고 먼저 선언한다.

```text
ai-workflow-demo/
├── app.py                        ← Streamlit 화면 구성만 담당
├── data/
│   └── sample_patients.csv       ← 예제 환자 데이터
├── services/
│   └── patient_service.py        ← 환자 데이터 로딩/저장 담당
├── utils/
│   └── risk_score.py             ← 위험 점수 계산 로직 담당
├── tests/
│   └── test_risk_score.py        ← pytest 테스트 코드
├── README.md
└── requirements.txt
```

각 파일의 역할 요약:

| 파일 | 담당 역할 |
|---|---|
| `app.py` | 화면 구성(UI)만 담당, 비즈니스 로직 없음 |
| `services/patient_service.py` | 환자 데이터 읽기/쓰기 |
| `utils/risk_score.py` | 위험 점수 계산 순수 함수 |
| `tests/test_risk_score.py` | risk_score.py 테스트 |
| `data/sample_patients.csv` | 외부 DB 없이 쓸 수 있는 예제 데이터 |

### 8-3. Codex 멀티 파일 생성 프롬프트 — 복붙용

```text
[ROLE]
너는 Python Streamlit 프로젝트 스캐폴딩을 담당하는 개발자다.

[TASK]
현재 단일 파일 Streamlit 앱을 멀티 파일 프로젝트 구조로 분리해줘.

[ENV]
- Python 3.11 이상
- Streamlit
- pandas
- pytest
- VS Code
- 로컬 실행

[PROJECT STRUCTURE]
아래 구조로 파일을 만들어줘.

ai-workflow-demo/
├── app.py
├── data/
│   └── sample_patients.csv
├── services/
│   └── patient_service.py
├── utils/
│   └── risk_score.py
├── tests/
│   └── test_risk_score.py
├── README.md
└── requirements.txt

[OUTPUT]
- 각 파일 생성
- 각 파일의 역할 설명
- 실행 방법
- 테스트 실행 방법

[CONSTRAINT]
- 외부 DB 사용 금지
- 네트워크 API 호출 금지
- 예제 데이터는 CSV로 포함
- 위험 점수 계산 로직은 utils/risk_score.py에 분리
- app.py는 화면 구성에 집중
```

### 8-4. 실행 명령어

```bash
pip install -r requirements.txt
streamlit run app.py
pytest
```

> ✅ **PART 6 완료 체크**: VS Code 탐색기에서 위 파일 트리가 보이고, `streamlit run app.py`와 `pytest`가 모두 오류 없이 실행되면 완료.

---

## 9. PART 7 — Claude Code 디버깅·리팩토링

### 시간

50분

### 목표

- 일부러 발생시킨 오류를 Claude Code가 터미널 로그와 코드 기반으로 분석하게 한다.
- 리팩토링과 검증 루프를 경험한다.

---

### 9-1. 일부러 만들 수 있는 오류 예시

#### 오류 1: import 오타

```python
import panda as pd
```

#### 오류 2: Streamlit 함수 오타

```python
st.titel("Patient Dashboard")
```

#### 오류 3: 파일 경로 오류

```python
pd.read_csv("sample_patients.csv")
```

실제 파일은 `data/sample_patients.csv`에 있음.

---

### 9-2. Claude 디버깅 프롬프트 — 복붙용

```text
현재 Streamlit 앱 실행 중 에러가 발생했어.

[요청]
1. 터미널 에러 로그를 읽고 원인을 분석해줘.
2. 어떤 파일의 어떤 부분이 문제인지 설명해줘.
3. 수정 계획을 먼저 제시해줘.
4. 승인 후 파일을 수정해줘.
5. 수정 후 실행 또는 테스트로 검증해줘.

[주의]
- 추측만 하지 말고 실제 파일과 로그를 근거로 설명해줘.
- 한 번에 과도한 구조 변경은 하지 마.
- 이번 단계는 디버깅이 목적이므로 최소 수정으로 해결해줘.
```

### 9-3. 리팩토링 프롬프트 — 복붙용

```text
현재 프로젝트를 유지보수 관점에서 리팩토링해줘.

[분석 기준]
- 함수가 너무 길지 않은가
- 한 파일이 너무 많은 책임을 갖고 있지 않은가
- 변수명이 의미를 잘 전달하는가
- 중복 코드가 있는가
- 테스트하기 어려운 구조가 있는가

[수정 목표]
- app.py는 화면 구성에 집중
- 위험 점수 계산은 utils/risk_score.py에 유지
- 데이터 로딩은 services/patient_service.py에 유지
- 테스트 가능한 함수 단위로 정리

[진행 방식]
1. 먼저 리팩토링 계획 제시
2. 내가 승인하면 수정
3. 수정 후 pytest 실행
4. 실패하면 원인 분석 후 재수정
```


## 10. PART 8 — 테스트 자동화와 Git Tree

### 시간

45분

### Git 기본 전제 확인 (신규 추가)

> 💡 **수강생 수준 확인**: MX 수강생은 대부분 Git을 사용하지만, 수준 차이가 있을 수 있다. 시작 전 1분만 투자해서 기본 상태를 확인한다.


### 목표

- Claude Code로 테스트 코드를 생성한다.
- 실패한 테스트를 기반으로 코드를 수정한다.
- Git commit tree를 매개로 변경 흐름을 정리한다.

---

### 10-1. pytest 설치

```bash
pip install pytest
```

또는 `requirements.txt`에 포함:

```text
streamlit
pandas
pytest
```

---

### 10-2. Claude 테스트 생성 프롬프트 — 복붙용

```text
utils/risk_score.py를 분석해서 pytest 테스트 코드를 만들어줘.

[대상]
- utils/risk_score.py
- tests/test_risk_score.py

[요청]
1. 위험 점수 계산 함수의 정상 케이스 테스트
2. 경계값 테스트
3. 잘못된 입력값 테스트
4. 테스트 실행 명령어 안내

[주의]
- 먼저 어떤 테스트 케이스가 필요한지 설명해줘.
- 그 다음 tests/test_risk_score.py를 생성해줘.
- 생성 후 pytest를 실행해서 결과를 확인해줘.
```

---

### 10-3. Git commit 정리

#### 현재 상태 확인

```bash
git status
git diff
```

#### Claude commit 메시지 생성 프롬프트 — 복붙용

```text
현재 git diff를 기준으로 commit 메시지를 작성해줘.

[출력 형식]
- Conventional Commit 형식
- 제목 1줄
- 본문 bullet 3개 이내
- 한국어 설명도 함께 제공

[주의]
- 실제 변경 내용을 과장하지 마
- 테스트 추가 여부를 명확히 적어줘
```

예상 결과:

```text
refactor: separate patient dashboard logic into service and utility modules

- Split data loading and risk score calculation into separate modules
- Add pytest coverage for risk score calculation
- Keep Streamlit app focused on UI composition
```

> ✅ **PART 8 완료 체크**: `pytest` 실행 후 전체 테스트 통과, `git log --oneline`에 commit 이력이 1개 이상 있으면 완료.

---

## 11. PART 9 — MCP와 도구 연결 개념

### 시간

40분

### 이 파트를 후반에 넣는 이유

MCP를 처음부터 설명하면 개념이 어렵다.

하지만 수강자는 이미 오전과 오후 초반에 다음 장면을 보았다.

- AI가 파일을 읽음
- AI가 코드를 수정함
- AI가 터미널 명령을 실행함
- AI가 테스트 결과를 확인함
- AI가 Git diff를 읽음

이 시점에서 MCP를 설명하면 자연스럽다.

> 💡 **PART 2에서 MCP를 한 줄 예고했기 때문에** 이 파트에서 수강생이 "아, 그때 말한 그거"라고 연결할 수 있다.


---

### 11-1. MCP 한 줄 정의

```text
MCP는 AI가 외부 도구를 사용할 수 있게 연결하는 표준 방식입니다.
```

### 11-2. 쉬운 비유

```text
USB가 컴퓨터와 키보드, 마우스, 저장장치를 연결하듯이
MCP는 AI와 외부 도구를 연결합니다.

AI 모델 자체는 말과 추론을 잘하지만,
MCP 같은 연결 구조를 통해
파일 시스템, 터미널, Git, DB, API, 테스트 도구와 연결될 수 있습니다.
```

### 11-3. MCP가 들어간 지점 설명

이번 수업에서 "MCP를 직접 설치하고 서버를 개발하는 것"은 하지 않는다.

대신 다음을 이해한다.

| 우리가 한 작업 | MCP 관점에서의 의미 |
|---|---|
| 프로젝트 파일 읽기 | AI가 파일 시스템 도구를 사용 |
| app.py 수정 | AI가 파일 편집 도구를 사용 |
| streamlit run 실행 | AI가 터미널 도구를 사용 |
| pytest 실행 | AI가 테스트 도구를 사용 |
| git diff 확인 | AI가 Git 정보를 도구로 조회 |
| commit 메시지 생성 | 변경 이력을 기반으로 문서화 |


---

### 11-4. MCP 활용 프롬프트 — 복붙용

#### 파일 시스템 활용

```text
현재 프로젝트의 파일 구조를 읽고,
각 파일이 어떤 역할을 하는지 설명해줘.

그 다음 중복 책임이 있는 파일이 있다면 개선 방향을 제안해줘.
파일은 아직 수정하지 말고 분석만 해줘.
```

#### 터미널 활용

```text
pytest를 실행해서 실패한 테스트가 있는지 확인해줘.

실패하면:
1. 실패한 테스트 이름
2. 실패 원인
3. 관련 파일
4. 최소 수정 방안
을 정리해줘.

수정은 내가 승인한 뒤 진행해줘.
```

#### Git 활용

```text
현재 git diff를 확인하고,
이번 변경이 어떤 목적을 가진 변경인지 요약해줘.

리뷰어 관점에서 확인해야 할 위험 요소도 함께 알려줘.
```

---

## 12. PART 10 — Codex × Claude Code 협업 오케스트레이션

### 시간

30분

### 목표

- Codex와 Claude Code를 경쟁 도구가 아니라 역할이 다른 협업 도구로 이해한다.
- Git Tree를 기준으로 AI 협업 흐름을 정리한다.

---

### 12-1. 오케스트레이션 흐름

```text
1. Codex
   요구사항 기반 초안 생성

2. 사람
   실행 확인 및 방향 조정

3. Claude Code
   기존 코드 분석 및 리팩토링 계획

4. 사람
   수정 승인

5. Claude Code
   디버깅, 리팩토링, 테스트 자동화

6. Git
   변경 내용 기록

7. 사람
   최종 리뷰
```

### 12-2. 최종 통합 프롬프트 — Codex

```text
[ROLE]
너는 빠른 프로토타이핑을 담당하는 AI 개발 에이전트다.

[TASK]
현재 Streamlit 프로젝트에 "환자 위험도 필터링" 기능을 추가해줘.

[ENV]
- Python 3.11 이상
- Streamlit
- pandas
- pytest
- 기존 프로젝트 구조 유지

[OUTPUT]
- 변경 파일 목록
- 수정 코드
- 실행 방법
- 간단한 검증 방법

[CONSTRAINT]
- 기존 함수 이름을 불필요하게 바꾸지 마
- 대규모 리팩토링 금지
- 새 기능 구현에 집중
- 테스트가 필요한 함수가 생기면 테스트 후보를 제안해줘
```

### 12-3. 최종 통합 프롬프트 — Claude Code

```text
Codex가 추가한 변경 사항을 리뷰해줘.

[리뷰 기준]
1. 기존 프로젝트 구조와 잘 맞는가
2. 불필요한 중복 코드가 생겼는가
3. 테스트가 필요한 로직이 있는가
4. 네이밍과 책임 분리가 적절한가
5. 실제 실행 시 문제가 생길 가능성이 있는가

[진행 방식]
- 먼저 git diff를 기준으로 분석해줘.
- 바로 수정하지 말고 리뷰 리포트를 먼저 작성해줘.
- 수정이 필요하면 최소 수정 계획을 제안해줘.
```

```text
여기서 중요한 것은 Codex와 Claude Code 중 하나만 고르는 것이 아닙니다.

실무에서는 작업의 성격에 따라 도구를 나눕니다.

빠르게 만들 때는 Codex.
기존 구조를 읽고 품질을 높일 때는 Claude Code.
최종 판단은 개발자.

이 구조가 AI 협업 개발 워크플로우의 기본입니다.
```

---

## 13. 모델 선택과 비용 최적화

### 13-1. 오늘 수업 운영 기준

| 작업 | 권장 도구/모델 | 이유 |
|---|---|---|
| 단순 UI 생성 | Codex 저비용/mini 계열 | 반복 생성에 적합 |
| Streamlit 초안 | Codex mini 또는 중간 모델 | 빠른 생성 |
| 멀티 파일 스캐폴딩 | Codex 중간 모델 | 여러 파일 생성 |
| 기존 코드 분석 | Claude | 문맥 분석 강점 |
| 리팩토링 계획 | Claude | 구조 개선 강점 |
| 테스트 자동화 | Claude 또는 Codex 중간 모델 | 로직 분석 필요 |
| 최종 아키텍처 리뷰 | Claude 고성능 모델 | 비용은 높지만 가치 큼 |

```text
실무에서는 항상 최고 모델을 쓰는 것이 정답이 아닙니다.

간단한 생성 작업은 저렴한 모델로 충분하고,
기존 코드 분석이나 구조 개선처럼 판단이 필요한 작업은
더 강한 모델을 제한적으로 사용하는 것이 좋습니다.

오늘 Claude 크레딧이 제한적인 이유도
오히려 실무와 비슷합니다.

비용 제약이 있는 상황에서
어떤 작업에 어떤 AI를 쓸지 판단하는 것이 중요합니다.
```

### 13-3. 모델 선택 기준

```text
단순 생성인가?
→ 저렴한 모델

기존 코드의 맥락 이해가 필요한가?
→ 중간 이상 모델

여러 파일과 아키텍처 판단이 필요한가?
→ 고성능 모델 제한 사용

테스트와 검증이 필요한가?
→ 실행 가능한 도구 연결이 있는 에이전트 사용
```

---

## 14. 보안 및 사내 코드 사용 주의

### 반드시 강조할 항목

- 실제 사내 소스코드는 승인된 환경에서만 사용한다.
- API Key를 프롬프트에 직접 붙여넣지 않는다.
- `.env`, 인증 토큰, 개인 정보가 포함된 파일을 AI에게 열람시키지 않는다.
- AI의 코드 수정은 사람이 리뷰한다.
- 자동 실행 권한을 남발하지 않는다.
- `Ask before edits`, `Plan mode`를 먼저 사용한다.
- 위험한 bash/PowerShell 명령은 실행 전 확인한다.

### 위험한 명령 예시

```bash
rm -rf
git reset --hard
git clean -fd
curl ... | bash
powershell Invoke-Expression
```


---

## 15. 자주 발생하는 문제와 대응

### 15-1. streamlit 명령어를 못 찾는 경우

```bash
pip install streamlit
python -m streamlit run app.py
```

Mac:

```bash
pip3 install streamlit
python3 -m streamlit run app.py
```

### 15-2. Codex 인식 안 됨

```bash
codex --version
```

안 되면:

- 터미널 새로 열기
- Node.js 설치 확인
- npm 전역 설치 경로 확인
- Windows는 PowerShell 실행 정책 확인
- 사내 네트워크 차단 → 개인 핫스팟으로 재설치

### 15-3. Claude 인식 안 됨

```bash
claude --version
claude doctor
```

안 되면:

- 새 터미널 열기
- PATH 확인
- 설치 스크립트 재확인
- 권한 문제 확인

### 15-4. Claude 비용이 빠르게 소진되는 경우

운영 팁:

- Claude는 전체 파일 분석 요청을 남발하지 않는다.
- "분석만 해줘, 수정하지 마"로 먼저 요청한다.
- 필요한 파일만 지정한다.
- 동일 질문 반복 금지.
- Codex로 생성하고 Claude는 리뷰 전용으로 사용한다.

### 15-5. AI가 너무 많은 코드를 바꾸는 경우

프롬프트에 다음 문장을 추가한다.

```text
최소 수정으로 해결해줘.
기존 구조를 크게 바꾸지 마.
변경 전 계획을 먼저 보여줘.
```

---

## 16. 최종 산출물 체크리스트

수업 종료 전 수강자에게 확인시킬 것.

### 산출물 1 — Codex 생성 결과

- [ ] Streamlit 앱이 실행된다.
- [ ] `app.py` 또는 멀티 파일 구조가 존재한다.
- [ ] `requirements.txt`가 있다.
- [ ] 브라우저에서 결과를 확인했다.

### 산출물 2 — Claude 분석/리팩토링 결과

- [ ] Claude가 프로젝트 분석 리포트를 작성했다.
- [ ] 리팩토링 계획이 있다.
- [ ] 승인 후 코드가 수정되었다.
- [ ] 수정 후 앱이 정상 실행된다.

### 산출물 3 — 테스트/Git 결과

- [ ] pytest 테스트가 있다.
- [ ] 테스트를 실행했다.
- [ ] `git diff`를 확인했다.
- [ ] commit 메시지를 생성했다.
- [ ] Codex와 Claude의 역할 차이를 설명할 수 있다.

---

## 17. 마무리 멘트

```text
오늘 수업의 핵심은 AI 도구 사용법이 아닙니다.

핵심은 AI를 개발 워크플로우 안에 어떻게 배치하고,
어떤 작업을 맡기고,
어디서 사람이 승인하고,
어떻게 검증할 것인가입니다.

Codex는 빠른 생성에 강하고,
Claude Code는 기존 코드 분석과 품질 개선에 강합니다.

그리고 MCP와 같은 도구 연결 개념은
AI가 단순히 답변하는 수준을 넘어
실제 개발 도구와 연결되어 작업하게 만드는 기반입니다.

앞으로 개발자의 역할은
코드를 모두 직접 작성하는 사람에서
AI 에이전트에게 명확히 지시하고,
결과를 검토하고,
품질과 보안을 책임지는 사람으로 이동하고 있습니다.
```

---

## 19. 참고 자료

- Claude Code 공식 문서: Claude Code는 코드베이스 이해, 기능 구현, 버그 수정, 개발 작업 자동화를 지원한다.
- Claude Code 비용 문서: Claude Code는 API 토큰 사용량 기반으로 과금될 수 있으며, 모델 선택과 코드베이스 크기, 사용 패턴에 따라 비용이 달라진다.
- Claude Code 보안 문서: 기본적으로 읽기 중심 권한에서 시작하고, 파일 수정·테스트 실행·명령 실행 등은 명시적 승인을 요구한다.
- Codex CLI 공식 문서: Codex CLI는 로컬 터미널에서 실행되는 코딩 에이전트이며, 선택한 디렉터리에서 코드를 읽고, 변경하고, 실행할 수 있다.
- Codex 모델 문서: Codex CLI에서는 `/model` 명령 또는 `--model` 옵션으로 모델을 선택할 수 있다.
- Codex 사용량 문서: Codex 사용량은 플랜 및 에이전틱 사용량 제한에 영향을 받는다.

---

## 부록 A. 수업 중 바로 쓰는 프롬프트 모음

### A-1. Codex 초안 생성

```text
[ROLE]
너는 Python Streamlit 개발자다.

[TASK]
실습용 병원 환자 관리 대시보드 앱을 만들어줘.

[ENV]
- Python 3.11 이상
- Streamlit
- VS Code
- 로컬 실행 환경

[OUTPUT]
- app.py 전체 코드
- 설치 명령어
- 실행 명령어
- 화면 구성 설명

[CONSTRAINT]
- 외부 DB 사용 금지
- 클래스 사용 금지
- pandas 사용 가능
- 코드에는 이해하기 쉬운 주석 포함
```

### A-2. Claude 분석

```text
현재 프로젝트를 분석해줘.

1. 프로젝트 요약
2. 실행 흐름
3. 좋은 점
4. 개선이 필요한 점
5. 리팩토링 제안

아직 파일을 수정하지 말고 분석과 계획만 제시해줘.
```

### A-3. Claude 리팩토링

```text
현재 프로젝트를 유지보수하기 쉽게 리팩토링해줘.

조건:
- 함수 분리
- 변수명 명확화
- 중복 제거
- Streamlit 화면 동작 유지
- 수정 전 계획 먼저 제시
- 승인 후 수정
```

### A-4. Claude 디버깅

```text
터미널 에러 로그와 현재 코드를 바탕으로 문제를 분석해줘.

1. 에러 원인
2. 관련 파일과 코드 위치
3. 최소 수정 방안
4. 수정 후 검증 방법

바로 수정하지 말고 먼저 계획을 보여줘.
```

### A-5. 테스트 생성

```text
utils/risk_score.py를 분석해서 pytest 테스트를 만들어줘.

요구사항:
- 정상 케이스
- 경계값 케이스
- 잘못된 입력 케이스
- 테스트 실행 방법 포함

생성 후 pytest 실행 결과까지 확인해줘.
```

### A-6. Git diff 리뷰

```text
현재 git diff를 리뷰해줘.

검토 기준:
- 변경 의도
- 구조 개선 여부
- 잠재 버그
- 테스트 필요 여부
- 리뷰어가 확인해야 할 위험 요소

수정하지 말고 리뷰 리포트만 작성해줘.
```

### A-7. Commit 메시지 생성

```text
현재 git diff를 기준으로 commit 메시지를 작성해줘.

형식:
- Conventional Commit
- 제목 1줄
- 본문 bullet 3개 이내
- 한국어 설명 포함

변경 내용을 과장하지 말고 실제 diff 기준으로 작성해줘.
```

---


---

## 부록 B. Codex CLI 실제 실행 화면 및 조작법


### B-1. Codex 첫 실행 순서

#### 1단계: 프로젝트 폴더로 이동

```bash
# 실습 폴더 생성 및 이동
mkdir ai-workflow-demo
cd ai-workflow-demo
```

#### 2단계: Codex 실행

```bash
codex
```

> 처음 실행하면 OpenAI API Key 입력 화면이 뜬다.

```text
┌─────────────────────────────────────┐
│  Welcome to Codex CLI               │
│                                     │
│  Enter your OpenAI API Key:         │
│  sk-...                             │
└─────────────────────────────────────┘
```

API Key를 붙여넣고 Enter.

#### 3단계: Codex 대화 화면

로그인이 완료되면 아래와 같은 프롬프트 입력창이 뜬다.

```text
┌─────────────────────────────────────────────────┐
│  Codex                                          │
│                                                 │
│  Current directory: /Users/.../ai-workflow-demo │
│                                                 │
│  > _                                            │
└─────────────────────────────────────────────────┘
```

**이 `>` 커서 위치에 프롬프트를 입력한다.**

#### 4단계: 프롬프트 입력 방법

- 짧은 프롬프트: 그냥 타이핑 후 Enter
- 긴 프롬프트 (부록 A의 복붙용 프롬프트): 터미널에 그대로 붙여넣기(Cmd+V / Ctrl+V) 후 Enter

---

### B-2. Codex가 코드를 생성할 때 보이는 화면

프롬프트를 입력하면 Codex가 파일을 생성하는 과정이 실시간으로 출력된다.

```text
> [ROLE] 너는 Python Streamlit 개발자다. ...

  Codex is working...

  Creating app.py
  ████████████████████ 100%

  ✓ app.py created (87 lines)
  ✓ requirements.txt created

  Run with: streamlit run app.py
```

**Codex가 파일을 생성하는 동안 수강생이 해야 할 것: 기다린다.**  
중간에 Enter를 누르거나 Ctrl+C를 누르면 생성이 중단된다.

---

### B-3. Codex가 수정 승인을 요청하는 경우

기존 파일이 있을 때 Codex는 수정 전 확인을 요청할 수 있다.

```text
  Codex wants to modify app.py

  - Remove: lines 12-15 (duplicated logic)
  + Add: calculate_bmi() function

  Approve? [y/n/d(diff)] _
```

- `y` + Enter: 승인하고 수정 진행
- `n` + Enter: 거부
- `d` + Enter: 변경 내용 diff 전체 보기


---

### B-4. Codex 종료 방법

```bash
# 대화 종료
exit
# 또는
Ctrl + C
```

---

### B-5. Codex 자주 쓰는 옵션

| 명령어 | 설명 |
|---|---|
| `codex` | 대화형 모드 시작 |
| `codex "프롬프트"` | 단일 명령 실행 후 종료 |
| `codex --model o4-mini` | 모델 지정 실행 |
| `/help` | 대화 중 도움말 |
| `/clear` | 대화 기록 초기화 |
| `Ctrl+C` | 현재 작업 중단 |

---

## 부록 C. Claude Code 프로젝트 인식 방법 및 실행 흐름


### C-1. Claude Code 실행 전 필수 확인

**반드시 프로젝트 폴더 안에서 실행해야 한다.**

```bash
# 현재 위치 확인
pwd
# 출력 예: /Users/username/ai-workflow-demo

# 폴더 안에 파일이 있는지 확인
ls
# 출력 예: app.py  requirements.txt
```

> ⚠️ 홈 디렉토리(`~`)나 엉뚱한 폴더에서 실행하면 Claude가 프로젝트를 찾지 못한다.

---

### C-2. Claude Code 첫 실행 순서

#### 1단계: 프로젝트 폴더에서 실행

```bash
cd ai-workflow-demo   # 반드시 프로젝트 폴더로 이동
claude                 # Claude Code 실행
```

#### 2단계: 처음 실행 시 인증 화면

```text
┌─────────────────────────────────────┐
│  Claude Code                        │
│                                     │
│  Login with Anthropic Console?      │
│  [Enter] to open browser            │
└─────────────────────────────────────┘
```

Enter를 누르면 브라우저가 열리고 Anthropic 로그인 화면이 뜬다. 로그인 후 터미널로 돌아온다.

#### 3단계: Claude Code 대화 화면

```text
┌──────────────────────────────────────────────────┐
│  Claude Code  ✓ Connected                        │
│                                                  │
│  Project: /Users/username/ai-workflow-demo       │
│  Files detected: app.py, requirements.txt        │
│                                                  │
│  > _                                             │
└──────────────────────────────────────────────────┘
```

**"Files detected"에 프로젝트 파일이 보이면 정상이다.**  
이 상태에서 프롬프트를 입력하면 Claude가 해당 파일들을 읽고 분석한다.

---

### C-3. Claude Code가 프로젝트를 분석할 때 보이는 화면

```text
> 현재 프로젝트를 분석해줘. 실행 흐름과 문제점을 찾아줘.

  ● Reading app.py...
  ● Reading requirements.txt...
  ● Analyzing code structure...

  # 프로젝트 분석 결과

  ## 1. 프로젝트 요약
  병원 환자 관리 대시보드. Streamlit 기반 단일 파일 앱.
  pandas로 데이터 처리, session_state로 환자 목록 관리.

  ## 2. 실행 흐름
  1. 앱 시작 → session_state 초기화
  2. 사이드바: 환자 등록 폼
  3. 메인 영역: 환자 목록 테이블 + 검색

  ## 3. 개선이 필요한 점
  - app.py 한 파일에 UI·데이터·로직이 혼재
  - 함수 분리 없이 전체가 순차 실행 구조
  - 테스트 작성 불가능한 구조

  수정하기 전에 계획을 먼저 보여드릴까요? [y/n]
```

**"수정하기 전에 계획을 먼저 보여드릴까요?"가 뜨면 반드시 `y`로 확인 후 진행한다.**

---

### C-4. Plan Mode 사용법

Plan Mode는 Claude가 코드를 수정하기 전에 계획만 보여주는 모드다.

#### 방법 1: 프롬프트에 명시

```text
분석해줘. 파일은 아직 수정하지 마.
```

#### 방법 2: 설정에서 Plan Mode 켜기

```bash
# Claude Code 실행 중 설정 메뉴
/config
→ Ask before edits: ON
```

이 설정을 켜면 모든 파일 수정 전에 Claude가 먼저 확인을 요청한다.

---

### C-5. Claude Code 파일 수정 승인 화면

```text
  Claude wants to make the following changes:

  app.py
  ──────
  - def main():                          (삭제)
  -     st.title("Patient Dashboard")   (삭제)
  + def render_header():                 (추가)
  +     """화면 상단 제목을 렌더링한다."""  (추가)
  +     st.title("Patient Dashboard")    (추가)

  Approve this change? [y/n/e(edit)/d(diff)]
```

- `y`: 승인
- `n`: 거부
- `e`: 수정 내용 직접 편집
- `d`: 전체 diff 보기

---

### C-6. Claude Code 자주 쓰는 명령

| 명령어 | 설명 |
|---|---|
| `claude` | 프로젝트 폴더에서 실행 |
| `/help` | 도움말 |
| `/config` | 설정 (Plan Mode, 모델 변경 등) |
| `/clear` | 대화 기록 초기화 |
| `/cost` | 현재까지 사용한 비용 확인 |
| `Ctrl+C` | 현재 작업 중단 |
| `Escape` | 입력 취소 |

> 💡 **비용 관리 팁**: `/cost` 명령으로 수시로 남은 크레딧을 확인하게 유도한다. 수강생이 크레딧을 얼마나 썼는지 모르면 후반 실습에서 잔액이 없을 수 있다.

---

## 부록 D. Streamlit 정상 결과물 화면 기준


---

### D-1. PART 3 완료 기준 — Streamlit Hello 화면

브라우저 `localhost:8501`에서 아래 화면이 뜨면 정상이다.

```text
┌──────────────────────────────────────────────┐
│  🎈 Welcome to Streamlit!                    │
│                                              │
│  If you're one of our development partners   │
│  or you're looking at this as part of your   │
│  product strategy...                         │
│                                              │
│  [Demo widgets, charts, sliders 등 표시]     │
└──────────────────────────────────────────────┘
```

**이 화면이 뜨면 Streamlit 설치 완료.**  
터미널에 `Ctrl+C`를 눌러 종료 후 다음 단계로 이동한다.

---

### D-2. PART 3 완료 기준 — 첫 앱 실행 화면

`streamlit run app.py` 실행 후 브라우저에서 아래 화면이 뜨면 정상이다.

```text
┌──────────────────────────────────────────────┐
│  AI Workflow First App                       │
│                                              │
│  Codex와 Claude Code를 활용한                │
│  AI 협업 개발 실습입니다.                     │
└──────────────────────────────────────────────┘
```

터미널 출력도 확인:

```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501

  [에러 메시지 없이 이 두 줄이 뜨면 정상]
```

---

### D-3. PART 4 완료 기준 — 환자 관리 앱 화면

Codex가 생성한 앱을 `streamlit run app.py`로 실행하면 아래와 같은 화면이 나와야 한다.

```text
┌──────────────────────────────────────────────────────┐
│  🏥 환자 관리 대시보드                                │
│                                                      │
│  ┌─ 사이드바 ──────────┐                             │
│  │  환자 등록          │  환자 목록                  │
│  │  이름: [______]    │  ┌────┬────┬──────┬──────┐  │
│  │  나이: [__]        │  │ # │이름│ 나이 │진료과│  │
│  │  진료과: [______]  │  ├────┼────┼──────┼──────┤  │
│  │  [등록하기]        │  │ 1 │... │  ... │ ...  │  │
│  └────────────────────┘  └────┴────┴──────┴──────┘  │
│                                                      │
│  검색: [____________]                                │
└──────────────────────────────────────────────────────┘
```

**확인할 것:**
- [ ] 사이드바에 입력 폼이 있는가
- [ ] 환자 등록 후 테이블에 행이 추가되는가
- [ ] 검색창에 입력하면 테이블이 필터링되는가
- [ ] 터미널에 빨간 에러가 없는가

---

### D-4. PART 6 완료 기준 — 멀티 파일 구조

VS Code 탐색기에서 아래 구조가 보이면 정상이다.

```text
ai-workflow-demo/
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📁 data/
│   └── 📄 sample_patients.csv
├── 📁 services/
│   └── 📄 patient_service.py
├── 📁 utils/
│   └── 📄 risk_score.py
└── 📁 tests/
    └── 📄 test_risk_score.py
```

터미널에서 실행 확인:

```bash
streamlit run app.py
# → 브라우저에 동일한 환자 관리 앱이 뜨면 정상

pytest
# → 아래와 같이 PASSED가 뜨면 정상
```

```text
========================= test session starts ==========================
platform darwin -- Python 3.11.x
collected 3 items

tests/test_risk_score.py ...                                     [100%]

========================== 3 passed in 0.12s ===========================
```

---

### D-5. 자주 보이는 오류 화면과 대응

#### 오류 1: ModuleNotFoundError

```text
ModuleNotFoundError: No module named 'streamlit'
```

대응:
```bash
pip install streamlit
# 또는
pip install -r requirements.txt
```

#### 오류 2: FileNotFoundError

```text
FileNotFoundError: [Errno 2] No such file or directory: 'sample_patients.csv'
```

대응: 파일 경로 확인
```bash
# 실행 위치가 프로젝트 루트인지 확인
pwd
ls data/
```

#### 오류 3: Port already in use

```text
Port 8501 is already in use
```

대응:
```bash
# 기존 Streamlit 프로세스 종료 후 재실행
streamlit run app.py --server.port 8502
```

#### 오류 4: pytest 실패

```text
FAILED tests/test_risk_score.py::test_normal_case - AssertionError
```

대응: Claude Code에 아래 프롬프트 입력
```text
pytest 실패 원인을 분석하고 최소 수정으로 해결해줘.
수정 전 계획 먼저 보여줘.
```

---


---

## 부록 E. 실습용 기준 코드 파일 목록

> 실습 중 참고용 기준 코드 세트입니다.
> 용도 1: Codex 생성 결과가 이상할 때 배포  
> 용도 2: 설치 실패 수강생이 PART 5부터 합류할 때 배포  
> 용도 3: PART 7 디버깅 실습에서 오류를 심을 기준 코드

포함 파일:

```text
ai-workflow-demo/
├── app.py                        ← PART 4 완성본
├── data/
│   └── sample_patients.csv       ← 예제 데이터 20건
├── services/
│   └── patient_service.py        ← PART 6 완성본
├── utils/
│   └── risk_score.py             ← PART 6 완성본
├── tests/
│   └── test_risk_score.py        ← PART 8 완성본
├── README.md
└── requirements.txt
```

각 파일은 이 교안과 함께 제공되는 Python 파일 세트를 사용한다.

