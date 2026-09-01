<!-- Generated file — do not edit; regenerated with the SDK. -->

# HostedOnboardingPage — operations

Accessor: `client.hosted_onboarding_page` · Source: `adyen/apis/hosted_onboarding_page.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.hosted_onboarding_page.post_get_onboarding_url

- **Route**: `POST /getOnboardingUrl`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default19`
- **Signature**: `def post_get_onboarding_url(*, body: GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetOnboardingUrlResponse`
- **Returns (raw)**: `ApiResult[GetOnboardingUrlResponse, PostGetOnboardingUrlErrorBody]`
- **Error**: `PostGetOnboardingUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOnboardingUrlRequest` | `adyen/models/get_onboarding_url_request.py` |
| `GetOnboardingUrlRequestDict` | `adyen/models/get_onboarding_url_request.py` |
| `GetOnboardingUrlResponse` | `adyen/models/get_onboarding_url_response.py` |
| `PostGetOnboardingUrlErrorBody` | `adyen/errors/post_get_onboarding_url_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

