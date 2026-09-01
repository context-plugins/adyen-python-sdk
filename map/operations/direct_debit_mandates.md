<!-- Generated file — do not edit; regenerated with the SDK. -->

# DirectDebitMandates — operations

Accessor: `client.direct_debit_mandates` · Source: `adyen/apis/direct_debit_mandates.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.direct_debit_mandates.get_mandates

- **Route**: `GET /mandates`
- **Server**: `default13`
- **Signature**: `def get_mandates(*, balance_account_id: str | None = None, payment_instrument_id: str | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `balance_account_id` — query `balanceAccountId` · `payment_instrument_id` — query `paymentInstrumentId` · `cursor` — query
- **Returns (parsed)**: `ListMandatesResponse`
- **Returns (raw)**: `ApiResult[ListMandatesResponse, GetMandatesErrorBody]`
- **Error**: `GetMandatesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMandatesResponse` | `adyen/models/list_mandates_response.py` |
| `GetMandatesErrorBody` | `adyen/errors/get_mandates_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.direct_debit_mandates.get_mandates_mandate_id

- **Route**: `GET /mandates/{mandateId}`
- **Server**: `default13`
- **Signature**: `def get_mandates_mandate_id(mandate_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `mandate_id`
- **Params**: `mandate_id` — path `mandateId`
- **Returns (parsed)**: `Mandate1`
- **Returns (raw)**: `ApiResult[Mandate1, GetMandatesMandateIdErrorBody]`
- **Error**: `GetMandatesMandateIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Mandate1` | `adyen/models/mandate1.py` |
| `GetMandatesMandateIdErrorBody` | `adyen/errors/get_mandates_mandate_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.direct_debit_mandates.patch_mandates_mandate_id

- **Route**: `PATCH /mandates/{mandateId}`
- **Server**: `default13`
- **Signature**: `def patch_mandates_mandate_id(mandate_id: str, body: MandateUpdate | MandateUpdateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `mandate_id`, `body`
- **Params**: `mandate_id` — path `mandateId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PatchMandatesMandateIdErrorBody]`
- **Error**: `PatchMandatesMandateIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MandateUpdate` | `adyen/models/mandate_update.py` |
| `MandateUpdateDict` | `adyen/models/mandate_update.py` |
| `PatchMandatesMandateIdErrorBody` | `adyen/errors/patch_mandates_mandate_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.direct_debit_mandates.post_mandates_mandate_id_cancel

- **Route**: `POST /mandates/{mandateId}/cancel`
- **Server**: `default13`
- **Signature**: `def post_mandates_mandate_id_cancel(mandate_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `mandate_id`
- **Params**: `mandate_id` — path `mandateId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostMandatesMandateIdCancelErrorBody]`
- **Error**: `PostMandatesMandateIdCancelErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostMandatesMandateIdCancelErrorBody` | `adyen/errors/post_mandates_mandate_id_cancel_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

