# Solapi for n8n (Community Node)

솔라피(Solapi) 메시지/카카오/커머스 웹훅을 n8n에서 쉽게 사용하기 위한 커뮤니티 노드입니다.

## 설치

- n8n Community Nodes에서 설치
  - n8n UI → Settings → Community Nodes → Install → `n8n-nodes-solapi` 입력
- 또는 수동 설치
  - 프로젝트에 패키지 설치 후 n8n 재기동

## 인증 설정 (OAuth2)
1) n8n → Credentials → New → `Solapi OAuth2 API` 선택
2) Solapi 콘솔에서 발급받은 Client ID/Secret 입력
3) Scope 기본값 유지(권장):
```
message:write message:read senderid:read storage:write storage:read webhook:read webhook:write kakao:write kakao:read users:read contacts:read contacts:write commerce:read commerce:write
```
4) Save & Connect로 로그인 → 연결 성공 확인

## 인증 설정 (API Key)
1) n8n → Credentials → New → `Solapi API Key` 선택
2) Solapi 콘솔에서 발급받은 API Key / API Secret 입력
3) 노드의 `Authentication`에서 `API Key (HMAC-SHA256)` 선택
4) 사용 시 각 요청에는 문서에 따라 HMAC-SHA256 시그니처가 자동으로 포함됩니다. 상세: [Solapi API Key 인증 방식](https://developers.solapi.com/references/authentication/api-key)

## 사용 가능한 노드/오퍼레이션
리소스 `Message`에서 아래 오퍼레이션을 제공합니다.

- Send Text Message
  - SMS/LMS/MMS 발송
  - 필수: To, From, Text
  - 선택: Subject(LMS), Image ID(MMS), Country Code(기본 82)
  - 동적 옵션: From(발신번호), Image ID(MMS 스토리지)

- Send Kakao AlimTalk (ATA)
  - 템플릿 기반 알림톡 발송
  - 필수: To, Kakao Channel, Kakao Template
  - 선택: Template Variables(JSON), From(문자 대체발신), Country Code
  - 동적 옵션: Kakao Channel, Kakao Template

- Send Kakao FriendTalk (CTA)
  - 카카오 친구톡 발송(채널 친구 대상)
  - 필수: To, Kakao Channel, Text
  - 선택: AD Flag, CTA Image ID, Buttons(JSON Array), From(문자 대체발신), Country Code
  - 동적 옵션: Kakao Channel, Kakao Image

- On Message Report (Single)
  - 단건 메시지 결과 웹훅 트리거(SINGLE-REPORT)
  - 워크플로우 활성화 시 Solapi Outgoing Webhook 자동 등록/해지

- On Group Report
  - 메시지 그룹 결과 웹훅 트리거(GROUP-REPORT)
  - 워크플로우 활성화 시 Solapi Outgoing Webhook 자동 등록/해지

- On Commerce Action
  - 커머스 액션 트리거(결제완료 등)
  - 필수: Commerce Hook (Solapi 콘솔에서 미리 생성)
  - 워크플로우 활성화 시 선택한 Hook에 웹훅 연결/해지

## 필드 설명 요약
- To: 콤마/줄바꿈으로 여러 번호 입력 가능. 국가코드는 Country Code로 설정(기본 82)
- From: Solapi에 등록된 발신번호만 사용 가능(동적 옵션)
- Image ID: Solapi Storage에 업로드된 파일의 fileId(동적 옵션)
- Kakao Channel: Solapi에 등록된 PFID(동적 옵션)
- Kakao Template: 선택한 채널에서 발송 가능한 템플릿(동적 옵션)
- Template Variables(JSON): 템플릿 변수 맵. 예) `{ "name": "홍길동" }`
- Buttons(JSON Array): 친구톡 버튼 배열. 예)
```
[
  { "buttonName": "홈", "buttonType": "WL", "linkMo": "https://example.com" }
]
```

## 권한(Scopes)
- 기본 제공 스코프로 대부분의 기능 동작
- 최소 필요 스코프 예시
  - 메시지 발송: `message:write`
  - 발신번호 조회: `senderid:read`
  - 스토리지 조회: `storage:read`
  - 카카오: `kakao:read kakao:write`
  - 웹훅: `webhook:read webhook:write`
  - 커머스: `commerce:read commerce:write`

## 트러블슈팅
- 401/403 인증 오류
  - 크리덴셜 연결 상태 확인 및 재인증
  - Solapi 앱의 Redirect URI에 n8n 크리덴셜 리다이렉트 URL 등록 여부 확인
- 템플릿/채널 목록 비어있음
  - Solapi 콘솔에서 채널/PFID 및 템플릿 등록 상태 확인
  - 해당 채널에 발송 가능한 템플릿인지 확인
- 문자 대체발신 미동작
  - `From(문자 대체발신)`을 비워두면 대체발송 비활성화됨. 등록된 발신번호 선택 필요
- 웹훅 미수신
  - 워크플로우 활성화 상태 확인
  - 방화벽/외부 접근 가능한 n8n 호스트인지 확인
  - Solapi 콘솔의 Outgoing Webhook 목록에 등록 여부 확인

## 라이선스
MIT
