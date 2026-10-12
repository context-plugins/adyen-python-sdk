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
from ..errors.post_confirm_third_party_error import (
    PostConfirmThirdPartyErrorBody,
    post_confirm_third_party_error_mapper,
)
from ..errors.post_decline_third_party_error import (
    PostDeclineThirdPartyErrorBody,
    post_decline_third_party_error_mapper,
)
from ..models.modify_request import ModifyRequest, ModifyRequestDict
from ..models.modify_response import ModifyResponse
from ..server.server import Server


class Reviewing:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReviewingWithRawResponse(client, server, auth)

    def post_confirm_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifyResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Confirms a previously submitted payout.

        To cancel a payout, use the ``/declineThirdParty`` endpoint.

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
        return unwrap(self._with_raw_response.post_confirm_third_party(body=body, request_options=request_options))

    def post_decline_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifyResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Cancels a previously submitted payout.

        To confirm and send a payout, use the ``/confirmThirdParty`` endpoint.

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
        return unwrap(self._with_raw_response.post_decline_third_party(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> ReviewingWithRawResponse:
        return self._with_raw_response


class AsyncReviewing:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReviewingWithRawResponse(client, server, auth)

    async def post_confirm_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifyResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Confirms a previously submitted payout.

        To cancel a payout, use the ``/declineThirdParty`` endpoint.

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
            await self._with_raw_response.post_confirm_third_party(body=body, request_options=request_options)
        )

    async def post_decline_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifyResponse:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Cancels a previously submitted payout.

        To confirm and send a payout, use the ``/confirmThirdParty`` endpoint.

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
            await self._with_raw_response.post_decline_third_party(body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncReviewingWithRawResponse:
        return self._with_raw_response


class ReviewingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_confirm_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifyResponse, PostConfirmThirdPartyErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Confirms a previously submitted payout.

        To cancel a payout, use the ``/declineThirdParty`` endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/confirmThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifyRequest | ModifyRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModifyResponse],
            error_mapper=post_confirm_third_party_error_mapper,
            request_options=request_options,
        )

    def post_decline_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifyResponse, PostDeclineThirdPartyErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Cancels a previously submitted payout.

        To confirm and send a payout, use the ``/confirmThirdParty`` endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/declineThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifyRequest | ModifyRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ModifyResponse],
            error_mapper=post_decline_third_party_error_mapper,
            request_options=request_options,
        )


class AsyncReviewingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_confirm_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifyResponse, PostConfirmThirdPartyErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Confirms a previously submitted payout.

        To cancel a payout, use the ``/declineThirdParty`` endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/confirmThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifyRequest | ModifyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ModifyResponse],
            error_mapper=post_confirm_third_party_error_mapper,
            request_options=request_options,
        )

    async def post_decline_third_party(
        self,
        *,
        body: ModifyRequest | ModifyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifyResponse, PostDeclineThirdPartyErrorBody]:
        """> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
        >- If you are building a new integration, use the `Transfers API
        <https://docs.adyen.com/api-explorer/transfers/latest/overview>`__ instead.
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

        Cancels a previously submitted payout.

        To confirm and send a payout, use the ``/confirmThirdParty`` endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/declineThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifyRequest | ModifyRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ModifyResponse],
            error_mapper=post_decline_third_party_error_mapper,
            request_options=request_options,
        )
