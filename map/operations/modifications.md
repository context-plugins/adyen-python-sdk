<!-- Generated file — do not edit; regenerated with the SDK. -->

# Modifications — operations

Accessor: `client.modifications` · Source: `adyen/apis/modifications.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.modifications.post_adjust_authorisation

- **Route**: `POST /adjustAuthorisation`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_adjust_authorisation(*, body: AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostAdjustAuthorisationErrorBody]`
- **Error**: `PostAdjustAuthorisationErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AdjustAuthorisationRequest` | `adyen/models/adjust_authorisation_request.py` |
| `AdjustAuthorisationRequestDict` | `adyen/models/adjust_authorisation_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostAdjustAuthorisationErrorBody` | `adyen/errors/post_adjust_authorisation_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_cancel

- **Route**: `POST /cancel`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_cancel(*, body: CancelRequest | CancelRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostCancelErrorBody]`
- **Error**: `PostCancelErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelRequest` | `adyen/models/cancel_request.py` |
| `CancelRequestDict` | `adyen/models/cancel_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostCancelErrorBody` | `adyen/errors/post_cancel_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_cancel_or_refund

- **Route**: `POST /cancelOrRefund`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_cancel_or_refund(*, body: CancelOrRefundRequest | CancelOrRefundRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostCancelOrRefundErrorBody]`
- **Error**: `PostCancelOrRefundErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelOrRefundRequest` | `adyen/models/cancel_or_refund_request.py` |
| `CancelOrRefundRequestDict` | `adyen/models/cancel_or_refund_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostCancelOrRefundErrorBody` | `adyen/errors/post_cancel_or_refund_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_cancels

- **Route**: `POST /cancels`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_cancels(*, idempotency_key: str | None = None, body: StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `StandalonePaymentCancelResponse`
- **Returns (raw)**: `ApiResult[StandalonePaymentCancelResponse, PostCancelsErrorBody]`
- **Error**: `PostCancelsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StandalonePaymentCancelRequest` | `adyen/models/standalone_payment_cancel_request.py` |
| `StandalonePaymentCancelRequestDict` | `adyen/models/standalone_payment_cancel_request.py` |
| `StandalonePaymentCancelResponse` | `adyen/models/standalone_payment_cancel_response.py` |
| `PostCancelsErrorBody` | `adyen/errors/post_cancels_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_capture

- **Route**: `POST /capture`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_capture(*, body: CaptureRequest | CaptureRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostCaptureErrorBody]`
- **Error**: `PostCaptureErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CaptureRequest` | `adyen/models/capture_request.py` |
| `CaptureRequestDict` | `adyen/models/capture_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostCaptureErrorBody` | `adyen/errors/post_capture_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_donate

- **Route**: `POST /donate`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_donate(*, body: DonationRequest | DonationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostDonateErrorBody]`
- **Error**: `PostDonateErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DonationRequest` | `adyen/models/donation_request.py` |
| `DonationRequestDict` | `adyen/models/donation_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostDonateErrorBody` | `adyen/errors/post_donate_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_payments_payment_psp_reference_amount_updates

- **Route**: `POST /payments/{paymentPspReference}/amountUpdates`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_payment_psp_reference_amount_updates(payment_psp_reference: str, *, idempotency_key: str | None = None, body: PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_psp_reference`
- **Params**: `payment_psp_reference` — path `paymentPspReference` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentAmountUpdateResponse`
- **Returns (raw)**: `ApiResult[PaymentAmountUpdateResponse, PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody]`
- **Error**: `PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentAmountUpdateRequest` | `adyen/models/payment_amount_update_request.py` |
| `PaymentAmountUpdateRequestDict` | `adyen/models/payment_amount_update_request.py` |
| `PaymentAmountUpdateResponse` | `adyen/models/payment_amount_update_response.py` |
| `PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody` | `adyen/errors/post_payments_payment_psp_reference_amount_updates_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_payments_payment_psp_reference_cancels

- **Route**: `POST /payments/{paymentPspReference}/cancels`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_payment_psp_reference_cancels(payment_psp_reference: str, *, idempotency_key: str | None = None, body: PaymentCancelRequest | PaymentCancelRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_psp_reference`
- **Params**: `payment_psp_reference` — path `paymentPspReference` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentCancelResponse`
- **Returns (raw)**: `ApiResult[PaymentCancelResponse, PostPaymentsPaymentPspReferenceCancelsErrorBody]`
- **Error**: `PostPaymentsPaymentPspReferenceCancelsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentCancelRequest` | `adyen/models/payment_cancel_request.py` |
| `PaymentCancelRequestDict` | `adyen/models/payment_cancel_request.py` |
| `PaymentCancelResponse` | `adyen/models/payment_cancel_response.py` |
| `PostPaymentsPaymentPspReferenceCancelsErrorBody` | `adyen/errors/post_payments_payment_psp_reference_cancels_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_payments_payment_psp_reference_captures

- **Route**: `POST /payments/{paymentPspReference}/captures`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_payment_psp_reference_captures(payment_psp_reference: str, *, idempotency_key: str | None = None, body: PaymentCaptureRequest | PaymentCaptureRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_psp_reference`
- **Params**: `payment_psp_reference` — path `paymentPspReference` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentCaptureResponse`
- **Returns (raw)**: `ApiResult[PaymentCaptureResponse, PostPaymentsPaymentPspReferenceCapturesErrorBody]`
- **Error**: `PostPaymentsPaymentPspReferenceCapturesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentCaptureRequest` | `adyen/models/payment_capture_request.py` |
| `PaymentCaptureRequestDict` | `adyen/models/payment_capture_request.py` |
| `PaymentCaptureResponse` | `adyen/models/payment_capture_response.py` |
| `PostPaymentsPaymentPspReferenceCapturesErrorBody` | `adyen/errors/post_payments_payment_psp_reference_captures_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_payments_payment_psp_reference_refunds

- **Route**: `POST /payments/{paymentPspReference}/refunds`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_payment_psp_reference_refunds(payment_psp_reference: str, *, idempotency_key: str | None = None, body: PaymentRefundRequest | PaymentRefundRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_psp_reference`
- **Params**: `payment_psp_reference` — path `paymentPspReference` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentRefundResponse`
- **Returns (raw)**: `ApiResult[PaymentRefundResponse, PostPaymentsPaymentPspReferenceRefundsErrorBody]`
- **Error**: `PostPaymentsPaymentPspReferenceRefundsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentRefundRequest` | `adyen/models/payment_refund_request.py` |
| `PaymentRefundRequestDict` | `adyen/models/payment_refund_request.py` |
| `PaymentRefundResponse` | `adyen/models/payment_refund_response.py` |
| `PostPaymentsPaymentPspReferenceRefundsErrorBody` | `adyen/errors/post_payments_payment_psp_reference_refunds_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_payments_payment_psp_reference_reversals

- **Route**: `POST /payments/{paymentPspReference}/reversals`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default`
- **Signature**: `def post_payments_payment_psp_reference_reversals(payment_psp_reference: str, *, idempotency_key: str | None = None, body: PaymentReversalRequest | PaymentReversalRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_psp_reference`
- **Params**: `payment_psp_reference` — path `paymentPspReference` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `PaymentReversalResponse`
- **Returns (raw)**: `ApiResult[PaymentReversalResponse, PostPaymentsPaymentPspReferenceReversalsErrorBody]`
- **Error**: `PostPaymentsPaymentPspReferenceReversalsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentReversalRequest` | `adyen/models/payment_reversal_request.py` |
| `PaymentReversalRequestDict` | `adyen/models/payment_reversal_request.py` |
| `PaymentReversalResponse` | `adyen/models/payment_reversal_response.py` |
| `PostPaymentsPaymentPspReferenceReversalsErrorBody` | `adyen/errors/post_payments_payment_psp_reference_reversals_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_refund

- **Route**: `POST /refund`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_refund(*, body: RefundRequest | RefundRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostRefundErrorBody]`
- **Error**: `PostRefundErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RefundRequest` | `adyen/models/refund_request.py` |
| `RefundRequestDict` | `adyen/models/refund_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostRefundErrorBody` | `adyen/errors/post_refund_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_technical_cancel

- **Route**: `POST /technicalCancel`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_technical_cancel(*, body: TechnicalCancelRequest | TechnicalCancelRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostTechnicalCancelErrorBody]`
- **Error**: `PostTechnicalCancelErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TechnicalCancelRequest` | `adyen/models/technical_cancel_request.py` |
| `TechnicalCancelRequestDict` | `adyen/models/technical_cancel_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostTechnicalCancelErrorBody` | `adyen/errors/post_technical_cancel_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.modifications.post_void_pending_refund

- **Route**: `POST /voidPendingRefund`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default1`
- **Signature**: `def post_void_pending_refund(*, body: VoidPendingRefundRequest | VoidPendingRefundRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ModificationResult`
- **Returns (raw)**: `ApiResult[ModificationResult, PostVoidPendingRefundErrorBody]`
- **Error**: `PostVoidPendingRefundErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VoidPendingRefundRequest` | `adyen/models/void_pending_refund_request.py` |
| `VoidPendingRefundRequestDict` | `adyen/models/void_pending_refund_request.py` |
| `ModificationResult` | `adyen/models/modification_result.py` |
| `PostVoidPendingRefundErrorBody` | `adyen/errors/post_void_pending_refund_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

