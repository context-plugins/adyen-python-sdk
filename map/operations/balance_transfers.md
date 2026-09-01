<!-- Generated file — do not edit; regenerated with the SDK. -->

# BalanceTransfers — operations

Accessor: `client.balance_transfers` · Source: `adyen/apis/balance_transfers.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.balance_transfers.post_balance_transfers

- **Route**: `POST /balanceTransfers`
- **Server**: `default11`
- **Signature**: `def post_balance_transfers(body: BalanceTransferRequest | BalanceTransferRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BalanceTransferResponse`
- **Returns (raw)**: `ApiResult[BalanceTransferResponse, PostBalanceTransfersErrorBody]`
- **Error**: `PostBalanceTransfersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceTransferRequest` | `adyen/models/balance_transfer_request.py` |
| `BalanceTransferRequestDict` | `adyen/models/balance_transfer_request.py` |
| `BalanceTransferResponse` | `adyen/models/balance_transfer_response.py` |
| `PostBalanceTransfersErrorBody` | `adyen/errors/post_balance_transfers_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

