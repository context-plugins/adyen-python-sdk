<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountVerification — operations

Accessor: `client.account_verification` · Source: `adyen/apis/account_verification.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_verification.get_account_verification_reports_code

- **Route**: `GET /accountVerification/reports/{code}`
- **Server**: `default21`
- **Signature**: `def get_account_verification_reports_code(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — path
- **Returns (parsed)**: `AccountVerificationReportResponse`
- **Returns (raw)**: `ApiResult[AccountVerificationReportResponse, GetAccountVerificationReportsCodeErrorBody]`
- **Error**: `GetAccountVerificationReportsCodeErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 404, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountVerificationReportResponse` | `adyen/models/account_verification_report_response.py` |
| `GetAccountVerificationReportsCodeErrorBody` | `adyen/errors/get_account_verification_reports_code_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.account_verification.post_account_verification_routes

- **Route**: `POST /accountVerification/routes`
- **Server**: `default21`
- **Signature**: `def post_account_verification_routes(body: AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountVerificationRoutesResponse`
- **Returns (raw)**: `ApiResult[AccountVerificationRoutesResponse, PostAccountVerificationRoutesErrorBody]`
- **Error**: `PostAccountVerificationRoutesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountVerificationRoutesRequest` | `adyen/models/account_verification_routes_request.py` |
| `AccountVerificationRoutesRequestDict` | `adyen/models/account_verification_routes_request.py` |
| `AccountVerificationRoutesResponse` | `adyen/models/account_verification_routes_response.py` |
| `PostAccountVerificationRoutesErrorBody` | `adyen/errors/post_account_verification_routes_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

