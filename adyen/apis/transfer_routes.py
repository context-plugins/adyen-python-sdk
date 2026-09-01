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
from ..errors.post_transfer_routes_calculate_error import (
    PostTransferRoutesCalculateErrorBody,
    post_transfer_routes_calculate_error_mapper,
)
from ..models.transfer_route_request import TransferRouteRequest, TransferRouteRequestDict
from ..models.transfer_route_response import TransferRouteResponse
from ..server.server import Server


class TransferRoutes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransferRoutesWithRawResponse(client, server, auth)

    def post_transfer_routes_calculate(
        self,
        *,
        body: TransferRouteRequest | TransferRouteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferRouteResponse:
        """Returns available transfer routes based on a combination of transfer ``country``, ``currency``,
        ``counterparty``, and ``priorities``. Use this endpoint to find optimal transfer priorities and associated
        requirements before you `make a transfer
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.post_transfer_routes_calculate(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TransferRoutesWithRawResponse:
        return self._with_raw_response


class AsyncTransferRoutes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransferRoutesWithRawResponse(client, server, auth)

    async def post_transfer_routes_calculate(
        self,
        *,
        body: TransferRouteRequest | TransferRouteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferRouteResponse:
        """Returns available transfer routes based on a combination of transfer ``country``, ``currency``,
        ``counterparty``, and ``priorities``. Use this endpoint to find optimal transfer priorities and associated
        requirements before you `make a transfer
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_transfer_routes_calculate(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransferRoutesWithRawResponse:
        return self._with_raw_response


class TransferRoutesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_transfer_routes_calculate(
        self,
        *,
        body: TransferRouteRequest | TransferRouteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferRouteResponse, PostTransferRoutesCalculateErrorBody]:
        """Returns available transfer routes based on a combination of transfer ``country``, ``currency``,
        ``counterparty``, and ``priorities``. Use this endpoint to find optimal transfer priorities and associated
        requirements before you `make a transfer
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/transferRoutes/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferRouteRequest | TransferRouteRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferRouteResponse],
            error_mapper=post_transfer_routes_calculate_error_mapper,
            request_options=request_options,
        )


class AsyncTransferRoutesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_transfer_routes_calculate(
        self,
        *,
        body: TransferRouteRequest | TransferRouteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferRouteResponse, PostTransferRoutesCalculateErrorBody]:
        """Returns available transfer routes based on a combination of transfer ``country``, ``currency``,
        ``counterparty``, and ``priorities``. Use this endpoint to find optimal transfer priorities and associated
        requirements before you `make a transfer
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/transferRoutes/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferRouteRequest | TransferRouteRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferRouteResponse],
            error_mapper=post_transfer_routes_calculate_error_mapper,
            request_options=request_options,
        )
