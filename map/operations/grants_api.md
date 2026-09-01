<!-- Generated file — do not edit; regenerated with the SDK. -->

# GrantsApi — operations

Accessor: `client.grants_api` · Source: `adyen/apis/grants_api.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.grants_api.get_grants_grant_id

- **Route**: `GET /grants/{grantId}`
- **Server**: `default15`
- **Signature**: `def get_grants_grant_id(grant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_id`
- **Params**: `grant_id` — path `grantId`
- **Returns (parsed)**: `Grant`
- **Returns (raw)**: `ApiResult[Grant, GetGrantsGrantIdErrorBody]`
- **Error**: `GetGrantsGrantIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Grant` | `adyen/models/grant.py` |
| `GetGrantsGrantIdErrorBody` | `adyen/errors/get_grants_grant_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grants_api.get_grants_grant_id_disbursements

- **Route**: `GET /grants/{grantId}/disbursements`
- **Server**: `default15`
- **Signature**: `def get_grants_grant_id_disbursements(grant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_id`
- **Params**: `grant_id` — path `grantId`
- **Returns (parsed)**: `Disbursements`
- **Returns (raw)**: `ApiResult[Disbursements, GetGrantsGrantIdDisbursementsErrorBody]`
- **Error**: `GetGrantsGrantIdDisbursementsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Disbursements` | `adyen/models/disbursements.py` |
| `GetGrantsGrantIdDisbursementsErrorBody` | `adyen/errors/get_grants_grant_id_disbursements_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grants_api.get_grants_grant_id_disbursements_disbursement_id

- **Route**: `GET /grants/{grantId}/disbursements/{disbursementId}`
- **Server**: `default15`
- **Signature**: `def get_grants_grant_id_disbursements_disbursement_id(grant_id: str, disbursement_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_id`, `disbursement_id`
- **Params**: `grant_id` — path `grantId` · `disbursement_id` — path `disbursementId`
- **Returns (parsed)**: `Disbursement`
- **Returns (raw)**: `ApiResult[Disbursement, GetGrantsGrantIdDisbursementsDisbursementIdErrorBody]`
- **Error**: `GetGrantsGrantIdDisbursementsDisbursementIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Disbursement` | `adyen/models/disbursement.py` |
| `GetGrantsGrantIdDisbursementsDisbursementIdErrorBody` | `adyen/errors/get_grants_grant_id_disbursements_disbursement_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grants_api.get_grants2

- **Route**: `GET /grants`
- **Server**: `default15`
- **Signature**: `def get_grants2(counterparty_account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `counterparty_account_holder_id`
- **Params**: `counterparty_account_holder_id` — query `counterpartyAccountHolderId`
- **Returns (parsed)**: `Grants`
- **Returns (raw)**: `ApiResult[Grants, GetGrants2ErrorBody]`
- **Error**: `GetGrants2ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Grants` | `adyen/models/grants.py` |
| `GetGrants2ErrorBody` | `adyen/errors/get_grants2_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grants_api.patch_grants_grant_id_disbursements_disbursement_id

- **Route**: `PATCH /grants/{grantId}/disbursements/{disbursementId}`
- **Server**: `default15`
- **Signature**: `def patch_grants_grant_id_disbursements_disbursement_id(grant_id: str, disbursement_id: str, body: DisbursementInfoUpdate | DisbursementInfoUpdateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_id`, `disbursement_id`, `body`
- **Params**: `grant_id` — path `grantId` · `disbursement_id` — path `disbursementId` · `body` — JSON body
- **Returns (parsed)**: `Disbursement`
- **Returns (raw)**: `ApiResult[Disbursement, PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody]`
- **Error**: `PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisbursementInfoUpdate` | `adyen/models/disbursement_info_update.py` |
| `DisbursementInfoUpdateDict` | `adyen/models/disbursement_info_update.py` |
| `Disbursement` | `adyen/models/disbursement.py` |
| `PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody` | `adyen/errors/patch_grants_grant_id_disbursements_disbursement_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.grants_api.post_grants2

- **Route**: `POST /grants`
- **Server**: `default15`
- **Signature**: `def post_grants2(*, body: CapitalGrantInfo | CapitalGrantInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Grant`
- **Returns (raw)**: `ApiResult[Grant, PostGrants2ErrorBody]`
- **Error**: `PostGrants2ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CapitalGrantInfo` | `adyen/models/capital_grant_info.py` |
| `CapitalGrantInfoDict` | `adyen/models/capital_grant_info.py` |
| `Grant` | `adyen/models/grant.py` |
| `PostGrants2ErrorBody` | `adyen/errors/post_grants2_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

