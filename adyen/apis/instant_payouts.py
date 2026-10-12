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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.post_payout_error import PostPayoutErrorBody, post_payout_error_mapper
from ..models.payout_request import PayoutRequest, PayoutRequestDict
from ..models.payout_response import PayoutResponse
from ..server.server import Server


class InstantPayouts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InstantPayoutsWithRawResponse(client, server, auth)

    def post_payout(
        self,
        *,
        body: PayoutRequest | PayoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the POST `/transfers
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ endpoint instead.
        > - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the
            Transfers API.
        >
        > With the Transfers API, you can:
        > - Handle multiple payout use cases with a single API.
        > - Use new payout functionalities, such as instant payouts to bank accounts.
        > - Receive webhooks with more details and defined transfer states.
        >
        > For more information about the payout features of the Transfers API, see our `Payouts
            <https://docs.adyen.com/payouts/payout-service>`__ documentation.

        With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the
        cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card
        payouts are only supported for Visa and Mastercard cards.

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
        return unwrap(self._with_raw_response.post_payout(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> InstantPayoutsWithRawResponse:
        return self._with_raw_response


class AsyncInstantPayouts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInstantPayoutsWithRawResponse(client, server, auth)

    async def post_payout(
        self,
        *,
        body: PayoutRequest | PayoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the POST `/transfers
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ endpoint instead.
        > - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the
            Transfers API.
        >
        > With the Transfers API, you can:
        > - Handle multiple payout use cases with a single API.
        > - Use new payout functionalities, such as instant payouts to bank accounts.
        > - Receive webhooks with more details and defined transfer states.
        >
        > For more information about the payout features of the Transfers API, see our `Payouts
            <https://docs.adyen.com/payouts/payout-service>`__ documentation.

        With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the
        cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card
        payouts are only supported for Visa and Mastercard cards.

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
        return unwrap(await self._with_raw_response.post_payout(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncInstantPayoutsWithRawResponse:
        return self._with_raw_response


class InstantPayoutsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_payout(
        self,
        *,
        body: PayoutRequest | PayoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutResponse, PostPayoutErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the POST `/transfers
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ endpoint instead.
        > - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the
            Transfers API.
        >
        > With the Transfers API, you can:
        > - Handle multiple payout use cases with a single API.
        > - Use new payout functionalities, such as instant payouts to bank accounts.
        > - Receive webhooks with more details and defined transfer states.
        >
        > For more information about the payout features of the Transfers API, see our `Payouts
            <https://docs.adyen.com/payouts/payout-service>`__ documentation.

        With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the
        cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card
        payouts are only supported for Visa and Mastercard cards.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/payout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutRequest | PayoutRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutResponse],
            error_mapper=post_payout_error_mapper,
            request_options=request_options,
        )


class AsyncInstantPayoutsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_payout(
        self,
        *,
        body: PayoutRequest | PayoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutResponse, PostPayoutErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the POST `/transfers
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ endpoint instead.
        > - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the
            Transfers API.
        >
        > With the Transfers API, you can:
        > - Handle multiple payout use cases with a single API.
        > - Use new payout functionalities, such as instant payouts to bank accounts.
        > - Receive webhooks with more details and defined transfer states.
        >
        > For more information about the payout features of the Transfers API, see our `Payouts
            <https://docs.adyen.com/payouts/payout-service>`__ documentation.

        With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the
        cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card
        payouts are only supported for Visa and Mastercard cards.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/payout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutRequest | PayoutRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PayoutResponse],
            error_mapper=post_payout_error_mapper,
            request_options=request_options,
        )
