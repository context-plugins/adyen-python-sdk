<!-- Generated file — do not edit; regenerated with the SDK. -->

# Payments — operations

Accessor: `client.payments` · Source: `adyen/apis/payments.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payments.get_sessions_session_id

- **Route**: `GET /sessions/{sessionId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def get_sessions_session_id(session_id: str, session_result: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `session_id`, `session_result`
- **Params**: `session_id` — path `sessionId` · `session_result` — query `sessionResult`
- **Returns (parsed)**: `SessionResultResponse`
- **Returns (raw)**: `ApiResult[SessionResultResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SessionResultResponse` | `adyen/models/session_result_response.py` |

### client.payments.post_authorise

- **Route**: `POST /authorise`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_authorise(*, body: PaymentRequest1 | PaymentRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentResult`
- **Returns (raw)**: `ApiResult[PaymentResult, PostAuthoriseErrorBody]`
- **Error**: `PostAuthoriseErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentRequest1` | `adyen/models/payment_request1.py` |
| `PaymentRequest1Dict` | `adyen/models/payment_request1.py` |
| `PaymentResult` | `adyen/models/payment_result.py` |
| `PostAuthoriseErrorBody` | `adyen/errors/post_authorise_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_authorise3d

- **Route**: `POST /authorise3d`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_authorise3d(*, body: PaymentRequest3D | PaymentRequest3DDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentResult`
- **Returns (raw)**: `ApiResult[PaymentResult, PostAuthorise3DErrorBody]`
- **Error**: `PostAuthorise3DErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentRequest3D` | `adyen/models/payment_request3_d.py` |
| `PaymentRequest3DDict` | `adyen/models/payment_request3_d.py` |
| `PaymentResult` | `adyen/models/payment_result.py` |
| `PostAuthorise3DErrorBody` | `adyen/errors/post_authorise3_d_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_authorise3ds2

- **Route**: `POST /authorise3ds2`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_authorise3ds2(*, body: PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentResult`
- **Returns (raw)**: `ApiResult[PaymentResult, PostAuthorise3Ds2ErrorBody]`
- **Error**: `PostAuthorise3Ds2ErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentRequest3Ds2` | `adyen/models/payment_request3_ds2.py` |
| `PaymentRequest3Ds2Dict` | `adyen/models/payment_request3_ds2.py` |
| `PaymentResult` | `adyen/models/payment_result.py` |
| `PostAuthorise3Ds2ErrorBody` | `adyen/errors/post_authorise3_ds2_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_card_details

- **Route**: `POST /cardDetails`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_card_details(*, idempotency_key: str | None = None, body: CardDetailsRequest | CardDetailsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CardDetailsResponse`
- **Returns (raw)**: `ApiResult[CardDetailsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CardDetailsRequest` | `adyen/models/card_details_request.py` |
| `CardDetailsRequestDict` | `adyen/models/card_details_request.py` |
| `CardDetailsResponse` | `adyen/models/card_details_response.py` |

### client.payments.post_get_authentication_result

- **Route**: `POST /getAuthenticationResult`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_get_authentication_result(*, body: AuthenticationResultRequest | AuthenticationResultRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthenticationResultResponse`
- **Returns (raw)**: `ApiResult[AuthenticationResultResponse, PostGetAuthenticationResultErrorBody]`
- **Error**: `PostGetAuthenticationResultErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthenticationResultRequest` | `adyen/models/authentication_result_request.py` |
| `AuthenticationResultRequestDict` | `adyen/models/authentication_result_request.py` |
| `AuthenticationResultResponse` | `adyen/models/authentication_result_response.py` |
| `PostGetAuthenticationResultErrorBody` | `adyen/errors/post_get_authentication_result_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_payment_methods

- **Route**: `POST /paymentMethods`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payment_methods(*, idempotency_key: str | None = None, body: PaymentMethodsRequest | PaymentMethodsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentMethodsResponse`
- **Returns (raw)**: `ApiResult[PaymentMethodsResponse, PostPaymentMethodsErrorBody]`
- **Error**: `PostPaymentMethodsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentMethodsRequest` | `adyen/models/payment_methods_request.py` |
| `PaymentMethodsRequestDict` | `adyen/models/payment_methods_request.py` |
| `PaymentMethodsResponse` | `adyen/models/payment_methods_response.py` |
| `PostPaymentMethodsErrorBody` | `adyen/errors/post_payment_methods_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_payments

- **Route**: `POST /payments`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments(*, idempotency_key: str | None = None, body: PaymentRequest | PaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentResponse`
- **Returns (raw)**: `ApiResult[PaymentResponse, PostPaymentsErrorBody]`
- **Error**: `PostPaymentsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentRequest` | `adyen/models/payment_request.py` |
| `PaymentRequestDict` | `adyen/models/payment_request.py` |
| `PaymentResponse` | `adyen/models/payment_response.py` |
| `PostPaymentsErrorBody` | `adyen/errors/post_payments_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_payments_cancel

- **Route**: `POST /payments/cancel`
- **Server**: `default20`
- **Signature**: `def post_payments_cancel(body: CancelPaymentRequest | CancelPaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CancelPaymentResponse`
- **Returns (raw)**: `ApiResult[CancelPaymentResponse, PostPaymentsCancelErrorBody]`
- **Error**: `PostPaymentsCancelErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelPaymentRequest` | `adyen/models/cancel_payment_request.py` |
| `CancelPaymentRequestDict` | `adyen/models/cancel_payment_request.py` |
| `CancelPaymentResponse` | `adyen/models/cancel_payment_response.py` |
| `PostPaymentsCancelErrorBody` | `adyen/errors/post_payments_cancel_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments.post_payments_confirm

- **Route**: `POST /payments/confirm`
- **Server**: `default20`
- **Signature**: `def post_payments_confirm(body: ConfirmPaymentRequest | ConfirmPaymentRequestDict, *, www_authenticate: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `www_authenticate` — header `WWW-Authenticate` · `body` — JSON body
- **Returns (parsed)**: `ConfirmPaymentResponse`
- **Returns (raw)**: `ApiResult[ConfirmPaymentResponse, PostPaymentsConfirmErrorBody]`
- **Error**: `PostPaymentsConfirmErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmPaymentRequest` | `adyen/models/confirm_payment_request.py` |
| `ConfirmPaymentRequestDict` | `adyen/models/confirm_payment_request.py` |
| `ConfirmPaymentResponse` | `adyen/models/confirm_payment_response.py` |
| `PostPaymentsConfirmErrorBody` | `adyen/errors/post_payments_confirm_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments.post_payments_details

- **Route**: `POST /payments/details`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_details(*, idempotency_key: str | None = None, body: PaymentDetailsRequest | PaymentDetailsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentDetailsResponse`
- **Returns (raw)**: `ApiResult[PaymentDetailsResponse, PostPaymentsDetailsErrorBody]`
- **Error**: `PostPaymentsDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentDetailsRequest` | `adyen/models/payment_details_request.py` |
| `PaymentDetailsRequestDict` | `adyen/models/payment_details_request.py` |
| `PaymentDetailsResponse` | `adyen/models/payment_details_response.py` |
| `PostPaymentsDetailsErrorBody` | `adyen/errors/post_payments_details_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_payments_details1

- **Route**: `POST /payments/details`
- **Server**: `default20`
- **Signature**: `def post_payments_details1(body: IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentDetailsResponse1`
- **Returns (raw)**: `ApiResult[PaymentDetailsResponse1, PostPaymentsDetails1ErrorBody]`
- **Error**: `PostPaymentsDetails1ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IdealPaymentDetailsRequest` | `adyen/models/ideal_payment_details_request.py` |
| `IdealPaymentDetailsRequestDict` | `adyen/models/ideal_payment_details_request.py` |
| `PaymentDetailsResponse1` | `adyen/models/payment_details_response1.py` |
| `PostPaymentsDetails1ErrorBody` | `adyen/errors/post_payments_details1_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments.post_retrieve3ds2_result

- **Route**: `POST /retrieve3ds2Result`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_retrieve3ds2_result(*, body: ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ThreeDs2ResultResponse`
- **Returns (raw)**: `ApiResult[ThreeDs2ResultResponse, PostRetrieve3Ds2ResultErrorBody]`
- **Error**: `PostRetrieve3Ds2ResultErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ThreeDs2ResultRequest` | `adyen/models/three_ds2_result_request.py` |
| `ThreeDs2ResultRequestDict` | `adyen/models/three_ds2_result_request.py` |
| `ThreeDs2ResultResponse` | `adyen/models/three_ds2_result_response.py` |
| `PostRetrieve3Ds2ResultErrorBody` | `adyen/errors/post_retrieve3_ds2_result_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.payments.post_sessions

- **Route**: `POST /sessions`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_sessions(*, idempotency_key: str | None = None, body: CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CreateCheckoutSessionResponse`
- **Returns (raw)**: `ApiResult[CreateCheckoutSessionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCheckoutSessionRequest` | `adyen/models/create_checkout_session_request.py` |
| `CreateCheckoutSessionRequestDict` | `adyen/models/create_checkout_session_request.py` |
| `CreateCheckoutSessionResponse` | `adyen/models/create_checkout_session_response.py` |

