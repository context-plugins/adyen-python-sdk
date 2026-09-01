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
from ..errors.get_payment_links_link_id_error import (
    GetPaymentLinksLinkIdErrorBody,
    get_payment_links_link_id_error_mapper,
)
from ..errors.patch_payment_links_link_id_error import (
    PatchPaymentLinksLinkIdErrorBody,
    patch_payment_links_link_id_error_mapper,
)
from ..errors.post_payment_links_error import PostPaymentLinksErrorBody, post_payment_links_error_mapper
from ..models.payment_link_request import PaymentLinkRequest, PaymentLinkRequestDict
from ..models.payment_link_response import PaymentLinkResponse
from ..models.update_payment_link_request import UpdatePaymentLinkRequest, UpdatePaymentLinkRequestDict
from ..server.server import Server


class PaymentLinks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentLinksWithRawResponse(client, server, auth)

    def get_payment_links_link_id(
        self, link_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentLinkResponse:
        """Retrieves the payment link details using the payment link ``id``.

        Args:
            link_id: Unique identifier of the payment link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.get_payment_links_link_id(link_id, request_options=request_options).unwrap()

    def patch_payment_links_link_id(
        self,
        link_id: str,
        *,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentLinkResponse:
        """Updates the status of a payment link. Use this endpoint to `force the expiry of a payment link
        <https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status>`__.

        Args:
            link_id: Unique identifier of the payment link.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.patch_payment_links_link_id(
            link_id, body=body, request_options=request_options
        ).unwrap()

    def post_payment_links(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentLinkRequest | PaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentLinkResponse:
        """Creates a payment link to a `Pay by Link <https://docs.adyen.com/unified-commerce/pay-by-link/>`__ page where
        the shopper can pay. The list of payment methods presented to the shopper depends on the ``currency`` and
        ``country`` parameters sent in the request.

        For more information, refer to `Pay by Link documentation
        <https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_payment_links(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentLinksWithRawResponse:
        return self._with_raw_response


class AsyncPaymentLinks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentLinksWithRawResponse(client, server, auth)

    async def get_payment_links_link_id(
        self, link_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentLinkResponse:
        """Retrieves the payment link details using the payment link ``id``.

        Args:
            link_id: Unique identifier of the payment link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.get_payment_links_link_id(link_id, request_options=request_options)
        ).unwrap()

    async def patch_payment_links_link_id(
        self,
        link_id: str,
        *,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentLinkResponse:
        """Updates the status of a payment link. Use this endpoint to `force the expiry of a payment link
        <https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status>`__.

        Args:
            link_id: Unique identifier of the payment link.
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
            await self._with_raw_response.patch_payment_links_link_id(
                link_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payment_links(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentLinkRequest | PaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentLinkResponse:
        """Creates a payment link to a `Pay by Link <https://docs.adyen.com/unified-commerce/pay-by-link/>`__ page where
        the shopper can pay. The list of payment methods presented to the shopper depends on the ``currency`` and
        ``country`` parameters sent in the request.

        For more information, refer to `Pay by Link documentation
        <https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payment_links(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentLinksWithRawResponse:
        return self._with_raw_response


class PaymentLinksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_payment_links_link_id(
        self, link_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentLinkResponse, GetPaymentLinksLinkIdErrorBody]:
        """Retrieves the payment link details using the payment link ``id``.

        Args:
            link_id: Unique identifier of the payment link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/paymentLinks/{linkId}"),
            path_params=[param[str]("linkId", link_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=get_payment_links_link_id_error_mapper,
            request_options=request_options,
        )

    def patch_payment_links_link_id(
        self,
        link_id: str,
        *,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentLinkResponse, PatchPaymentLinksLinkIdErrorBody]:
        """Updates the status of a payment link. Use this endpoint to `force the expiry of a payment link
        <https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status>`__.

        Args:
            link_id: Unique identifier of the payment link.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/paymentLinks/{linkId}"),
            path_params=[param[str]("linkId", link_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=patch_payment_links_link_id_error_mapper,
            request_options=request_options,
        )

    def post_payment_links(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentLinkRequest | PaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentLinkResponse, PostPaymentLinksErrorBody]:
        """Creates a payment link to a `Pay by Link <https://docs.adyen.com/unified-commerce/pay-by-link/>`__ page where
        the shopper can pay. The list of payment methods presented to the shopper depends on the ``currency`` and
        ``country`` parameters sent in the request.

        For more information, refer to `Pay by Link documentation
        <https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentLinks"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentLinkRequest | PaymentLinkRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=post_payment_links_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentLinksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_payment_links_link_id(
        self, link_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentLinkResponse, GetPaymentLinksLinkIdErrorBody]:
        """Retrieves the payment link details using the payment link ``id``.

        Args:
            link_id: Unique identifier of the payment link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/paymentLinks/{linkId}"),
            path_params=[param[str]("linkId", link_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=get_payment_links_link_id_error_mapper,
            request_options=request_options,
        )

    async def patch_payment_links_link_id(
        self,
        link_id: str,
        *,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentLinkResponse, PatchPaymentLinksLinkIdErrorBody]:
        """Updates the status of a payment link. Use this endpoint to `force the expiry of a payment link
        <https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status>`__.

        Args:
            link_id: Unique identifier of the payment link.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/paymentLinks/{linkId}"),
            path_params=[param[str]("linkId", link_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=patch_payment_links_link_id_error_mapper,
            request_options=request_options,
        )

    async def post_payment_links(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaymentLinkRequest | PaymentLinkRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentLinkResponse, PostPaymentLinksErrorBody]:
        """Creates a payment link to a `Pay by Link <https://docs.adyen.com/unified-commerce/pay-by-link/>`__ page where
        the shopper can pay. The list of payment methods presented to the shopper depends on the ``currency`` and
        ``country`` parameters sent in the request.

        For more information, refer to `Pay by Link documentation
        <https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentLinks"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaymentLinkRequest | PaymentLinkRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentLinkResponse],
            error_mapper=post_payment_links_error_mapper,
            request_options=request_options,
        )
