<!-- Generated file — do not edit; regenerated with the SDK. -->

# Orders — operations

Accessor: `client.orders` · Source: `adyen/apis/orders.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.orders.post_orders

- **Route**: `POST /orders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_orders(*, idempotency_key: str | None = None, body: CreateOrderRequest | CreateOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CreateOrderResponse`
- **Returns (raw)**: `ApiResult[CreateOrderResponse, PostOrdersErrorBody]`
- **Error**: `PostOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateOrderRequest` | `adyen/models/create_order_request.py` |
| `CreateOrderRequestDict` | `adyen/models/create_order_request.py` |
| `CreateOrderResponse` | `adyen/models/create_order_response.py` |
| `PostOrdersErrorBody` | `adyen/errors/post_orders_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.orders.post_orders_cancel

- **Route**: `POST /orders/cancel`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_orders_cancel(*, idempotency_key: str | None = None, body: CancelOrderRequest | CancelOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CancelOrderResponse`
- **Returns (raw)**: `ApiResult[CancelOrderResponse, PostOrdersCancelErrorBody]`
- **Error**: `PostOrdersCancelErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelOrderRequest` | `adyen/models/cancel_order_request.py` |
| `CancelOrderRequestDict` | `adyen/models/cancel_order_request.py` |
| `CancelOrderResponse` | `adyen/models/cancel_order_response.py` |
| `PostOrdersCancelErrorBody` | `adyen/errors/post_orders_cancel_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.orders.post_payment_methods_balance

- **Route**: `POST /paymentMethods/balance`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payment_methods_balance(*, idempotency_key: str | None = None, body: BalanceCheckRequest | BalanceCheckRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `BalanceCheckResponse`
- **Returns (raw)**: `ApiResult[BalanceCheckResponse, PostPaymentMethodsBalanceErrorBody]`
- **Error**: `PostPaymentMethodsBalanceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceCheckRequest` | `adyen/models/balance_check_request.py` |
| `BalanceCheckRequestDict` | `adyen/models/balance_check_request.py` |
| `BalanceCheckResponse` | `adyen/models/balance_check_response.py` |
| `PostPaymentMethodsBalanceErrorBody` | `adyen/errors/post_payment_methods_balance_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

