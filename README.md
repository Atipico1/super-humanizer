# Super Humanizer

**실제로 생성한 글에서 패턴을 찾고, 작성 모델에 맞춰 한국어 초안을 다듬는 Claude Code · Codex 플러그인**입니다.

사람 글 **34편**과 같은 소재로 Opus 5·Fable 5.1·Astra 6가 쓴 **102편**을 비교했습니다. 어떤 표현이 나왔는지뿐 아니라, 사람 글보다 얼마나 자주 쓰였는지, 어느 모델과 문맥에서 두드러지는지 살펴 윤문 지침을 구성했습니다.

별도 API 키, 서버, 패키지 설치가 필요하지 않습니다. 로그인한 Claude Code 또는 Codex의 모델이 스킬을 읽고 작업합니다.

## 모든 AI에 같은 규칙을 적용하지 않습니다

모델마다 글을 전개하고 강조하고 마무리하는 습관이 다릅니다. **모든 모델과 장르를 관통하는 하나의 교정 규칙이 있다고 가정하지 않습니다.** 같은 표현도 어떤 글에서는 반복적인 수사이고, 다른 글에서는 꼭 필요한 설명입니다.

그래서 Super Humanizer는 실제 생성 결과에서 출발합니다. 모델별로 두드러진 경향을 찾고, 그 경향이 글에서 어떤 역할을 하는지 판단한 다음 수정합니다. 모델 이름은 금지어 목록을 고르는 용도가 아니라 **먼저 살펴볼 구간과 수정 조건을 정하는 정보**입니다.

| 설계 원칙 | 실제 구성 |
|---|---|
| 생성해보고 찾기 | 같은 소재를 세 모델에 직접 집필시켜 사람 원문과 비교 |
| 모델별로 살피기 | 모델별 빈도와 문맥 차이를 바탕으로 각각의 참고 문서 작성 |
| 예시로 판단하기 | 눈여겨볼 형태·문제·수정 전후·유지할 반례를 함께 제공 |
| 윤문과 평가 구분하기 | 윤문 스킬과 별도로 내용 보존·유창성·담화·문체 평가 스킬 제공 |

이 저장소의 `common-patterns.md`도 모든 AI에 적용되는 확정적 법칙은 아닙니다. 여러 모델에서 함께 살펴볼 **조건부 편집 기준**을 모은 문서입니다. 모델별 문서는 여기에 우선순위와 실제 사례를 더합니다. 사람도 쓰는 질문·목록·짧은 문장·따옴표를 일괄 금지하지 않습니다.

## 어떻게 만들었나

1. **사람 글을 선정했습니다.** 필자 신뢰성과 글의 품질을 보고 블로그·뉴스레터·기명 칼럼 100편을 선정하고, 그중 34편으로 비교 실험을 진행했습니다.
2. **세 모델에 실제로 글을 쓰게 했습니다.** 각 원문을 요약한 뒤, 같은 소재에 대해 짧고 일상적인 집필 요청을 주어 모델마다 34편씩 생성했습니다. 특정 문체나 AI 패턴을 넣으라는 요청은 하지 않았습니다.
3. **사람과 AI, 모델과 모델을 비교했습니다.** 사전 정의한 6개 패턴을 집계하고, 추가 관찰 46건을 묶어 18개 항목으로 재분석했습니다. 글 길이를 고려한 빈도와 실제 문맥을 함께 확인했습니다.
4. **관찰을 윤문 지침으로 옮겼습니다.** 반복되는 경향에 수정 조건과 예시를 붙이고, 같은 형태라도 유지해야 할 반례를 함께 정리했습니다. 관찰한 패턴을 전부 삭제 규칙으로 만들지는 않았습니다.

현재 모델별 점검 방향은 다음과 같습니다. 해당 모델에서만 나타나는 독점적 특징을 뜻하지는 않습니다.

| 작성 모델 | 먼저 살펴볼 경향 |
|---|---|
| Opus 5 | 반복 대조, 짧은 판단·문장 조각의 강조, 소제목 뒤의 빈 예고 |
| Fable 5.1 | 같은 결론을 변주하는 대조, 나열 뒤 총평, 목록 앞의 반복 안내 |
| Astra 6 | 유보한 뒤 제한된 긍정으로 돌아오는 전개, 같은 장면의 재설명 |

모든 경향의 근거 강도가 같지는 않습니다. 예를 들어 Astra의 장면 재설명은 모델 특화 경향이 아니라 공통 중복 점검의 실제 수정 사례입니다. 표본 구성, 빈도와 한계는 [연구 요약](docs/RESEARCH.md)에 공개했습니다. 최신 지침이 경쟁 스킬보다 우수하다거나 모델별 지침의 추가 효과가 입증됐다는 주장은 하지 않습니다.

## 이런 부분을 다듬습니다

실제 실험 초안에서 발췌한 문장과 편집 제안입니다.

**전**

> 도착한 뒤에도 도착을 기다리는 사람. 이미 와 있는데도 아직 오지 않았다고 느끼는 사람.

**후 — 편집 제안**

> 도착한 뒤에도 도착을 기다리는 사람.

두 번째 문장은 앞의 판단을 다시 풀어 썼습니다. 반면 같은 글의 **“어쩌면 지금도.”**는 과거의 감각을 현재로 옮기므로 유지합니다. 짧은 문장이나 특정 부호를 전부 없애는 방식이 아닙니다.

## 설치

플러그인 기능을 지원하는 Claude Code 또는 Codex를 준비하세요. 설치 후 새 세션/작업을 시작합니다.

### Claude Code

Claude Code 안에서 실행합니다.

```text
/plugin marketplace add Atipico1/super-humanizer
/plugin install super-humanizer@super-humanizer
```

터미널에서 설치하려면:

```sh
claude plugin marketplace add Atipico1/super-humanizer
claude plugin install super-humanizer@super-humanizer
```

### Codex

터미널에서 실행합니다.

```sh
codex plugin marketplace add Atipico1/super-humanizer
codex plugin add super-humanizer@super-humanizer
```

Codex 앱을 사용 중이면 설치 후 새 작업을 시작하세요. 바로 표시되지 않으면 앱을 다시 시작하고 Plugins에서 `Super Humanizer`를 확인합니다. CLI에서는 `/plugins`로 설치 상태를 확인할 수 있습니다.

`codex plugin` 명령이 없다면 해당 명령을 지원하는 버전으로 업데이트하세요. 이 저장소의 설치 명령은 Codex CLI 0.149.1, Claude Code 2.1.228을 기준으로 확인했습니다.

## 사용

### 한국어 글 윤문

Claude Code:

```text
/super-humanizer:super-humanizer-ko

아래는 Opus 5로 작성한 블로그 초안이야.
사실과 말투의 격식은 유지하면서 반복되는 AI 말투를 다듬어줘.

[초안]
```

Codex:

```text
$super-humanizer-ko

아래는 Astra 6로 작성한 뉴스레터 초안이야.
내용과 화자의 태도를 유지하면서 자연스럽게 다듬어줘.

[초안]
```

작성 모델을 몰라도 사용할 수 있습니다. 모델을 알려주면 공통 규칙에 해당 모델의 참고 문서를 더해 읽습니다. 평소 쓴 글이 있다면 문체 샘플과 독자·격식도 함께 알려주세요. 기본 출력은 윤문한 본문이며, 설명이 필요하면 변경 이유도 요청할 수 있습니다.

**작성 모델 선택은 모델 전환 명령이 아닙니다.** 플러그인은 모델을 호출하거나 변경하지 않습니다. 초안과 같은 모델로 윤문하려면 Claude Code/Codex에서 실행 모델을 직접 맞추세요. Opus 5·Fable 5.1·Astra 6는 이 프로젝트의 실험에서 사용한 모델 식별자이며, 서비스별 선택 가능 여부와 명칭은 다를 수 있습니다.

### 윤문 후보 비교

Claude Code에서는 `/super-humanizer:review-ai-writing-ko`, Codex에서는 `$review-ai-writing-ko`를 선택합니다.

```text
원문과 후보 A/B를 비교해줘.
내용·태도 보존과 유창성·전개·문체를 구분해서 평가하고,
실제 문구를 근거로 선호 또는 동률을 알려줘.

[원문]
[후보 A]
[후보 B]
[가능하면 같은 장르의 사람 참조 글]
```

평가 결과는 사람이 검토할 판단 자료입니다. AI 작성 확률이나 인간 작성 인증을 출력하지 않습니다. 사람 참조가 없으면 사람 대비 사용 빈도는 판단하지 않습니다.

## 포함된 스킬

| 스킬 | 역할 |
|---|---|
| `super-humanizer-ko` | 한국어 윤문. 공통 패턴과 Opus 5·Fable 5.1·Astra 6 참고 문서 |
| `review-ai-writing-ko` | 내용 보존과 유창성·담화·문체를 나누어 평가 |

현재 연구와 예시는 **한국어 블로그·뉴스레터·기명 칼럼** 중심입니다. 영어 윤문이나 모든 모델·장르에서의 효과는 검증하지 않았습니다. 연구 표본은 작고 자동 평가가 포함되어 있으며, 최신 예시 보완판의 성능 대조 실험은 아직 없습니다. 자세한 조건은 [연구 요약](docs/RESEARCH.md)에 있습니다.

이 플러그인은 프롬프트 문서만 포함합니다. 별도 서버·MCP·실행 훅·외부 전송 코드는 없습니다. 입력한 글의 처리는 사용 중인 Claude Code/Codex와 선택한 모델 서비스의 설정을 따릅니다.

## 업데이트와 삭제

Claude Code 터미널 명령:

```sh
claude plugin marketplace update super-humanizer
claude plugin update super-humanizer@super-humanizer
```

Codex 터미널 명령:

```sh
codex plugin marketplace upgrade super-humanizer
codex plugin add super-humanizer@super-humanizer
```

업데이트 후 새 세션을 시작합니다. 로컬 경로로 설치한 경우 먼저 해당 저장소에서 `git pull`을 실행하세요.

삭제:

```sh
claude plugin uninstall super-humanizer@super-humanizer
# 또는
codex plugin remove super-humanizer@super-humanizer
```

## 로컬에서 수정하며 사용하기

```sh
git clone https://github.com/Atipico1/super-humanizer.git
cd super-humanizer
```

Claude Code에서 설치 없이 한 세션만 시험하려면:

```sh
claude --plugin-dir ./plugins/super-humanizer
```

Codex에 로컬 마켓플레이스로 등록하려면:

```sh
codex plugin marketplace add "$PWD"
codex plugin add super-humanizer@super-humanizer
```

GitHub 설치와 로컬 설치는 같은 마켓플레이스 이름을 사용합니다. 둘을 동시에 등록하지 마세요. 전환이 필요하면 기존 마켓플레이스를 제거한 뒤 원하는 주소를 등록합니다. [공식 Codex 문서](https://developers.openai.com/plugins/build/plugins)와 [Claude Code 문서](https://code.claude.com/docs/en/plugin-marketplaces)에서 마켓플레이스 관리 방법을 확인할 수 있습니다.

## 디렉토리

```text
.agents/plugins/marketplace.json     # Codex 마켓플레이스
.claude-plugin/marketplace.json      # Claude Code 마켓플레이스
plugins/super-humanizer/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── LICENSE
└── skills/
    ├── super-humanizer-ko/
    │   ├── SKILL.md
    │   └── references/
    │       ├── common-patterns.md
    │       ├── opus5.md
    │       ├── fable51.md
    │       └── astra6.md
    └── review-ai-writing-ko/
        ├── SKILL.md
        └── references/rubric.md
docs/RESEARCH.md                     # 공개 연구 요약
scripts/validate_package.py         # 배포 구조·참조 검사
```

두 플랫폼은 같은 스킬 파일을 사용합니다. 수집한 글 본문, 실험 입력·출력, 개인 경로와 실행 로그는 배포에 포함하지 않습니다. 스킬의 짧은 예시 발췌는 포함합니다.

## 기여

실제 문장, 독자·장르, 수정안과 **수정하지 않아야 하는 경우**를 함께 제안해주세요. 한 문구의 출현만으로 새 금지 규칙을 추가하기보다, 문맥에서 어떤 문제가 생기는지 설명하는 기여를 환영합니다. 공유할 권한이 없는 원문이나 민감한 정보는 이슈에 붙이지 말아주세요.

스킬은 `plugins/super-humanizer/skills/`에서 수정합니다. 변경 후 아래 검사를 실행하세요. 배포할 때는 두 `plugin.json`의 버전을 함께 올립니다.

```sh
python3 scripts/validate_package.py
claude plugin validate plugins/super-humanizer
claude plugin validate .claude-plugin/marketplace.json
```

## 참고와 라이선스

[blader/humanizer](https://github.com/blader/humanizer)의 패턴 설명·수정 전후 형식과 [im-not-ai](https://github.com/epoko77-ai/im-not-ai)를 조사하며 구성했습니다. 한국어 규칙은 로컬 비교 연구와 편집 판단을 바탕으로 작성했습니다. 외부 프로젝트의 명성이나 규칙 수를 이 스킬의 성능 근거로 삼지 않습니다.

[MIT License](LICENSE). 공식 Anthropic/OpenAI 플러그인이 아닌 독립 커뮤니티 프로젝트입니다.
