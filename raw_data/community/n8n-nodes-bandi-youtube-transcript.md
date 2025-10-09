# n8n-nodes-youtube-transcript

n8n 워크플로우에서 직접 유튜브 동영상의 자막을 다운로드할 수 있게 해주는 n8n 커뮤니티 노드입니다.

중요! Youtube가 IP 주소를 막으면, 현재 제가 해결할 수 있는 방법은 없습니다. 시간이 지나면 풀릴 수도 있습니다.
보통 이런 에러가 발생합니다.

```bash
Cannot read properties of undefined (reading 'videoId')
```

이 노드는 `youtubei` 라이브러리를 사용하여 유튜브 내부 API와 통신합니다. 따라서 유튜브 인터페이스 변경에 덜 민감하게 작동할 수 있습니다.

[n8n](https://n8n.io/)은 [fair-code 라이선스](https://docs.n8n.io/reference/license/)를 따르는 워크플로우 자동화 플랫폼입니다.

[선행 조건](#선행-조건)
[설치](#설치)
[기능](#기능)
[기여](#기여)
[자료](#자료)
[라이선스](#라이선스)

## 선행 조건

- [n8n](https://n8n.io/)이 설치되어 있고 설정이 완료되어 있어야 합니다.

## 설치

n8n 커뮤니티 노드 문서의 [설치 가이드](https://docs.n8n.io/integrations/community-nodes/installation/)를 따르세요.

이 노드는 `youtubei` 패키지를 사용합니다. 일반적으로 n8n 노드 설치 시 자동으로 의존성이 해결됩니다.

혹시 문제가 발생하면 수동으로 `youtubei`를 설치해야 할 수도 있습니다.

```bash
npm install youtubei
```

## 기능

- **유튜브 자막 다운로드**: 지정된 유튜브 동영상의 자막을 추출하여 워크플로우에서 사용할 수 있도록 텍스트 또는 JSON 형식으로 제공합니다.

  **중요**: 모든 유튜브 동영상에 자막이 있는 것은 아닙니다.

### 지원되는 URL

이 노드는 `youtube.com/watch?v=example` 및 `youtu.be/example` URL 형식을 모두 사용하여 유튜브 동영상에서 자막을 추출할 수 있도록 지원합니다. n8n 워크플로우에 동영상 URL 또는 ID를 제공하기만 하면 나머지는 노드가 알아서 처리합니다.

## 기여

풀 리퀘스트를 환영합니다! 문제점을 발견하거나 개선 사항에 대한 제안이 있는 경우:

1. **저장소를 포크**하고 기능 브랜치를 만듭니다 (`git checkout -b feature/AmazingFeature`).
2. **변경 사항을 커밋**합니다 (`git commit -m 'Add some AmazingFeature'`).
3. **브랜치에 푸시**합니다 (`git push origin feature/AmazingFeature`).
4. **풀 리퀘스트를 엽니다**.

코드가 스타일 가이드를 따르고 해당되는 경우 테스트를 포함하는지 확인하십시오.

## 자료

- [n8n 커뮤니티 노드 문서](https://docs.n8n.io/integrations/community-nodes/)

## 라이선스

이 프로젝트는 [n8n fair-code 라이선스](https://docs.n8n.io/reference/license/)에 따라 라이선스가 부여됩니다.
