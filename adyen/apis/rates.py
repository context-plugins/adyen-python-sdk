from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.post_rates_calculate_error import PostRatesCalculateErrorBody, post_rates_calculate_error_mapper
from ..models.calculate_rate_request import CalculateRateRequest, CalculateRateRequestDict
from ..models.calculate_rate_response import CalculateRateResponse
from ..server.server import Server


class Rates:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = RatesWithRawResponse(client, server)

    def post_rates_calculate(
        self,
        body: CalculateRateRequest | CalculateRateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateRateResponse:
        """Returns the calculated amounts and rates required to convert the currency of a transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_rates_calculate(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> RatesWithRawResponse:
        return self._with_raw_response


class AsyncRates:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncRatesWithRawResponse(client, server)

    async def post_rates_calculate(
        self,
        body: CalculateRateRequest | CalculateRateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateRateResponse:
        """Returns the calculated amounts and rates required to convert the currency of a transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.post_rates_calculate(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncRatesWithRawResponse:
        return self._with_raw_response


class RatesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_rates_calculate(
        self,
        body: CalculateRateRequest | CalculateRateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateRateResponse, PostRatesCalculateErrorBody]:
        """Returns the calculated amounts and rates required to convert the currency of a transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/rates/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateRateRequest | CalculateRateRequestDict](body),
            decoder=json_decoder[CalculateRateResponse],
            error_mapper=post_rates_calculate_error_mapper,
            request_options=request_options,
        )


class AsyncRatesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_rates_calculate(
        self,
        body: CalculateRateRequest | CalculateRateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateRateResponse, PostRatesCalculateErrorBody]:
        """Returns the calculated amounts and rates required to convert the currency of a transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/rates/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateRateRequest | CalculateRateRequestDict](body),
            decoder=json_decoder[CalculateRateResponse],
            error_mapper=post_rates_calculate_error_mapper,
            request_options=request_options,
        )
