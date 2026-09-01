<!-- Generated file — do not edit; regenerated with the SDK. -->

# SessionAuthentication — operations

Accessor: `client.session_authentication` · Source: `adyen/apis/session_authentication.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.session_authentication.post_auth_certificate

- **Route**: `POST /auth/certificate`
- **Server**: `default25`
- **Signature**: `def post_auth_certificate(*, x_api_key: str | None = None, body: CertificateLoadingRequest | CertificateLoadingRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_api_key` — header `X-API-Key` · `body` — JSON body
- **Returns (parsed)**: `CertificateLoadingResponse`
- **Returns (raw)**: `ApiResult[CertificateLoadingResponse, PostAuthCertificateErrorBody]`
- **Error**: `PostAuthCertificateErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CertificateLoadingRequest` | `adyen/models/certificate_loading_request.py` |
| `CertificateLoadingRequestDict` | `adyen/models/certificate_loading_request.py` |
| `CertificateLoadingResponse` | `adyen/models/certificate_loading_response.py` |
| `PostAuthCertificateErrorBody` | `adyen/errors/post_auth_certificate_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.session_authentication.post_sessions2

- **Route**: `POST /sessions`
- **Server**: `default17`
- **Signature**: `def post_sessions2(body: AuthenticationSessionRequest | AuthenticationSessionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthenticationSessionResponse`
- **Returns (raw)**: `ApiResult[AuthenticationSessionResponse, PostSessions2ErrorBody]`
- **Error**: `PostSessions2ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthenticationSessionRequest` | `adyen/models/authentication_session_request.py` |
| `AuthenticationSessionRequestDict` | `adyen/models/authentication_session_request.py` |
| `AuthenticationSessionResponse` | `adyen/models/authentication_session_response.py` |
| `PostSessions2ErrorBody` | `adyen/errors/post_sessions2_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

