<!-- Generated file — do not edit; regenerated with the SDK. -->

# Utility — operations

Accessor: `client.utility` · Source: `adyen/apis/utility.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.utility.post_apple_pay_sessions

- **Route**: `POST /applePay/sessions`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_apple_pay_sessions(*, idempotency_key: str | None = None, body: ApplePaySessionRequest | ApplePaySessionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `ApplePaySessionResponse`
- **Returns (raw)**: `ApiResult[ApplePaySessionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApplePaySessionRequest` | `adyen/models/apple_pay_session_request.py` |
| `ApplePaySessionRequestDict` | `adyen/models/apple_pay_session_request.py` |
| `ApplePaySessionResponse` | `adyen/models/apple_pay_session_response.py` |

### client.utility.post_origin_keys

- **Route**: `POST /originKeys`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_origin_keys(*, idempotency_key: str | None = None, body: UtilityRequest | UtilityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `UtilityResponse`
- **Returns (raw)**: `ApiResult[UtilityResponse, PostOriginKeysErrorBody]`
- **Error**: `PostOriginKeysErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UtilityRequest` | `adyen/models/utility_request.py` |
| `UtilityRequestDict` | `adyen/models/utility_request.py` |
| `UtilityResponse` | `adyen/models/utility_response.py` |
| `PostOriginKeysErrorBody` | `adyen/errors/post_origin_keys_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.utility.post_paypal_update_order

- **Route**: `POST /paypal/updateOrder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_paypal_update_order(*, idempotency_key: str | None = None, body: PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaypalUpdateOrderResponse`
- **Returns (raw)**: `ApiResult[PaypalUpdateOrderResponse, PostPaypalUpdateOrderErrorBody]`
- **Error**: `PostPaypalUpdateOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaypalUpdateOrderRequest` | `adyen/models/paypal_update_order_request.py` |
| `PaypalUpdateOrderRequestDict` | `adyen/models/paypal_update_order_request.py` |
| `PaypalUpdateOrderResponse` | `adyen/models/paypal_update_order_response.py` |
| `PostPaypalUpdateOrderErrorBody` | `adyen/errors/post_paypal_update_order_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.utility.post_validate_shopper_id

- **Route**: `POST /validateShopperId`
- **Server**: `default`
- **Signature**: `def post_validate_shopper_id(body: ValidateShopperIdRequest | ValidateShopperIdRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ValidateShopperIdResponse`
- **Returns (raw)**: `ApiResult[ValidateShopperIdResponse, PostValidateShopperIdErrorBody]`
- **Error**: `PostValidateShopperIdErrorBody` — **Case A (typed)**
- **Error arms**: `CheckoutErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ValidateShopperIdRequest` | `adyen/models/validate_shopper_id_request.py` |
| `ValidateShopperIdRequestDict` | `adyen/models/validate_shopper_id_request.py` |
| `ValidateShopperIdResponse` | `adyen/models/validate_shopper_id_response.py` |
| `PostValidateShopperIdErrorBody` | `adyen/errors/post_validate_shopper_id_error.py` |
| `CheckoutErrorResponseEntity` | `adyen/models/checkout_error_response_entity.py` |

