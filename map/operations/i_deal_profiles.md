<!-- Generated file — do not edit; regenerated with the SDK. -->

# IDealProfiles — operations

Accessor: `client.i_deal_profiles` · Source: `adyen/apis/i_deal_profiles.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.i_deal_profiles.post_ideal_profile_auth_link

- **Route**: `POST /ideal/profile/auth-link`
- **Server**: `default20`
- **Signature**: `def post_ideal_profile_auth_link(body: IdealAuthLinkRequest | IdealAuthLinkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdealAuthLinkResponse`
- **Returns (raw)**: `ApiResult[IdealAuthLinkResponse, PostIdealProfileAuthLinkErrorBody]`
- **Error**: `PostIdealProfileAuthLinkErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IdealAuthLinkRequest` | `adyen/models/ideal_auth_link_request.py` |
| `IdealAuthLinkRequestDict` | `adyen/models/ideal_auth_link_request.py` |
| `IdealAuthLinkResponse` | `adyen/models/ideal_auth_link_response.py` |
| `PostIdealProfileAuthLinkErrorBody` | `adyen/errors/post_ideal_profile_auth_link_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.i_deal_profiles.post_ideal_profile_authenticate

- **Route**: `POST /ideal/profile/authenticate`
- **Server**: `default20`
- **Signature**: `def post_ideal_profile_authenticate(body: IdealAuthenticateRequest | IdealAuthenticateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdealAuthenticateResponse`
- **Returns (raw)**: `ApiResult[IdealAuthenticateResponse, PostIdealProfileAuthenticateErrorBody]`
- **Error**: `PostIdealProfileAuthenticateErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IdealAuthenticateRequest` | `adyen/models/ideal_authenticate_request.py` |
| `IdealAuthenticateRequestDict` | `adyen/models/ideal_authenticate_request.py` |
| `IdealAuthenticateResponse` | `adyen/models/ideal_authenticate_response.py` |
| `PostIdealProfileAuthenticateErrorBody` | `adyen/errors/post_ideal_profile_authenticate_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.i_deal_profiles.post_ideal_profile_register

- **Route**: `POST /ideal/profile/register`
- **Server**: `default20`
- **Signature**: `def post_ideal_profile_register(body: ProfileRegistrationRequest | ProfileRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProfileRegistrationResponse`
- **Returns (raw)**: `ApiResult[ProfileRegistrationResponse, PostIdealProfileRegisterErrorBody]`
- **Error**: `PostIdealProfileRegisterErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileRegistrationRequest` | `adyen/models/profile_registration_request.py` |
| `ProfileRegistrationRequestDict` | `adyen/models/profile_registration_request.py` |
| `ProfileRegistrationResponse` | `adyen/models/profile_registration_response.py` |
| `PostIdealProfileRegisterErrorBody` | `adyen/errors/post_ideal_profile_register_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

