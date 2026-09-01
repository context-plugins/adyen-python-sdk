<!-- Generated file — do not edit; regenerated with the SDK. -->

# InstantPayouts — operations

Accessor: `client.instant_payouts` · Source: `adyen/apis/instant_payouts.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.instant_payouts.post_payout

- **Route**: `POST /payout`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_payout(*, body: PayoutRequest | PayoutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PayoutResponse`
- **Returns (raw)**: `ApiResult[PayoutResponse, PostPayoutErrorBody]`
- **Error**: `PostPayoutErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutRequest` | `adyen/models/payout_request.py` |
| `PayoutRequestDict` | `adyen/models/payout_request.py` |
| `PayoutResponse` | `adyen/models/payout_response.py` |
| `PostPayoutErrorBody` | `adyen/errors/post_payout_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

