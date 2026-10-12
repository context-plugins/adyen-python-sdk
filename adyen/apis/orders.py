from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.post_orders_cancel_error import PostOrdersCancelErrorBody, post_orders_cancel_error_mapper
from ..errors.post_orders_error import PostOrdersErrorBody, post_orders_error_mapper
from ..errors.post_payment_methods_balance_error import (
    PostPaymentMethodsBalanceErrorBody,
    post_payment_methods_balance_error_mapper,
)
from ..models.balance_check_request import BalanceCheckRequest, BalanceCheckRequestDict
from ..models.balance_check_response import BalanceCheckResponse
from ..models.cancel_order_request import CancelOrderRequest, CancelOrderRequestDict
from ..models.cancel_order_response import CancelOrderResponse
from ..models.create_order_request import CreateOrderRequest, CreateOrderRequestDict
from ..models.create_order_response import CreateOrderResponse
from ..server.server import Server


class Orders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrdersWithRawResponse(client, server, auth)

    def post_orders(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateOrderRequest | CreateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateOrderResponse:
        """Creates an order to be used for partial payments. Make a POST ``/orders`` call before making a ``/payments``
        call when processing payments with different payment methods.

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
            self._with_raw_response.post_orders(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_orders_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelOrderRequest | CancelOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelOrderResponse:
        """Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the
        order, either by canceling or refunding the payment, depending on the type of payment method.

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
            self._with_raw_response.post_orders_cancel(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_payment_methods_balance(
        self,
        *,
        idempotency_key: str | None = None,
        body: BalanceCheckRequest | BalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceCheckResponse:
        """Retrieves the balance remaining on a shopper's gift card. To check a gift card's balance, make a POST
        ``/paymentMethods/balance`` call and include the gift card's details inside a ``paymentMethod`` object.

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
            self._with_raw_response.post_payment_methods_balance(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return self._with_raw_response


class AsyncOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrdersWithRawResponse(client, server, auth)

    async def post_orders(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateOrderRequest | CreateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateOrderResponse:
        """Creates an order to be used for partial payments. Make a POST ``/orders`` call before making a ``/payments``
        call when processing payments with different payment methods.

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
            await self._with_raw_response.post_orders(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_orders_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelOrderRequest | CancelOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelOrderResponse:
        """Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the
        order, either by canceling or refunding the payment, depending on the type of payment method.

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
            await self._with_raw_response.post_orders_cancel(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_payment_methods_balance(
        self,
        *,
        idempotency_key: str | None = None,
        body: BalanceCheckRequest | BalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceCheckResponse:
        """Retrieves the balance remaining on a shopper's gift card. To check a gift card's balance, make a POST
        ``/paymentMethods/balance`` call and include the gift card's details inside a ``paymentMethod`` object.

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
            await self._with_raw_response.post_payment_methods_balance(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return self._with_raw_response


class OrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_orders(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateOrderRequest | CreateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateOrderResponse, PostOrdersErrorBody]:
        """Creates an order to be used for partial payments. Make a POST ``/orders`` call before making a ``/payments``
        call when processing payments with different payment methods.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/orders"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CreateOrderRequest | CreateOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateOrderResponse],
            error_mapper=post_orders_error_mapper,
            request_options=request_options,
        )

    def post_orders_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelOrderRequest | CancelOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelOrderResponse, PostOrdersCancelErrorBody]:
        """Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the
        order, either by canceling or refunding the payment, depending on the type of payment method.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/orders/cancel"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CancelOrderRequest | CancelOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CancelOrderResponse],
            error_mapper=post_orders_cancel_error_mapper,
            request_options=request_options,
        )

    def post_payment_methods_balance(
        self,
        *,
        idempotency_key: str | None = None,
        body: BalanceCheckRequest | BalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceCheckResponse, PostPaymentMethodsBalanceErrorBody]:
        """Retrieves the balance remaining on a shopper's gift card. To check a gift card's balance, make a POST
        ``/paymentMethods/balance`` call and include the gift card's details inside a ``paymentMethod`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentMethods/balance"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[BalanceCheckRequest | BalanceCheckRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceCheckResponse],
            error_mapper=post_payment_methods_balance_error_mapper,
            request_options=request_options,
        )


class AsyncOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_orders(
        self,
        *,
        idempotency_key: str | None = None,
        body: CreateOrderRequest | CreateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateOrderResponse, PostOrdersErrorBody]:
        """Creates an order to be used for partial payments. Make a POST ``/orders`` call before making a ``/payments``
        call when processing payments with different payment methods.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/orders"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CreateOrderRequest | CreateOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CreateOrderResponse],
            error_mapper=post_orders_error_mapper,
            request_options=request_options,
        )

    async def post_orders_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelOrderRequest | CancelOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelOrderResponse, PostOrdersCancelErrorBody]:
        """Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the
        order, either by canceling or refunding the payment, depending on the type of payment method.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/orders/cancel"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CancelOrderRequest | CancelOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CancelOrderResponse],
            error_mapper=post_orders_cancel_error_mapper,
            request_options=request_options,
        )

    async def post_payment_methods_balance(
        self,
        *,
        idempotency_key: str | None = None,
        body: BalanceCheckRequest | BalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceCheckResponse, PostPaymentMethodsBalanceErrorBody]:
        """Retrieves the balance remaining on a shopper's gift card. To check a gift card's balance, make a POST
        ``/paymentMethods/balance`` call and include the gift card's details inside a ``paymentMethod`` object.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paymentMethods/balance"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[BalanceCheckRequest | BalanceCheckRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[BalanceCheckResponse],
            error_mapper=post_payment_methods_balance_error_mapper,
            request_options=request_options,
        )
