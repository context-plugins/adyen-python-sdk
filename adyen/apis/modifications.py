from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.post_adjust_authorisation_error import (
    PostAdjustAuthorisationErrorBody,
    post_adjust_authorisation_error_mapper,
)
from ..errors.post_cancel_error import PostCancelErrorBody, post_cancel_error_mapper
from ..errors.post_cancel_or_refund_error import PostCancelOrRefundErrorBody, post_cancel_or_refund_error_mapper
from ..errors.post_cancels_error import PostCancelsErrorBody, post_cancels_error_mapper
from ..errors.post_capture_error import PostCaptureErrorBody, post_capture_error_mapper
from ..errors.post_donate_error import PostDonateErrorBody, post_donate_error_mapper
from ..errors.post_payments_payment_psp_reference_amount_updates_error import (
    PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody,
    post_payments_payment_psp_reference_amount_updates_error_mapper,
)
from ..errors.post_payments_payment_psp_reference_cancels_error import (
    PostPaymentsPaymentPspReferenceCancelsErrorBody,
    post_payments_payment_psp_reference_cancels_error_mapper,
)
from ..errors.post_payments_payment_psp_reference_captures_error import (
    PostPaymentsPaymentPspReferenceCapturesErrorBody,
    post_payments_payment_psp_reference_captures_error_mapper,
)
from ..errors.post_payments_payment_psp_reference_refunds_error import (
    PostPaymentsPaymentPspReferenceRefundsErrorBody,
    post_payments_payment_psp_reference_refunds_error_mapper,
)
from ..errors.post_payments_payment_psp_reference_reversals_error import (
    PostPaymentsPaymentPspReferenceReversalsErrorBody,
    post_payments_payment_psp_reference_reversals_error_mapper,
)
from ..errors.post_refund_error import PostRefundErrorBody, post_refund_error_mapper
from ..errors.post_technical_cancel_error import PostTechnicalCancelErrorBody, post_technical_cancel_error_mapper
from ..errors.post_void_pending_refund_error import (
    PostVoidPendingRefundErrorBody,
    post_void_pending_refund_error_mapper,
)
from ..models.adjust_authorisation_request import AdjustAuthorisationRequest, AdjustAuthorisationRequestDict
from ..models.cancel_or_refund_request import CancelOrRefundRequest, CancelOrRefundRequestDict
from ..models.cancel_request import CancelRequest, CancelRequestDict
from ..models.capture_request import CaptureRequest, CaptureRequestDict
from ..models.donation_request import DonationRequest, DonationRequestDict
from ..models.modification_result import ModificationResult
from ..models.payment_amount_update_request import PaymentAmountUpdateRequest, PaymentAmountUpdateRequestDict
from ..models.payment_amount_update_response import PaymentAmountUpdateResponse
from ..models.payment_cancel_request import PaymentCancelRequest, PaymentCancelRequestDict
from ..models.payment_cancel_response import PaymentCancelResponse
from ..models.payment_capture_request import PaymentCaptureRequest, PaymentCaptureRequestDict
from ..models.payment_capture_response import PaymentCaptureResponse
from ..models.payment_refund_request import PaymentRefundRequest, PaymentRefundRequestDict
from ..models.payment_refund_response import PaymentRefundResponse
from ..models.payment_reversal_request import PaymentReversalRequest, PaymentReversalRequestDict
from ..models.payment_reversal_response import PaymentReversalResponse
from ..models.refund_request import RefundRequest, RefundRequestDict
from ..models.standalone_payment_cancel_request import (
    StandalonePaymentCancelRequest,
    StandalonePaymentCancelRequestDict,
)
from ..models.standalone_payment_cancel_response import StandalonePaymentCancelResponse
from ..models.technical_cancel_request import TechnicalCancelRequest, TechnicalCancelRequestDict
from ..models.void_pending_refund_request import VoidPendingRefundRequest, VoidPendingRefundRequestDict
from ..server.server import Server


class Modifications:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ModificationsWithRawResponse(client, server, auth)

    def post_adjust_authorisation(
        self,
        *,
        body: AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Allows you to increase or decrease the authorised amount after the initial authorisation has taken place.
        This functionality enables for example tipping, improving the chances your authorisation will be valid, or
        charging the shopper when they have already left the merchant premises.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/amountUpdates)
            endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_adjust_authorisation(body=body, request_options=request_options).unwrap()

    def post_cancel(
        self,
        *,
        body: CancelRequest | CancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel
        payments after authorisation only for payment methods that support distinct authorisations and captures.

        For more information, refer to `Cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/cancels) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_cancel(body=body, request_options=request_options).unwrap()

    def post_cancel_or_refund(
        self,
        *,
        body: CancelOrRefundRequest | CancelOrRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is
        useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).

        Do not use this endpoint for payments that involve:
         * `Multiple partial captures <https://docs.adyen.com/online-payments/capture>`__.
         * `Split data <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__
                either at time of payment or capture for Adyen for Platforms.

         Instead, check if the payment has been captured and make a corresponding
            https://docs.adyen.com/api-explorer/#/Payment/refund or https://docs.adyen.com/api-explorer/#/Payment/cancel
            call.

        For more information, refer to `Cancel or refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/reversals) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_cancel_or_refund(body=body, request_options=request_options).unwrap()

    def post_cancels(
        self,
        *,
        idempotency_key: str | None = None,
        body: StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StandalonePaymentCancelResponse:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**TECHNICAL_CANCEL** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment using the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels
        endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_cancels(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_capture(
        self,
        *,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full
        authorisation amount is captured, however it's also possible to capture a smaller amount, which results in
        cancelling the remaining authorisation balance.

        Payment methods that are captured automatically after authorisation don't need to be captured. However,
        submitting a capture request on these transactions will not result in double charges. If immediate or delayed
        auto-capture is enabled, calling the capture method is not necessary.

        For more information refer to `Capture
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/captures) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_capture(body=body, request_options=request_options).unwrap()

    def post_donate(
        self,
        *,
        body: DonationRequest | DonationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Schedules a new payment to be created (including a new authorisation request) for the specified donation
        using the payment details of the original payment.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/donations endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_donate(body=body, request_options=request_options).unwrap()

    def post_payments_payment_psp_reference_amount_updates(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAmountUpdateResponse:
        """Increases or decreases the authorised payment amount and returns a unique reference for this request. You get
        the outcome of the request asynchronously, in an `**AUTHORISATION_ADJUSTMENT** webhook
        <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__.

        You can only update authorised amounts that have not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__.

        The amount you specify in the request is the updated amount, which is larger or smaller than the initial
        authorised amount.

        For more information, refer to `Authorisation adjustment
        <https://docs.adyen.com/online-payments/adjust-authorisation#use-cases>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payments_payment_psp_reference_amount_updates(
            payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_payments_payment_psp_reference_cancels(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCancelRequest | PaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentCancelResponse:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**CANCELLATION** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment but don't have the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to cancel.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payments_payment_psp_reference_cancels(
            payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_payments_payment_psp_reference_captures(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCaptureRequest | PaymentCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentCaptureResponse:
        """Captures an authorised payment and returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CAPTURE** webhook
        <https://docs.adyen.com/online-payments/capture#capture-notification>`__.

        You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed
        amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on
        your account and the payment method supports multiple partial captures.

        `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__ is the default setting
        for most payment methods. In these cases, you don't need to make capture requests. However, making capture
        requests for payments that are captured automatically does not result in double charges.

        For more information, refer to `Capture <https://docs.adyen.com/online-payments/capture>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to capture.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payments_payment_psp_reference_captures(
            payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_payments_payment_psp_reference_refunds(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentRefundRequest | PaymentRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentRefundResponse:
        """Refunds a payment that has been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**REFUND** webhook <https://docs.adyen.com/online-payments/refund#refund-webhook>`__.

        You can refund either the full captured amount or a part of the captured amount. You can also perform multiple
        partial refunds, as long as their sum doesn't exceed the captured amount.

        > Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds,
            refer to the payment method page such as `cards
            <https://docs.adyen.com/payment-methods/cards#supported-cards>`__, `iDEAL
            <https://docs.adyen.com/payment-methods/ideal>`__, or `Klarna
            <https://docs.adyen.com/payment-methods/klarna>`__.

        If you want to refund a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Refund <https://docs.adyen.com/online-payments/refund>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to refund.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payments_payment_psp_reference_refunds(
            payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_payments_payment_psp_reference_reversals(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentReversalRequest | PaymentReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentReversalResponse:
        """`Refunds
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds>`__ a
        payment if it has already been captured, and `cancels
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels>`__ a
        payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CANCEL_OR_REFUND** webhook
        <https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook>`__.

        The reversed amount is always the full payment amount.
        > Do not use this request for payments that involve multiple partial captures.

        For more information, refer to `Reversal <https://docs.adyen.com/online-payments/reversal>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to reverse.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payments_payment_psp_reference_reversals(
            payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_refund(
        self,
        *,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding
        can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long
        as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot
        be refunded, use the /cancel method instead.

        Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be
        configured to cover shipping/handling costs.

        For more information, refer to `Refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/refunds) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_refund(body=body, request_options=request_options).unwrap()

    def post_technical_cancel(
        self,
        *,
        body: TechnicalCancelRequest | TechnicalCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment
        request available.

        In your call, refer to the original payment by using the ``reference`` that you specified in your payment
        request.

        For more information, see `Technical cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_technical_cancel(body=body, request_options=request_options).unwrap()

    def post_void_pending_refund(
        self,
        *,
        body: VoidPendingRefundRequest | VoidPendingRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """This endpoint allows you to cancel an unreferenced refund request before it has been completed.

        In your call, you can refer to the original refund request either by using the ``tenderReference``, or the
        ``pspReference``. We recommend implementing based on the ``tenderReference``, as this is generated for both
        offline and online transactions.

        For more information, refer to `Cancel an unreferenced refund
        <https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_void_pending_refund(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ModificationsWithRawResponse:
        return self._with_raw_response


class AsyncModifications:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncModificationsWithRawResponse(client, server, auth)

    async def post_adjust_authorisation(
        self,
        *,
        body: AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Allows you to increase or decrease the authorised amount after the initial authorisation has taken place.
        This functionality enables for example tipping, improving the chances your authorisation will be valid, or
        charging the shopper when they have already left the merchant premises.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/amountUpdates)
            endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_adjust_authorisation(body=body, request_options=request_options)
        ).unwrap()

    async def post_cancel(
        self,
        *,
        body: CancelRequest | CancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel
        payments after authorisation only for payment methods that support distinct authorisations and captures.

        For more information, refer to `Cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/cancels) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (await self._with_raw_response.post_cancel(body=body, request_options=request_options)).unwrap()

    async def post_cancel_or_refund(
        self,
        *,
        body: CancelOrRefundRequest | CancelOrRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is
        useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).

        Do not use this endpoint for payments that involve:
         * `Multiple partial captures <https://docs.adyen.com/online-payments/capture>`__.
         * `Split data <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__
                either at time of payment or capture for Adyen for Platforms.

         Instead, check if the payment has been captured and make a corresponding
            https://docs.adyen.com/api-explorer/#/Payment/refund or https://docs.adyen.com/api-explorer/#/Payment/cancel
            call.

        For more information, refer to `Cancel or refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/reversals) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_cancel_or_refund(body=body, request_options=request_options)
        ).unwrap()

    async def post_cancels(
        self,
        *,
        idempotency_key: str | None = None,
        body: StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StandalonePaymentCancelResponse:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**TECHNICAL_CANCEL** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment using the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels
        endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_cancels(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_capture(
        self,
        *,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full
        authorisation amount is captured, however it's also possible to capture a smaller amount, which results in
        cancelling the remaining authorisation balance.

        Payment methods that are captured automatically after authorisation don't need to be captured. However,
        submitting a capture request on these transactions will not result in double charges. If immediate or delayed
        auto-capture is enabled, calling the capture method is not necessary.

        For more information refer to `Capture
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/captures) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (await self._with_raw_response.post_capture(body=body, request_options=request_options)).unwrap()

    async def post_donate(
        self,
        *,
        body: DonationRequest | DonationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Schedules a new payment to be created (including a new authorisation request) for the specified donation
        using the payment details of the original payment.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/donations endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (await self._with_raw_response.post_donate(body=body, request_options=request_options)).unwrap()

    async def post_payments_payment_psp_reference_amount_updates(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAmountUpdateResponse:
        """Increases or decreases the authorised payment amount and returns a unique reference for this request. You get
        the outcome of the request asynchronously, in an `**AUTHORISATION_ADJUSTMENT** webhook
        <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__.

        You can only update authorised amounts that have not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__.

        The amount you specify in the request is the updated amount, which is larger or smaller than the initial
        authorised amount.

        For more information, refer to `Authorisation adjustment
        <https://docs.adyen.com/online-payments/adjust-authorisation#use-cases>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payments_payment_psp_reference_amount_updates(
                payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payments_payment_psp_reference_cancels(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCancelRequest | PaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentCancelResponse:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**CANCELLATION** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment but don't have the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to cancel.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payments_payment_psp_reference_cancels(
                payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payments_payment_psp_reference_captures(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCaptureRequest | PaymentCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentCaptureResponse:
        """Captures an authorised payment and returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CAPTURE** webhook
        <https://docs.adyen.com/online-payments/capture#capture-notification>`__.

        You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed
        amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on
        your account and the payment method supports multiple partial captures.

        `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__ is the default setting
        for most payment methods. In these cases, you don't need to make capture requests. However, making capture
        requests for payments that are captured automatically does not result in double charges.

        For more information, refer to `Capture <https://docs.adyen.com/online-payments/capture>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to capture.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payments_payment_psp_reference_captures(
                payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payments_payment_psp_reference_refunds(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentRefundRequest | PaymentRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentRefundResponse:
        """Refunds a payment that has been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**REFUND** webhook <https://docs.adyen.com/online-payments/refund#refund-webhook>`__.

        You can refund either the full captured amount or a part of the captured amount. You can also perform multiple
        partial refunds, as long as their sum doesn't exceed the captured amount.

        > Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds,
            refer to the payment method page such as `cards
            <https://docs.adyen.com/payment-methods/cards#supported-cards>`__, `iDEAL
            <https://docs.adyen.com/payment-methods/ideal>`__, or `Klarna
            <https://docs.adyen.com/payment-methods/klarna>`__.

        If you want to refund a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Refund <https://docs.adyen.com/online-payments/refund>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to refund.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payments_payment_psp_reference_refunds(
                payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payments_payment_psp_reference_reversals(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentReversalRequest | PaymentReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentReversalResponse:
        """`Refunds
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds>`__ a
        payment if it has already been captured, and `cancels
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels>`__ a
        payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CANCEL_OR_REFUND** webhook
        <https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook>`__.

        The reversed amount is always the full payment amount.
        > Do not use this request for payments that involve multiple partial captures.

        For more information, refer to `Reversal <https://docs.adyen.com/online-payments/reversal>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to reverse.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payments_payment_psp_reference_reversals(
                payment_psp_reference, idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_refund(
        self,
        *,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding
        can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long
        as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot
        be refunded, use the /cancel method instead.

        Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be
        configured to cover shipping/handling costs.

        For more information, refer to `Refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/refunds) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (await self._with_raw_response.post_refund(body=body, request_options=request_options)).unwrap()

    async def post_technical_cancel(
        self,
        *,
        body: TechnicalCancelRequest | TechnicalCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment
        request available.

        In your call, refer to the original payment by using the ``reference`` that you specified in your payment
        request.

        For more information, see `Technical cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_technical_cancel(body=body, request_options=request_options)
        ).unwrap()

    async def post_void_pending_refund(
        self,
        *,
        body: VoidPendingRefundRequest | VoidPendingRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModificationResult:
        """This endpoint allows you to cancel an unreferenced refund request before it has been completed.

        In your call, you can refer to the original refund request either by using the ``tenderReference``, or the
        ``pspReference``. We recommend implementing based on the ``tenderReference``, as this is generated for both
        offline and online transactions.

        For more information, refer to `Cancel an unreferenced refund
        <https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_void_pending_refund(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncModificationsWithRawResponse:
        return self._with_raw_response


class ModificationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_adjust_authorisation(
        self,
        *,
        body: AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostAdjustAuthorisationErrorBody]:
        """Allows you to increase or decrease the authorised amount after the initial authorisation has taken place.
        This functionality enables for example tipping, improving the chances your authorisation will be valid, or
        charging the shopper when they have already left the merchant premises.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/amountUpdates)
            endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/adjustAuthorisation"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_adjust_authorisation_error_mapper,
            request_options=request_options,
        )

    def post_cancel(
        self,
        *,
        body: CancelRequest | CancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCancelErrorBody]:
        """Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel
        payments after authorisation only for payment methods that support distinct authorisations and captures.

        For more information, refer to `Cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/cancels) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelRequest | CancelRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_cancel_error_mapper,
            request_options=request_options,
        )

    def post_cancel_or_refund(
        self,
        *,
        body: CancelOrRefundRequest | CancelOrRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCancelOrRefundErrorBody]:
        """Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is
        useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).

        Do not use this endpoint for payments that involve:
         * `Multiple partial captures <https://docs.adyen.com/online-payments/capture>`__.
         * `Split data <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__
                either at time of payment or capture for Adyen for Platforms.

         Instead, check if the payment has been captured and make a corresponding
            https://docs.adyen.com/api-explorer/#/Payment/refund or https://docs.adyen.com/api-explorer/#/Payment/cancel
            call.

        For more information, refer to `Cancel or refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/reversals) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/cancelOrRefund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelOrRefundRequest | CancelOrRefundRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_cancel_or_refund_error_mapper,
            request_options=request_options,
        )

    def post_cancels(
        self,
        *,
        idempotency_key: str | None = None,
        body: StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StandalonePaymentCancelResponse, PostCancelsErrorBody]:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**TECHNICAL_CANCEL** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment using the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels
        endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/cancels"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StandalonePaymentCancelResponse],
            error_mapper=post_cancels_error_mapper,
            request_options=request_options,
        )

    def post_capture(
        self,
        *,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCaptureErrorBody]:
        """Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full
        authorisation amount is captured, however it's also possible to capture a smaller amount, which results in
        cancelling the remaining authorisation balance.

        Payment methods that are captured automatically after authorisation don't need to be captured. However,
        submitting a capture request on these transactions will not result in double charges. If immediate or delayed
        auto-capture is enabled, calling the capture method is not necessary.

        For more information refer to `Capture
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/captures) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/capture"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CaptureRequest | CaptureRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_capture_error_mapper,
            request_options=request_options,
        )

    def post_donate(
        self,
        *,
        body: DonationRequest | DonationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostDonateErrorBody]:
        """Schedules a new payment to be created (including a new authorisation request) for the specified donation
        using the payment details of the original payment.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/donations endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/donate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationRequest | DonationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_donate_error_mapper,
            request_options=request_options,
        )

    def post_payments_payment_psp_reference_amount_updates(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAmountUpdateResponse, PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody]:
        """Increases or decreases the authorised payment amount and returns a unique reference for this request. You get
        the outcome of the request asynchronously, in an `**AUTHORISATION_ADJUSTMENT** webhook
        <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__.

        You can only update authorised amounts that have not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__.

        The amount you specify in the request is the updated amount, which is larger or smaller than the initial
        authorised amount.

        For more information, refer to `Authorisation adjustment
        <https://docs.adyen.com/online-payments/adjust-authorisation#use-cases>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/amountUpdates"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentAmountUpdateResponse],
            error_mapper=post_payments_payment_psp_reference_amount_updates_error_mapper,
            request_options=request_options,
        )

    def post_payments_payment_psp_reference_cancels(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCancelRequest | PaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentCancelResponse, PostPaymentsPaymentPspReferenceCancelsErrorBody]:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**CANCELLATION** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment but don't have the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to cancel.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/cancels"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentCancelRequest | PaymentCancelRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentCancelResponse],
            error_mapper=post_payments_payment_psp_reference_cancels_error_mapper,
            request_options=request_options,
        )

    def post_payments_payment_psp_reference_captures(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCaptureRequest | PaymentCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentCaptureResponse, PostPaymentsPaymentPspReferenceCapturesErrorBody]:
        """Captures an authorised payment and returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CAPTURE** webhook
        <https://docs.adyen.com/online-payments/capture#capture-notification>`__.

        You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed
        amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on
        your account and the payment method supports multiple partial captures.

        `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__ is the default setting
        for most payment methods. In these cases, you don't need to make capture requests. However, making capture
        requests for payments that are captured automatically does not result in double charges.

        For more information, refer to `Capture <https://docs.adyen.com/online-payments/capture>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to capture.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/captures"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentCaptureRequest | PaymentCaptureRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentCaptureResponse],
            error_mapper=post_payments_payment_psp_reference_captures_error_mapper,
            request_options=request_options,
        )

    def post_payments_payment_psp_reference_refunds(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentRefundRequest | PaymentRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentRefundResponse, PostPaymentsPaymentPspReferenceRefundsErrorBody]:
        """Refunds a payment that has been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**REFUND** webhook <https://docs.adyen.com/online-payments/refund#refund-webhook>`__.

        You can refund either the full captured amount or a part of the captured amount. You can also perform multiple
        partial refunds, as long as their sum doesn't exceed the captured amount.

        > Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds,
            refer to the payment method page such as `cards
            <https://docs.adyen.com/payment-methods/cards#supported-cards>`__, `iDEAL
            <https://docs.adyen.com/payment-methods/ideal>`__, or `Klarna
            <https://docs.adyen.com/payment-methods/klarna>`__.

        If you want to refund a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Refund <https://docs.adyen.com/online-payments/refund>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to refund.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/refunds"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentRefundRequest | PaymentRefundRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentRefundResponse],
            error_mapper=post_payments_payment_psp_reference_refunds_error_mapper,
            request_options=request_options,
        )

    def post_payments_payment_psp_reference_reversals(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentReversalRequest | PaymentReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentReversalResponse, PostPaymentsPaymentPspReferenceReversalsErrorBody]:
        """`Refunds
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds>`__ a
        payment if it has already been captured, and `cancels
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels>`__ a
        payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CANCEL_OR_REFUND** webhook
        <https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook>`__.

        The reversed amount is always the full payment amount.
        > Do not use this request for payments that involve multiple partial captures.

        For more information, refer to `Reversal <https://docs.adyen.com/online-payments/reversal>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to reverse.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/reversals"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentReversalRequest | PaymentReversalRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentReversalResponse],
            error_mapper=post_payments_payment_psp_reference_reversals_error_mapper,
            request_options=request_options,
        )

    def post_refund(
        self,
        *,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostRefundErrorBody]:
        """Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding
        can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long
        as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot
        be refunded, use the /cancel method instead.

        Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be
        configured to cover shipping/handling costs.

        For more information, refer to `Refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/refunds) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/refund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundRequest | RefundRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_refund_error_mapper,
            request_options=request_options,
        )

    def post_technical_cancel(
        self,
        *,
        body: TechnicalCancelRequest | TechnicalCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostTechnicalCancelErrorBody]:
        """This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment
        request available.

        In your call, refer to the original payment by using the ``reference`` that you specified in your payment
        request.

        For more information, see `Technical cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/technicalCancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TechnicalCancelRequest | TechnicalCancelRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_technical_cancel_error_mapper,
            request_options=request_options,
        )

    def post_void_pending_refund(
        self,
        *,
        body: VoidPendingRefundRequest | VoidPendingRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostVoidPendingRefundErrorBody]:
        """This endpoint allows you to cancel an unreferenced refund request before it has been completed.

        In your call, you can refer to the original refund request either by using the ``tenderReference``, or the
        ``pspReference``. We recommend implementing based on the ``tenderReference``, as this is generated for both
        offline and online transactions.

        For more information, refer to `Cancel an unreferenced refund
        <https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/voidPendingRefund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidPendingRefundRequest | VoidPendingRefundRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_void_pending_refund_error_mapper,
            request_options=request_options,
        )


class AsyncModificationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_adjust_authorisation(
        self,
        *,
        body: AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostAdjustAuthorisationErrorBody]:
        """Allows you to increase or decrease the authorised amount after the initial authorisation has taken place.
        This functionality enables for example tipping, improving the chances your authorisation will be valid, or
        charging the shopper when they have already left the merchant premises.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/amountUpdates)
            endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/adjustAuthorisation"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustAuthorisationRequest | AdjustAuthorisationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_adjust_authorisation_error_mapper,
            request_options=request_options,
        )

    async def post_cancel(
        self,
        *,
        body: CancelRequest | CancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCancelErrorBody]:
        """Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel
        payments after authorisation only for payment methods that support distinct authorisations and captures.

        For more information, refer to `Cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/cancels) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelRequest | CancelRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_cancel_error_mapper,
            request_options=request_options,
        )

    async def post_cancel_or_refund(
        self,
        *,
        body: CancelOrRefundRequest | CancelOrRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCancelOrRefundErrorBody]:
        """Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is
        useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).

        Do not use this endpoint for payments that involve:
         * `Multiple partial captures <https://docs.adyen.com/online-payments/capture>`__.
         * `Split data <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__
                either at time of payment or capture for Adyen for Platforms.

         Instead, check if the payment has been captured and make a corresponding
            https://docs.adyen.com/api-explorer/#/Payment/refund or https://docs.adyen.com/api-explorer/#/Payment/cancel
            call.

        For more information, refer to `Cancel or refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/reversals) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/cancelOrRefund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelOrRefundRequest | CancelOrRefundRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_cancel_or_refund_error_mapper,
            request_options=request_options,
        )

    async def post_cancels(
        self,
        *,
        idempotency_key: str | None = None,
        body: StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StandalonePaymentCancelResponse, PostCancelsErrorBody]:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**TECHNICAL_CANCEL** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment using the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels
        endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/cancels"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[StandalonePaymentCancelRequest | StandalonePaymentCancelRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StandalonePaymentCancelResponse],
            error_mapper=post_cancels_error_mapper,
            request_options=request_options,
        )

    async def post_capture(
        self,
        *,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostCaptureErrorBody]:
        """Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full
        authorisation amount is captured, however it's also possible to capture a smaller amount, which results in
        cancelling the remaining authorisation balance.

        Payment methods that are captured automatically after authorisation don't need to be captured. However,
        submitting a capture request on these transactions will not result in double charges. If immediate or delayed
        auto-capture is enabled, calling the capture method is not necessary.

        For more information refer to `Capture
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/captures) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/capture"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CaptureRequest | CaptureRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_capture_error_mapper,
            request_options=request_options,
        )

    async def post_donate(
        self,
        *,
        body: DonationRequest | DonationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostDonateErrorBody]:
        """Schedules a new payment to be created (including a new authorisation request) for the specified donation
        using the payment details of the original payment.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/donations endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/donate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationRequest | DonationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_donate_error_mapper,
            request_options=request_options,
        )

    async def post_payments_payment_psp_reference_amount_updates(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAmountUpdateResponse, PostPaymentsPaymentPspReferenceAmountUpdatesErrorBody]:
        """Increases or decreases the authorised payment amount and returns a unique reference for this request. You get
        the outcome of the request asynchronously, in an `**AUTHORISATION_ADJUSTMENT** webhook
        <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__.

        You can only update authorised amounts that have not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__.

        The amount you specify in the request is the updated amount, which is larger or smaller than the initial
        authorised amount.

        For more information, refer to `Authorisation adjustment
        <https://docs.adyen.com/online-payments/adjust-authorisation#use-cases>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/amountUpdates"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentAmountUpdateRequest | PaymentAmountUpdateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentAmountUpdateResponse],
            error_mapper=post_payments_payment_psp_reference_amount_updates_error_mapper,
            request_options=request_options,
        )

    async def post_payments_payment_psp_reference_cancels(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCancelRequest | PaymentCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentCancelResponse, PostPaymentsPaymentPspReferenceCancelsErrorBody]:
        """Cancels the authorisation on a payment that has not yet been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**CANCELLATION** webhook <https://docs.adyen.com/online-payments/cancel#cancellation-webhook>`__.

        If you want to cancel a payment but don't have the
        https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels endpoint instead.

        If you want to cancel a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Cancel <https://docs.adyen.com/online-payments/cancel>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to cancel.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/cancels"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentCancelRequest | PaymentCancelRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentCancelResponse],
            error_mapper=post_payments_payment_psp_reference_cancels_error_mapper,
            request_options=request_options,
        )

    async def post_payments_payment_psp_reference_captures(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentCaptureRequest | PaymentCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentCaptureResponse, PostPaymentsPaymentPspReferenceCapturesErrorBody]:
        """Captures an authorised payment and returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CAPTURE** webhook
        <https://docs.adyen.com/online-payments/capture#capture-notification>`__.

        You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed
        amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on
        your account and the payment method supports multiple partial captures.

        `Automatic capture <https://docs.adyen.com/online-payments/capture#automatic-capture>`__ is the default setting
        for most payment methods. In these cases, you don't need to make capture requests. However, making capture
        requests for payments that are captured automatically does not result in double charges.

        For more information, refer to `Capture <https://docs.adyen.com/online-payments/capture>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to capture.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/captures"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentCaptureRequest | PaymentCaptureRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentCaptureResponse],
            error_mapper=post_payments_payment_psp_reference_captures_error_mapper,
            request_options=request_options,
        )

    async def post_payments_payment_psp_reference_refunds(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentRefundRequest | PaymentRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentRefundResponse, PostPaymentsPaymentPspReferenceRefundsErrorBody]:
        """Refunds a payment that has been `captured
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures>`__,
        and returns a unique reference for this request. You get the outcome of the request asynchronously, in a
        `**REFUND** webhook <https://docs.adyen.com/online-payments/refund#refund-webhook>`__.

        You can refund either the full captured amount or a part of the captured amount. You can also perform multiple
        partial refunds, as long as their sum doesn't exceed the captured amount.

        > Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds,
            refer to the payment method page such as `cards
            <https://docs.adyen.com/payment-methods/cards#supported-cards>`__, `iDEAL
            <https://docs.adyen.com/payment-methods/ideal>`__, or `Klarna
            <https://docs.adyen.com/payment-methods/klarna>`__.

        If you want to refund a payment but are not sure whether it has been captured, use the
        https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals
        endpoint instead.

        For more information, refer to `Refund <https://docs.adyen.com/online-payments/refund>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to refund.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/refunds"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentRefundRequest | PaymentRefundRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentRefundResponse],
            error_mapper=post_payments_payment_psp_reference_refunds_error_mapper,
            request_options=request_options,
        )

    async def post_payments_payment_psp_reference_reversals(
        self,
        payment_psp_reference: str,
        *,
        idempotency_key: str | None = None,
        body: PaymentReversalRequest | PaymentReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentReversalResponse, PostPaymentsPaymentPspReferenceReversalsErrorBody]:
        """`Refunds
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds>`__ a
        payment if it has already been captured, and `cancels
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels>`__ a
        payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the
        request asynchronously, in a `**CANCEL_OR_REFUND** webhook
        <https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook>`__.

        The reversed amount is always the full payment amount.
        > Do not use this request for payments that involve multiple partial captures.

        For more information, refer to `Reversal <https://docs.adyen.com/online-payments/reversal>`__.

        Args:
            payment_psp_reference: The
                https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the
                payment that you want to reverse.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/{paymentPspReference}/reversals"),
            path_params=[param[str]("paymentPspReference", payment_psp_reference)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentReversalRequest | PaymentReversalRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentReversalResponse],
            error_mapper=post_payments_payment_psp_reference_reversals_error_mapper,
            request_options=request_options,
        )

    async def post_refund(
        self,
        *,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostRefundErrorBody]:
        """Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding
        can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long
        as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot
        be refunded, use the /cancel method instead.

        Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be
        configured to cover shipping/handling costs.

        For more information, refer to `Refund
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference/refunds) endpoint
            instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/refund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundRequest | RefundRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_refund_error_mapper,
            request_options=request_options,
        )

    async def post_technical_cancel(
        self,
        *,
        body: TechnicalCancelRequest | TechnicalCancelRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostTechnicalCancelErrorBody]:
        """This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment
        request available.

        In your call, refer to the original payment by using the ``reference`` that you specified in your payment
        request.

        For more information, see `Technical cancel
        <https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel>`__.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/technicalCancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TechnicalCancelRequest | TechnicalCancelRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_technical_cancel_error_mapper,
            request_options=request_options,
        )

    async def post_void_pending_refund(
        self,
        *,
        body: VoidPendingRefundRequest | VoidPendingRefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModificationResult, PostVoidPendingRefundErrorBody]:
        """This endpoint allows you to cancel an unreferenced refund request before it has been completed.

        In your call, you can refer to the original refund request either by using the ``tenderReference``, or the
        ``pspReference``. We recommend implementing based on the ``tenderReference``, as this is generated for both
        offline and online transactions.

        For more information, refer to `Cancel an unreferenced refund
        <https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/voidPendingRefund"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidPendingRefundRequest | VoidPendingRefundRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModificationResult],
            error_mapper=post_void_pending_refund_error_mapper,
            request_options=request_options,
        )
