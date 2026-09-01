<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reviewing — operations

Accessor: `client.reviewing` · Source: `adyen/apis/reviewing.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reviewing.post_confirm_third_party

- **Route**: `POST /confirmThirdParty`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_confirm_third_party(*, body: ModifyRequest | ModifyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModifyResponse`
- **Returns (raw)**: `ApiResult[ModifyResponse, PostConfirmThirdPartyErrorBody]`
- **Error**: `PostConfirmThirdPartyErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ModifyRequest` | `adyen/models/modify_request.py` |
| `ModifyRequestDict` | `adyen/models/modify_request.py` |
| `ModifyResponse` | `adyen/models/modify_response.py` |
| `PostConfirmThirdPartyErrorBody` | `adyen/errors/post_confirm_third_party_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.reviewing.post_decline_third_party

- **Route**: `POST /declineThirdParty`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_decline_third_party(*, body: ModifyRequest | ModifyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModifyResponse`
- **Returns (raw)**: `ApiResult[ModifyResponse, PostDeclineThirdPartyErrorBody]`
- **Error**: `PostDeclineThirdPartyErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ModifyRequest` | `adyen/models/modify_request.py` |
| `ModifyRequestDict` | `adyen/models/modify_request.py` |
| `ModifyResponse` | `adyen/models/modify_response.py` |
| `PostDeclineThirdPartyErrorBody` | `adyen/errors/post_decline_third_party_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

