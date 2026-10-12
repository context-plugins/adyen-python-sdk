from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.post_cashouts_error import PostCashoutsErrorBody, post_cashouts_error_mapper
from ..models.cash_out import CashOut
from ..models.cash_out_info import CashOutInfo, CashOutInfoDict
from ..server.server import Server


class CashOutApi:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = CashOutApiWithRawResponse(client, server)

    def post_cashouts(
        self, body: CashOutInfo | CashOutInfoDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CashOut:
        """Initiates a `cashout <https://docs.adyen.com/platforms/cash-out-instantly>`__ request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid. Forbidden - The API credential does not have the right
                permissions. Not Found - The requested resource was not found. Unprocessable Entity - A request
                validation error. Too Many Requests - Request rate limit exceeded. Internal Service Error - An
                unrecoverable error occurred while trying to perform the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_cashouts(body, request_options=request_options))

    @property
    def with_raw_response(self) -> CashOutApiWithRawResponse:
        return self._with_raw_response


class AsyncCashOutApi:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncCashOutApiWithRawResponse(client, server)

    async def post_cashouts(
        self, body: CashOutInfo | CashOutInfoDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CashOut:
        """Initiates a `cashout <https://docs.adyen.com/platforms/cash-out-instantly>`__ request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid. Forbidden - The API credential does not have the right
                permissions. Not Found - The requested resource was not found. Unprocessable Entity - A request
                validation error. Too Many Requests - Request rate limit exceeded. Internal Service Error - An
                unrecoverable error occurred while trying to perform the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_cashouts(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncCashOutApiWithRawResponse:
        return self._with_raw_response


class CashOutApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_cashouts(
        self, body: CashOutInfo | CashOutInfoDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CashOut, PostCashoutsErrorBody]:
        """Initiates a `cashout <https://docs.adyen.com/platforms/cash-out-instantly>`__ request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/cashouts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CashOutInfo | CashOutInfoDict](body),
            decoder=json_decoder[CashOut],
            error_mapper=post_cashouts_error_mapper,
            request_options=request_options,
        )


class AsyncCashOutApiWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_cashouts(
        self, body: CashOutInfo | CashOutInfoDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CashOut, PostCashoutsErrorBody]:
        """Initiates a `cashout <https://docs.adyen.com/platforms/cash-out-instantly>`__ request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/cashouts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CashOutInfo | CashOutInfoDict](body),
            decoder=async_json_decoder[CashOut],
            error_mapper=post_cashouts_error_mapper,
            request_options=request_options,
        )
