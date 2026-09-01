<!-- Generated file — do not edit; regenerated with the SDK. -->

# CashOutApi — operations

Accessor: `client.cash_out_api` · Source: `adyen/apis/cash_out_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cash_out_api.post_cashouts

- **Route**: `POST /cashouts`
- **Server**: `default14`
- **Signature**: `def post_cashouts(body: CashOutInfo | CashOutInfoDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CashOut`
- **Returns (raw)**: `ApiResult[CashOut, PostCashoutsErrorBody]`
- **Error**: `PostCashoutsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CashOutInfo` | `adyen/models/cash_out_info.py` |
| `CashOutInfoDict` | `adyen/models/cash_out_info.py` |
| `CashOut` | `adyen/models/cash_out.py` |
| `PostCashoutsErrorBody` | `adyen/errors/post_cashouts_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

