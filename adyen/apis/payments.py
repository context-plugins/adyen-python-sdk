from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.post_authorise3_d_error import PostAuthorise3DErrorBody, post_authorise3_d_error_mapper
from ..errors.post_authorise3_ds2_error import PostAuthorise3Ds2ErrorBody, post_authorise3_ds2_error_mapper
from ..errors.post_authorise_error import PostAuthoriseErrorBody, post_authorise_error_mapper
from ..errors.post_get_authentication_result_error import (
    PostGetAuthenticationResultErrorBody,
    post_get_authentication_result_error_mapper,
)
from ..errors.post_payment_methods_error import PostPaymentMethodsErrorBody, post_payment_methods_error_mapper
from ..errors.post_payments_cancel_error import PostPaymentsCancelErrorBody, post_payments_cancel_error_mapper
from ..errors.post_payments_confirm_error import PostPaymentsConfirmErrorBody, post_payments_confirm_error_mapper
from ..errors.post_payments_details1_error import PostPaymentsDetails1ErrorBody, post_payments_details1_error_mapper
from ..errors.post_payments_details_error import PostPaymentsDetailsErrorBody, post_payments_details_error_mapper
from ..errors.post_payments_error import PostPaymentsErrorBody, post_payments_error_mapper
from ..errors.post_retrieve3_ds2_result_error import (
    PostRetrieve3Ds2ResultErrorBody,
    post_retrieve3_ds2_result_error_mapper,
)
from ..models.authentication_result_request import AuthenticationResultRequest, AuthenticationResultRequestDict
from ..models.authentication_result_response import AuthenticationResultResponse
from ..models.cancel_payment_request import CancelPaymentRequest, CancelPaymentRequestDict
from ..models.cancel_payment_response import CancelPaymentResponse
from ..models.card_details_request import CardDetailsRequest, CardDetailsRequestDict
from ..models.card_details_response import CardDetailsResponse
from ..models.confirm_payment_request import ConfirmPaymentRequest, ConfirmPaymentRequestDict
from ..models.confirm_payment_response import ConfirmPaymentResponse
from ..models.create_checkout_session_request import CreateCheckoutSessionRequest, CreateCheckoutSessionRequestDict
from ..models.create_checkout_session_response import CreateCheckoutSessionResponse
from ..models.ideal_payment_details_request import IdealPaymentDetailsRequest, IdealPaymentDetailsRequestDict
from ..models.payment_details_request import PaymentDetailsRequest, PaymentDetailsRequestDict
from ..models.payment_details_response import PaymentDetailsResponse
from ..models.payment_details_response1 import PaymentDetailsResponse1
from ..models.payment_methods_request import PaymentMethodsRequest, PaymentMethodsRequestDict
from ..models.payment_methods_response import PaymentMethodsResponse
from ..models.payment_request import PaymentRequest, PaymentRequestDict
from ..models.payment_request1 import PaymentRequest1, PaymentRequest1Dict
from ..models.payment_request3_d import PaymentRequest3D, PaymentRequest3DDict
from ..models.payment_request3_ds2 import PaymentRequest3Ds2, PaymentRequest3Ds2Dict
from ..models.payment_response import PaymentResponse
from ..models.payment_result import PaymentResult
from ..models.session_result_response import SessionResultResponse
from ..models.three_ds2_result_request import ThreeDs2ResultRequest, ThreeDs2ResultRequestDict
from ..models.three_ds2_result_response import ThreeDs2ResultResponse
from ..server.server import Server


class Payments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentsWithRawResponse(client, server, auth)

    def get_sessions_session_id(
        self, session_id: str, session_result: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SessionResultResponse:
        """Returns the status of the payment session with the ``sessionId`` and ``sessionResult`` specified in the path.

        Args:
            session_id: A unique identifier of the session.
            session_result: The ``sessionResult`` value from the Drop-in or Component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_sessions_session_id(session_id, session_result, request_options=request_options)
        )

    def post_authorise(
        self,
        *,
        body: PaymentRequest1 | PaymentRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """Creates a payment with a unique reference (``pspReference``) and attempts to obtain an authorisation hold.
        For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this
        and will automatically capture as part of the authorisation.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_authorise(body=body, request_options=request_options))

    def post_authorise3d(
        self,
        *,
        body: PaymentRequest3D | PaymentRequest3DDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the
        ``md`` and ``paResponse`` parameters that you get from the card issuer after a shopper pays via 3D Secure.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_authorise3d(body=body, request_options=request_options))

    def post_authorise3ds2(
        self,
        *,
        body: PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the
        ``threeDS2Token`` and ``threeDS2Result`` parameters.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_authorise3ds2(body=body, request_options=request_options))

    def post_card_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: CardDetailsRequest | CardDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CardDetailsResponse:
        """Use this endpoint to get information about the card or network token that enables you to decide on the
        routing of the transaction and the eligibility of the card for the type of transaction.

        If you include `your supported brands
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands>`__ in
        the request, the response also tells you if you support each `brand that was identified on the card
        <https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails#responses-200-brands>`__.

        If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card
        is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with if you support both
        brands.

        ## Server-side API libraries We provide open-source `server-side API libraries
        <https://docs.adyen.com/development-resources/libraries/>`__ in several languages:
        - PHP
        - Java
        - Node.js
        - .NET
        - Go
        - Python
        - Ruby
        - Apex (beta)

        See our `integration examples <https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples>`__ for
        example uses of the libraries.

        ## Developer resources BIN Lookup API is available through a Postman collection. Click the button below to
        create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

        `![Run in Postman
        <https://run.pstmn.io/button.svg>`__](https://god.gw.postman.com/run-collection/25716737-677c7679-a695-4ebb-91da-68b4e7c9228a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-677c7679-a695-4ebb-91da-68b4e7c9228a%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.post_card_details(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_get_authentication_result(
        self,
        *,
        body: AuthenticationResultRequest | AuthenticationResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthenticationResultResponse:
        """Return the authentication result after doing a 3D Secure authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_get_authentication_result(body=body, request_options=request_options)
        )

    def post_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentMethodsRequest | PaymentMethodsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodsResponse:
        """Retrieves the list of available payment methods for the transaction, based on the transaction information
        like amount, country, and currency.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_payment_methods(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_payments(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentRequest | PaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResponse:
        """Sends payment parameters (like amount, country, and currency) together with other required input details
        collected from the shopper. To know more about required parameters for specific payment methods, refer to our
        `payment method guides <https://docs.adyen.com/payment-methods>`__. The response depends on the `payment flow
        <https://docs.adyen.com/payment-methods#payment-flow>`__:
        * For a direct flow, the response includes a ``pspReference`` and a ``resultCode`` with the payment result, for
            example **Authorised** or **Refused**.
        * For a redirect or additional action, the response contains an ``action`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_payments(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_payments_cancel(
        self,
        body: CancelPaymentRequest | CancelPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelPaymentResponse:
        """Cancels the payment. Returns a URL for user redirection.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_payments_cancel(body, request_options=request_options))

    def post_payments_confirm(
        self,
        body: ConfirmPaymentRequest | ConfirmPaymentRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmPaymentResponse:
        """Confirms the payment using Strong Customer Authentication (SCA).

        To confirm a payment you must make this request two times:

            1. Make this request to initiate SCA and receive the WWW-Authenticate header.
            2. After the user completes the SCA challenge, make this request again, including the updated
                WWW-Authenticate header.

            The second response provides a redirection URL that guides the user to a payment success or failure page.
        For more information, see our `documentation
        <https://docs.adyen.com/business-accounts/send-funds-ideal-integration>`__.

        Args:
            body: The request body.
            www_authenticate: Header for authenticating through SCA: Contains information for an SCA challenge for A2A
                payments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Unprocessable Entity -
                A request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_payments_confirm(
                body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    def post_payments_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentDetailsRequest | PaymentDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentDetailsResponse:
        """Submits details for a payment created using ``/payments``. This step is only needed when no final state has
        been reached on the ``/payments`` request, for example when the shopper was redirected to another page to
        complete the payment.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_payments_details(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_payments_details1(
        self,
        body: IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentDetailsResponse1:
        """Returns the details of an open payment, which you must show to the user. Also provides a token required to
        `confirm <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/confirm>`__ or `cancel
        <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/cancel>`__ the payment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_payments_details1(body, request_options=request_options))

    def post_retrieve3ds2_result(
        self,
        *,
        body: ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ThreeDs2ResultResponse:
        """Retrieves the ``threeDS2Result`` after doing a 3D Secure 2 authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_retrieve3ds2_result(body=body, request_options=request_options))

    def post_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCheckoutSessionResponse:
        """Creates a payment session for `Drop-in
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Drop-in>`__,
        `Components
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Components>`__,
        and `Hosted Checkout
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Hosted+Checkout>`__
        integrations.

        The response contains encrypted payment session data. The front end then uses the session data to make any
        required server-side calls for the payment flow.

        You get the payment outcome asynchronously, in an `AUTHORISATION
        <https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION>`__ webhook.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.post_sessions(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        return self._with_raw_response


class AsyncPayments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentsWithRawResponse(client, server, auth)

    async def get_sessions_session_id(
        self, session_id: str, session_result: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SessionResultResponse:
        """Returns the status of the payment session with the ``sessionId`` and ``sessionResult`` specified in the path.

        Args:
            session_id: A unique identifier of the session.
            session_result: The ``sessionResult`` value from the Drop-in or Component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_sessions_session_id(
                session_id, session_result, request_options=request_options
            ),
        )

    async def post_authorise(
        self,
        *,
        body: PaymentRequest1 | PaymentRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """Creates a payment with a unique reference (``pspReference``) and attempts to obtain an authorisation hold.
        For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this
        and will automatically capture as part of the authorisation.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_authorise(body=body, request_options=request_options))

    async def post_authorise3d(
        self,
        *,
        body: PaymentRequest3D | PaymentRequest3DDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the
        ``md`` and ``paResponse`` parameters that you get from the card issuer after a shopper pays via 3D Secure.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_authorise3d(body=body, request_options=request_options))

    async def post_authorise3ds2(
        self,
        *,
        body: PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResult:
        """For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the
        ``threeDS2Token`` and ``threeDS2Result`` parameters.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_authorise3ds2(body=body, request_options=request_options))

    async def post_card_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: CardDetailsRequest | CardDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CardDetailsResponse:
        """Use this endpoint to get information about the card or network token that enables you to decide on the
        routing of the transaction and the eligibility of the card for the type of transaction.

        If you include `your supported brands
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands>`__ in
        the request, the response also tells you if you support each `brand that was identified on the card
        <https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails#responses-200-brands>`__.

        If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card
        is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with if you support both
        brands.

        ## Server-side API libraries We provide open-source `server-side API libraries
        <https://docs.adyen.com/development-resources/libraries/>`__ in several languages:
        - PHP
        - Java
        - Node.js
        - .NET
        - Go
        - Python
        - Ruby
        - Apex (beta)

        See our `integration examples <https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples>`__ for
        example uses of the libraries.

        ## Developer resources BIN Lookup API is available through a Postman collection. Click the button below to
        create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

        `![Run in Postman
        <https://run.pstmn.io/button.svg>`__](https://god.gw.postman.com/run-collection/25716737-677c7679-a695-4ebb-91da-68b4e7c9228a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-677c7679-a695-4ebb-91da-68b4e7c9228a%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.post_card_details(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_get_authentication_result(
        self,
        *,
        body: AuthenticationResultRequest | AuthenticationResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthenticationResultResponse:
        """Return the authentication result after doing a 3D Secure authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_authentication_result(body=body, request_options=request_options)
        )

    async def post_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentMethodsRequest | PaymentMethodsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodsResponse:
        """Retrieves the list of available payment methods for the transaction, based on the transaction information
        like amount, country, and currency.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payment_methods(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_payments(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentRequest | PaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResponse:
        """Sends payment parameters (like amount, country, and currency) together with other required input details
        collected from the shopper. To know more about required parameters for specific payment methods, refer to our
        `payment method guides <https://docs.adyen.com/payment-methods>`__. The response depends on the `payment flow
        <https://docs.adyen.com/payment-methods#payment-flow>`__:
        * For a direct flow, the response includes a ``pspReference`` and a ``resultCode`` with the payment result, for
            example **Authorised** or **Refused**.
        * For a redirect or additional action, the response contains an ``action`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payments(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_payments_cancel(
        self,
        body: CancelPaymentRequest | CancelPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelPaymentResponse:
        """Cancels the payment. Returns a URL for user redirection.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_payments_cancel(body, request_options=request_options))

    async def post_payments_confirm(
        self,
        body: ConfirmPaymentRequest | ConfirmPaymentRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmPaymentResponse:
        """Confirms the payment using Strong Customer Authentication (SCA).

        To confirm a payment you must make this request two times:

            1. Make this request to initiate SCA and receive the WWW-Authenticate header.
            2. After the user completes the SCA challenge, make this request again, including the updated
                WWW-Authenticate header.

            The second response provides a redirection URL that guides the user to a payment success or failure page.
        For more information, see our `documentation
        <https://docs.adyen.com/business-accounts/send-funds-ideal-integration>`__.

        Args:
            body: The request body.
            www_authenticate: Header for authenticating through SCA: Contains information for an SCA challenge for A2A
                payments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Unprocessable Entity -
                A request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payments_confirm(
                body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    async def post_payments_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentDetailsRequest | PaymentDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentDetailsResponse:
        """Submits details for a payment created using ``/payments``. This step is only needed when no final state has
        been reached on the ``/payments`` request, for example when the shopper was redirected to another page to
        complete the payment.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payments_details(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_payments_details1(
        self,
        body: IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentDetailsResponse1:
        """Returns the details of an open payment, which you must show to the user. Also provides a token required to
        `confirm <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/confirm>`__ or `cancel
        <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/cancel>`__ the payment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_payments_details1(body, request_options=request_options))

    async def post_retrieve3ds2_result(
        self,
        *,
        body: ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ThreeDs2ResultResponse:
        """Retrieves the ``threeDS2Result`` after doing a 3D Secure 2 authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_retrieve3ds2_result(body=body, request_options=request_options)
        )

    async def post_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCheckoutSessionResponse:
        """Creates a payment session for `Drop-in
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Drop-in>`__,
        `Components
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Components>`__,
        and `Hosted Checkout
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Hosted+Checkout>`__
        integrations.

        The response contains encrypted payment session data. The front end then uses the session data to make any
        required server-side calls for the payment flow.

        You get the payment outcome asynchronously, in an `AUTHORISATION
        <https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION>`__ webhook.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.post_sessions(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        return self._with_raw_response


class PaymentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_sessions_session_id(
        self, session_id: str, session_result: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SessionResultResponse, RawError]:
        """Returns the status of the payment session with the ``sessionId`` and ``sessionResult`` specified in the path.

        Args:
            session_id: A unique identifier of the session.
            session_result: The ``sessionResult`` value from the Drop-in or Component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sessions/{sessionId}"),
            path_params=[param[str]("sessionId", session_id)],
            query_params=[param[str]("sessionResult", session_result)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SessionResultResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_authorise(
        self,
        *,
        body: PaymentRequest1 | PaymentRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthoriseErrorBody]:
        """Creates a payment with a unique reference (``pspReference``) and attempts to obtain an authorisation hold.
        For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this
        and will automatically capture as part of the authorisation.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest1 | PaymentRequest1Dict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentResult],
            error_mapper=post_authorise_error_mapper,
            request_options=request_options,
        )

    def post_authorise3d(
        self,
        *,
        body: PaymentRequest3D | PaymentRequest3DDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthorise3DErrorBody]:
        """For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the
        ``md`` and ``paResponse`` parameters that you get from the card issuer after a shopper pays via 3D Secure.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise3d"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest3D | PaymentRequest3DDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentResult],
            error_mapper=post_authorise3_d_error_mapper,
            request_options=request_options,
        )

    def post_authorise3ds2(
        self,
        *,
        body: PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthorise3Ds2ErrorBody]:
        """For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the
        ``threeDS2Token`` and ``threeDS2Result`` parameters.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise3ds2"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentResult],
            error_mapper=post_authorise3_ds2_error_mapper,
            request_options=request_options,
        )

    def post_card_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: CardDetailsRequest | CardDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CardDetailsResponse, RawError]:
        """Use this endpoint to get information about the card or network token that enables you to decide on the
        routing of the transaction and the eligibility of the card for the type of transaction.

        If you include `your supported brands
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands>`__ in
        the request, the response also tells you if you support each `brand that was identified on the card
        <https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails#responses-200-brands>`__.

        If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card
        is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with if you support both
        brands.

        ## Server-side API libraries We provide open-source `server-side API libraries
        <https://docs.adyen.com/development-resources/libraries/>`__ in several languages:
        - PHP
        - Java
        - Node.js
        - .NET
        - Go
        - Python
        - Ruby
        - Apex (beta)

        See our `integration examples <https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples>`__ for
        example uses of the libraries.

        ## Developer resources BIN Lookup API is available through a Postman collection. Click the button below to
        create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

        `![Run in Postman
        <https://run.pstmn.io/button.svg>`__](https://god.gw.postman.com/run-collection/25716737-677c7679-a695-4ebb-91da-68b4e7c9228a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-677c7679-a695-4ebb-91da-68b4e7c9228a%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/cardDetails"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CardDetailsRequest | CardDetailsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CardDetailsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_get_authentication_result(
        self,
        *,
        body: AuthenticationResultRequest | AuthenticationResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthenticationResultResponse, PostGetAuthenticationResultErrorBody]:
        """Return the authentication result after doing a 3D Secure authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/getAuthenticationResult"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthenticationResultRequest | AuthenticationResultRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AuthenticationResultResponse],
            error_mapper=post_get_authentication_result_error_mapper,
            request_options=request_options,
        )

    def post_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentMethodsRequest | PaymentMethodsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodsResponse, PostPaymentMethodsErrorBody]:
        """Retrieves the list of available payment methods for the transaction, based on the transaction information
        like amount, country, and currency.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentMethods"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentMethodsRequest | PaymentMethodsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentMethodsResponse],
            error_mapper=post_payment_methods_error_mapper,
            request_options=request_options,
        )

    def post_payments(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentRequest | PaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResponse, PostPaymentsErrorBody]:
        """Sends payment parameters (like amount, country, and currency) together with other required input details
        collected from the shopper. To know more about required parameters for specific payment methods, refer to our
        `payment method guides <https://docs.adyen.com/payment-methods>`__. The response depends on the `payment flow
        <https://docs.adyen.com/payment-methods#payment-flow>`__:
        * For a direct flow, the response includes a ``pspReference`` and a ``resultCode`` with the payment result, for
            example **Authorised** or **Refused**.
        * For a redirect or additional action, the response contains an ``action`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentRequest | PaymentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentResponse],
            error_mapper=post_payments_error_mapper,
            request_options=request_options,
        )

    def post_payments_cancel(
        self,
        body: CancelPaymentRequest | CancelPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelPaymentResponse, PostPaymentsCancelErrorBody]:
        """Cancels the payment. Returns a URL for user redirection.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelPaymentRequest | CancelPaymentRequestDict](body),
            decoder=json_decoder[CancelPaymentResponse],
            error_mapper=post_payments_cancel_error_mapper,
            request_options=request_options,
        )

    def post_payments_confirm(
        self,
        body: ConfirmPaymentRequest | ConfirmPaymentRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmPaymentResponse, PostPaymentsConfirmErrorBody]:
        """Confirms the payment using Strong Customer Authentication (SCA).

        To confirm a payment you must make this request two times:

            1. Make this request to initiate SCA and receive the WWW-Authenticate header.
            2. After the user completes the SCA challenge, make this request again, including the updated
                WWW-Authenticate header.

            The second response provides a redirection URL that guides the user to a payment success or failure page.
        For more information, see our `documentation
        <https://docs.adyen.com/business-accounts/send-funds-ideal-integration>`__.

        Args:
            body: The request body.
            www_authenticate: Header for authenticating through SCA: Contains information for an SCA challenge for A2A
                payments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/confirm"),
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmPaymentRequest | ConfirmPaymentRequestDict](body),
            decoder=json_decoder[ConfirmPaymentResponse],
            error_mapper=post_payments_confirm_error_mapper,
            request_options=request_options,
        )

    def post_payments_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentDetailsRequest | PaymentDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentDetailsResponse, PostPaymentsDetailsErrorBody]:
        """Submits details for a payment created using ``/payments``. This step is only needed when no final state has
        been reached on the ``/payments`` request, for example when the shopper was redirected to another page to
        complete the payment.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/details"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentDetailsRequest | PaymentDetailsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentDetailsResponse],
            error_mapper=post_payments_details_error_mapper,
            request_options=request_options,
        )

    def post_payments_details1(
        self,
        body: IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentDetailsResponse1, PostPaymentsDetails1ErrorBody]:
        """Returns the details of an open payment, which you must show to the user. Also provides a token required to
        `confirm <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/confirm>`__ or `cancel
        <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/cancel>`__ the payment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/details"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict](body),
            decoder=json_decoder[PaymentDetailsResponse1],
            error_mapper=post_payments_details1_error_mapper,
            request_options=request_options,
        )

    def post_retrieve3ds2_result(
        self,
        *,
        body: ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ThreeDs2ResultResponse, PostRetrieve3Ds2ResultErrorBody]:
        """Retrieves the ``threeDS2Result`` after doing a 3D Secure 2 authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/retrieve3ds2Result"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ThreeDs2ResultResponse],
            error_mapper=post_retrieve3_ds2_result_error_mapper,
            request_options=request_options,
        )

    def post_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCheckoutSessionResponse, RawError]:
        """Creates a payment session for `Drop-in
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Drop-in>`__,
        `Components
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Components>`__,
        and `Hosted Checkout
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Hosted+Checkout>`__
        integrations.

        The response contains encrypted payment session data. The front end then uses the session data to make any
        required server-side calls for the payment flow.

        You get the payment outcome asynchronously, in an `AUTHORISATION
        <https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION>`__ webhook.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sessions"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateCheckoutSessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPaymentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_sessions_session_id(
        self, session_id: str, session_result: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SessionResultResponse, RawError]:
        """Returns the status of the payment session with the ``sessionId`` and ``sessionResult`` specified in the path.

        Args:
            session_id: A unique identifier of the session.
            session_result: The ``sessionResult`` value from the Drop-in or Component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sessions/{sessionId}"),
            path_params=[param[str]("sessionId", session_id)],
            query_params=[param[str]("sessionResult", session_result)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SessionResultResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_authorise(
        self,
        *,
        body: PaymentRequest1 | PaymentRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthoriseErrorBody]:
        """Creates a payment with a unique reference (``pspReference``) and attempts to obtain an authorisation hold.
        For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this
        and will automatically capture as part of the authorisation.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest1 | PaymentRequest1Dict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentResult],
            error_mapper=post_authorise_error_mapper,
            request_options=request_options,
        )

    async def post_authorise3d(
        self,
        *,
        body: PaymentRequest3D | PaymentRequest3DDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthorise3DErrorBody]:
        """For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the
        ``md`` and ``paResponse`` parameters that you get from the card issuer after a shopper pays via 3D Secure.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        > The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
            accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise3d"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest3D | PaymentRequest3DDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentResult],
            error_mapper=post_authorise3_d_error_mapper,
            request_options=request_options,
        )

    async def post_authorise3ds2(
        self,
        *,
        body: PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResult, PostAuthorise3Ds2ErrorBody]:
        """For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the
        ``threeDS2Token`` and ``threeDS2Result`` parameters.

        > This endpoint is `inactive
            <https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle>`__ and is no longer
            supported for new integrations.
        > * If you are building a new integration, use the Checkout API
            https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details endpoint instead.
        > * If you have an existing integration using this endpoint, reach out to your Adyen contact and `migrate to the
            Checkout API <https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api>`__.

        >The Checkout API enables your `online payments <https://docs.adyen.com/online-payments>`__ integration to
        accept all supported payment methods, use the latest features, and access more benefits.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/authorise3ds2"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest3Ds2 | PaymentRequest3Ds2Dict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentResult],
            error_mapper=post_authorise3_ds2_error_mapper,
            request_options=request_options,
        )

    async def post_card_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: CardDetailsRequest | CardDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CardDetailsResponse, RawError]:
        """Use this endpoint to get information about the card or network token that enables you to decide on the
        routing of the transaction and the eligibility of the card for the type of transaction.

        If you include `your supported brands
        <https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands>`__ in
        the request, the response also tells you if you support each `brand that was identified on the card
        <https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails#responses-200-brands>`__.

        If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card
        is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with if you support both
        brands.

        ## Server-side API libraries We provide open-source `server-side API libraries
        <https://docs.adyen.com/development-resources/libraries/>`__ in several languages:
        - PHP
        - Java
        - Node.js
        - .NET
        - Go
        - Python
        - Ruby
        - Apex (beta)

        See our `integration examples <https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples>`__ for
        example uses of the libraries.

        ## Developer resources BIN Lookup API is available through a Postman collection. Click the button below to
        create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

        `![Run in Postman
        <https://run.pstmn.io/button.svg>`__](https://god.gw.postman.com/run-collection/25716737-677c7679-a695-4ebb-91da-68b4e7c9228a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-677c7679-a695-4ebb-91da-68b4e7c9228a%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/cardDetails"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CardDetailsRequest | CardDetailsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CardDetailsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_get_authentication_result(
        self,
        *,
        body: AuthenticationResultRequest | AuthenticationResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthenticationResultResponse, PostGetAuthenticationResultErrorBody]:
        """Return the authentication result after doing a 3D Secure authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/getAuthenticationResult"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthenticationResultRequest | AuthenticationResultRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AuthenticationResultResponse],
            error_mapper=post_get_authentication_result_error_mapper,
            request_options=request_options,
        )

    async def post_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentMethodsRequest | PaymentMethodsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodsResponse, PostPaymentMethodsErrorBody]:
        """Retrieves the list of available payment methods for the transaction, based on the transaction information
        like amount, country, and currency.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentMethods"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentMethodsRequest | PaymentMethodsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentMethodsResponse],
            error_mapper=post_payment_methods_error_mapper,
            request_options=request_options,
        )

    async def post_payments(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentRequest | PaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResponse, PostPaymentsErrorBody]:
        """Sends payment parameters (like amount, country, and currency) together with other required input details
        collected from the shopper. To know more about required parameters for specific payment methods, refer to our
        `payment method guides <https://docs.adyen.com/payment-methods>`__. The response depends on the `payment flow
        <https://docs.adyen.com/payment-methods#payment-flow>`__:
        * For a direct flow, the response includes a ``pspReference`` and a ``resultCode`` with the payment result, for
            example **Authorised** or **Refused**.
        * For a redirect or additional action, the response contains an ``action`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentRequest | PaymentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentResponse],
            error_mapper=post_payments_error_mapper,
            request_options=request_options,
        )

    async def post_payments_cancel(
        self,
        body: CancelPaymentRequest | CancelPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelPaymentResponse, PostPaymentsCancelErrorBody]:
        """Cancels the payment. Returns a URL for user redirection.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelPaymentRequest | CancelPaymentRequestDict](body),
            decoder=async_json_decoder[CancelPaymentResponse],
            error_mapper=post_payments_cancel_error_mapper,
            request_options=request_options,
        )

    async def post_payments_confirm(
        self,
        body: ConfirmPaymentRequest | ConfirmPaymentRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmPaymentResponse, PostPaymentsConfirmErrorBody]:
        """Confirms the payment using Strong Customer Authentication (SCA).

        To confirm a payment you must make this request two times:

            1. Make this request to initiate SCA and receive the WWW-Authenticate header.
            2. After the user completes the SCA challenge, make this request again, including the updated
                WWW-Authenticate header.

            The second response provides a redirection URL that guides the user to a payment success or failure page.
        For more information, see our `documentation
        <https://docs.adyen.com/business-accounts/send-funds-ideal-integration>`__.

        Args:
            body: The request body.
            www_authenticate: Header for authenticating through SCA: Contains information for an SCA challenge for A2A
                payments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/confirm"),
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmPaymentRequest | ConfirmPaymentRequestDict](body),
            decoder=async_json_decoder[ConfirmPaymentResponse],
            error_mapper=post_payments_confirm_error_mapper,
            request_options=request_options,
        )

    async def post_payments_details(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentDetailsRequest | PaymentDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentDetailsResponse, PostPaymentsDetailsErrorBody]:
        """Submits details for a payment created using ``/payments``. This step is only needed when no final state has
        been reached on the ``/payments`` request, for example when the shopper was redirected to another page to
        complete the payment.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payments/details"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentDetailsRequest | PaymentDetailsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentDetailsResponse],
            error_mapper=post_payments_details_error_mapper,
            request_options=request_options,
        )

    async def post_payments_details1(
        self,
        body: IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentDetailsResponse1, PostPaymentsDetails1ErrorBody]:
        """Returns the details of an open payment, which you must show to the user. Also provides a token required to
        `confirm <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/confirm>`__ or `cancel
        <https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/cancel>`__ the payment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/payments/details"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealPaymentDetailsRequest | IdealPaymentDetailsRequestDict](body),
            decoder=async_json_decoder[PaymentDetailsResponse1],
            error_mapper=post_payments_details1_error_mapper,
            request_options=request_options,
        )

    async def post_retrieve3ds2_result(
        self,
        *,
        body: ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ThreeDs2ResultResponse, PostRetrieve3Ds2ResultErrorBody]:
        """Retrieves the ``threeDS2Result`` after doing a 3D Secure 2 authentication only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/retrieve3ds2Result"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ThreeDs2ResultRequest | ThreeDs2ResultRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ThreeDs2ResultResponse],
            error_mapper=post_retrieve3_ds2_result_error_mapper,
            request_options=request_options,
        )

    async def post_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCheckoutSessionResponse, RawError]:
        """Creates a payment session for `Drop-in
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Drop-in>`__,
        `Components
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Components>`__,
        and `Hosted Checkout
        <https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Hosted+Checkout>`__
        integrations.

        The response contains encrypted payment session data. The front end then uses the session data to make any
        required server-side calls for the payment flow.

        You get the payment outcome asynchronously, in an `AUTHORISATION
        <https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION>`__ webhook.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sessions"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CreateCheckoutSessionRequest | CreateCheckoutSessionRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CreateCheckoutSessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
