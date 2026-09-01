<!-- Generated file — do not edit; regenerated with the SDK. -->

# RecurringApi — operations

Accessor: `client.recurring_api` · Source: `adyen/apis/recurring_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.recurring_api.delete_stored_payment_methods_stored_payment_method_id

- **Route**: `DELETE /storedPaymentMethods/{storedPaymentMethodId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def delete_stored_payment_methods_stored_payment_method_id(stored_payment_method_id: str, shopper_reference: str, merchant_account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `stored_payment_method_id`, `shopper_reference`, `merchant_account`
- **Params**: `stored_payment_method_id` — path `storedPaymentMethodId` · `shopper_reference` — query `shopperReference` · `merchant_account` — query `merchantAccount`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.recurring_api.get_stored_payment_methods

- **Route**: `GET /storedPaymentMethods`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def get_stored_payment_methods(*, shopper_reference: str | None = None, merchant_account: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `shopper_reference` — query `shopperReference` · `merchant_account` — query `merchantAccount`
- **Returns (parsed)**: `ListStoredPaymentMethodsResponse`
- **Returns (raw)**: `ApiResult[ListStoredPaymentMethodsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListStoredPaymentMethodsResponse` | `adyen/models/list_stored_payment_methods_response.py` |

### client.recurring_api.post_forward

- **Route**: `POST /forward`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_forward(*, idempotency_key: str | None = None, body: CheckoutForwardRequest | CheckoutForwardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CheckoutForwardResponse`
- **Returns (raw)**: `ApiResult[CheckoutForwardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CheckoutForwardRequest` | `adyen/models/checkout_forward_request.py` |
| `CheckoutForwardRequestDict` | `adyen/models/checkout_forward_request.py` |
| `CheckoutForwardResponse` | `adyen/models/checkout_forward_response.py` |

### client.recurring_api.post_stored_payment_methods

- **Route**: `POST /storedPaymentMethods`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_stored_payment_methods(*, idempotency_key: str | None = None, body: StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `StoredPaymentMethodResource`
- **Returns (raw)**: `ApiResult[StoredPaymentMethodResource, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StoredPaymentMethodRequest` | `adyen/models/stored_payment_method_request.py` |
| `StoredPaymentMethodRequestDict` | `adyen/models/stored_payment_method_request.py` |
| `StoredPaymentMethodResource` | `adyen/models/stored_payment_method_resource.py` |

