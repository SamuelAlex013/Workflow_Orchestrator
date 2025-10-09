# n8n-nodes-openai-analytics

This package provides custom nodes for the [n8n](https://n8n.io/) workflow automation tool to integrate with the [OpenAI API](https://platform.openai.com/docs).

이 패키지는 [n8n](https://n8n.io/) 워크플로우 자동화 도구를 위한 [OpenAI API](https://platform.openai.com/docs) 커스텀 노드를 제공합니다.

## Features / 기능

This package offers the following features to leverage OpenAI API in n8n workflows:

n8n 워크플로우에서 OpenAI API를 쉽게 활용할 수 있도록 다음 기능을 제공합니다:

### Thread Operations / Thread 작업

- Create Thread / Thread 생성
- Add Message to Thread / Thread에 메시지 추가
- Run Thread / Thread 실행
- Create and Run Thread (All in one) / Thread 생성 및 실행 (한 번에)
- Run Existing Thread / 기존 Thread 실행
- Check Run Status / Run 상태 확인
- List Thread Messages / Thread의 메시지 목록 조회
- Get Thread / Thread 정보 조회

### Assistant Operations / Assistant 작업

- Get Assistants List / Assistant 목록 조회
- Create Assistant / Assistant 생성
- Get Assistant Details / 특정 Assistant 정보 조회

### File Operations / File 작업

- Get Files List / File 목록 조회
- Get File Details / 특정 File 정보 조회
- Upload File / 파일 업로드
- Download File / 파일 다운로드

### Embedding Operations / Embedding 작업

- Create Embeddings from Text / 텍스트를 임베딩 벡터로 변환
- Embedding Based Classification / 임베딩 기반 텍스트 분류
- LLM Based Classification / LLM 기반 텍스트 분류
- Cosine Similarity / 코사인 유사도 계산

### Text Operations / Text 작업

- Parse JSON / JSON 파싱

### Report Operations / Report 작업

- Generate HTML Report / HTML 보고서 생성

## Requirements / 요구사항

- n8n version 1.0.0 or later / n8n 버전 1.0.0 이상
- Node.js 16 or later / Node.js 16 이상

## Installation / 설치

### Install as n8n Community Node / n8n Community 노드로 설치

1. Go to n8n instance Settings > Community Nodes / n8n 인스턴스 설정 > 커뮤니티 노드 페이지로 이동
2. Search for `n8n-nodes-openai-analytics` / `n8n-nodes-openai-analytics` 검색
3. Click the Install button / 설치 버튼 클릭

### Manual Installation / 수동 설치

Install this package in the appropriate location within your n8n installation directory.

이 패키지를 n8n 설치 디렉토리 내의 적절한 위치에 설치하십시오.

```bash
# Using npm / npm 사용
npm install n8n-nodes-openai-analytics

# Install in n8n custom extensions folder / n8n 커스텀 확장 폴더에 설치
cd ~/.n8n/custom
npm install n8n-nodes-openai-analytics
```

### Installation for Local Development / 로컬 개발 설치

```bash
# Build project and install to local n8n / 프로젝트 빌드 및 로컬 n8n에 설치
npm run install-local
```

## Usage / 사용 방법

1. Access your n8n instance and create a new workflow / n8n 인스턴스에 접속하여 새 워크플로우 생성
2. Add the OpenAI Analytics node / OpenAI Analytics 노드 추가
3. Set up authentication with your OpenAI API key / OpenAI API 키로 인증 정보 설정
4. Select the desired resource and operation / 원하는 리소스와 작업 선택
5. Enter the required parameters / 필요한 매개변수 입력
6. Run the workflow / 워크플로우 실행

## Examples / 예제

### Create Assistant / Assistant 생성

1. Add OpenAI Analytics node / OpenAI Analytics 노드 추가
2. Select `Assistant` resource / `Assistant` 리소스 선택
3. Select `Create Assistant` operation / `Create Assistant` 작업 선택
4. Enter the following parameters / 다음 매개변수 입력:
   - Assistant Name: Name for your new assistant / 새로운 어시스턴트 이름
   - Description: Optional description / 설명 (선택 사항)
   - System Instructions: System prompts for the assistant / 어시스턴트 지시사항
   - Model: Select AI model (e.g., gpt-4o) / AI 모델 선택 (예: gpt-4o)
   - Tools: Select which tools to enable (Code Interpreter, Retrieval, Function Calling) / 사용할 도구 선택 (코드 인터프리터, 검색, 함수 호출)
   - Response Format: Select auto, text, or JSON / 응답 형식 선택 (자동, 텍스트, JSON)
   - Advanced Settings: Configure temperature, top p and metadata / 고급 설정: 온도, top p 및 메타데이터 구성
5. Run the workflow / 워크플로우 실행

### Create and Run Thread / Thread 생성 및 실행

1. Add OpenAI Analytics node / OpenAI Analytics 노드 추가
2. Select `Thread` resource / `Thread` 리소스 선택
3. Select `Create and Run Thread` operation / `Create and Run Thread` 작업 선택
4. Enter the following parameters / 다음 매개변수 입력:
   - Assistant ID: ID of the Assistant to use / 사용할 Assistant의 ID
   - Initial Message: Message content to add to the thread / 스레드에 추가할 메시지 내용
   - Wait for Completion: Whether to wait for the run to complete / 실행 완료 대기 여부
5. Run the workflow / 워크플로우 실행

### Run Embedding Based Classification / 임베딩 기반 분류 실행

1. Add OpenAI Analytics node / OpenAI Analytics 노드 추가
2. Select `Embedding` resource / `Embedding` 리소스 선택
3. Select `Embedding Based Classify` operation / `Embedding Based Classify` 작업 선택
4. Enter the following parameters / 다음 매개변수 입력:
   - Target Text: Text to classify / 분류할 텍스트
   - Embedding Model: Model to use for embeddings / 임베딩에 사용할 모델
   - Categories: Define classification categories / 분류 카테고리 정의
   - Similarity Threshold: Minimum similarity score for classification / 분류 최소 유사도 점수
5. Run the workflow / 워크플로우 실행

### Calculate Cosine Similarity / 코사인 유사도 계산

1. Add OpenAI Analytics node / OpenAI Analytics 노드 추가
2. Select `Embedding` resource / `Embedding` 리소스 선택
3. Select `Cosine Similarity` operation / `Cosine Similarity` 작업 선택
4. Enter the following parameters / 다음 매개변수 입력:
   - Input Method: Direct input, JSON Path, or Binary Property / 입력 방식 선택
   - Embedding Vector 1: First vector for comparison / 비교할 첫 번째 벡터
   - Embedding Vector 2: Second vector for comparison / 비교할 두 번째 벡터
5. Run the workflow / 워크플로우 실행

### Generate HTML Report / HTML 보고서 생성

1. Add OpenAI Analytics node / OpenAI Analytics 노드 추가
2. Select `Report` resource / `Report` 리소스 선택
3. Select `Generate HTML Report` operation / `Generate HTML Report` 작업 선택
4. Enter the following parameters / 다음 매개변수 입력:
   - Prompt: Instructions for the report generation / 보고서 생성 지시 프롬프트
   - Input Text: Text data to analyze / 분석할 텍스트 데이터
   - OpenAI Model: Model to use for report generation / 보고서 생성에 사용할 모델
   - Include Default Libraries: Whether to include Bootstrap, ChartJS, etc. / 기본 UI 라이브러리 포함 여부
5. Run the workflow / 워크플로우 실행

## Development / 개발

```bash
# Install dependencies / 의존성 설치
npm install

# Run in development mode / 개발 모드 실행
npm run dev

# Build the project / 빌드
npm run build

# Create a symbolic link to your local n8n instance / n8n 로컬 인스턴스에 심볼릭 링크 생성
npm link

# Connect with your local n8n instance / n8n 로컬 인스턴스와 연결
cd ~/.n8n/custom
npm link n8n-nodes-openai-analytics
```

## License / 라이선스

[MIT](LICENSE)
