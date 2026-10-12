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
from ..errors.post_balance_transfers_error import PostBalanceTransfersErrorBody, post_balance_transfers_error_mapper
from ..models.balance_transfer_request import BalanceTransferRequest, BalanceTransferRequestDict
from ..models.balance_transfer_response import BalanceTransferResponse
from ..server.server import Server


class BalanceTransfers:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = BalanceTransfersWithRawResponse(client, server)

    def post_balance_transfers(
        self,
        body: BalanceTransferRequest | BalanceTransferRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceTransferResponse:
        r"""Performs a balance transfer between merchant accounts. The following conditions must be met before you can
        successfully transfer balances:
        * The source and destination merchant accounts must be under the same company account and legal entity.
        * The source merchant account must have sufficient funds.
        * The source and destination merchant accounts must have at least one common processing currency.\n\n
        When sending multiple API requests with the same source and destination merchant accounts, send the requests
        sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized Unprocessable Content - A request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_balance_transfers(body, request_options=request_options))

    @property
    def with_raw_response(self) -> BalanceTransfersWithRawResponse:
        return self._with_raw_response


class AsyncBalanceTransfers:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncBalanceTransfersWithRawResponse(client, server)

    async def post_balance_transfers(
        self,
        body: BalanceTransferRequest | BalanceTransferRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceTransferResponse:
        r"""Performs a balance transfer between merchant accounts. The following conditions must be met before you can
        successfully transfer balances:
        * The source and destination merchant accounts must be under the same company account and legal entity.
        * The source merchant account must have sufficient funds.
        * The source and destination merchant accounts must have at least one common processing currency.\n\n
        When sending multiple API requests with the same source and destination merchant accounts, send the requests
        sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized Unprocessable Content - A request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_balance_transfers(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncBalanceTransfersWithRawResponse:
        return self._with_raw_response


class BalanceTransfersWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_balance_transfers(
        self,
        body: BalanceTransferRequest | BalanceTransferRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceTransferResponse, PostBalanceTransfersErrorBody]:
        r"""Performs a balance transfer between merchant accounts. The following conditions must be met before you can
        successfully transfer balances:
        * The source and destination merchant accounts must be under the same company account and legal entity.
        * The source merchant account must have sufficient funds.
        * The source and destination merchant accounts must have at least one common processing currency.\n\n
        When sending multiple API requests with the same source and destination merchant accounts, send the requests
        sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/balanceTransfers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceTransferRequest | BalanceTransferRequestDict](body),
            decoder=json_decoder[BalanceTransferResponse],
            error_mapper=post_balance_transfers_error_mapper,
            request_options=request_options,
        )


class AsyncBalanceTransfersWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_balance_transfers(
        self,
        body: BalanceTransferRequest | BalanceTransferRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceTransferResponse, PostBalanceTransfersErrorBody]:
        r"""Performs a balance transfer between merchant accounts. The following conditions must be met before you can
        successfully transfer balances:
        * The source and destination merchant accounts must be under the same company account and legal entity.
        * The source merchant account must have sufficient funds.
        * The source and destination merchant accounts must have at least one common processing currency.\n\n
        When sending multiple API requests with the same source and destination merchant accounts, send the requests
        sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/balanceTransfers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceTransferRequest | BalanceTransferRequestDict](body),
            decoder=async_json_decoder[BalanceTransferResponse],
            error_mapper=post_balance_transfers_error_mapper,
            request_options=request_options,
        )
