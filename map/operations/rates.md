<!-- Generated file — do not edit; regenerated with the SDK. -->

# Rates — operations

Accessor: `client.rates` · Source: `adyen/apis/rates.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.rates.post_rates_calculate

- **Route**: `POST /rates/calculate`
- **Server**: `default7`
- **Signature**: `def post_rates_calculate(body: CalculateRateRequest | CalculateRateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CalculateRateResponse`
- **Returns (raw)**: `ApiResult[CalculateRateResponse, PostRatesCalculateErrorBody]`
- **Error**: `PostRatesCalculateErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CalculateRateRequest` | `adyen/models/calculate_rate_request.py` |
| `CalculateRateRequestDict` | `adyen/models/calculate_rate_request.py` |
| `CalculateRateResponse` | `adyen/models/calculate_rate_response.py` |
| `PostRatesCalculateErrorBody` | `adyen/errors/post_rates_calculate_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

