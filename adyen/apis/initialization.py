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
from ..errors.post_store_detail_and_submit_third_party_error import (
    PostStoreDetailAndSubmitThirdPartyErrorBody,
    post_store_detail_and_submit_third_party_error_mapper,
)
from ..errors.post_store_detail_error import PostStoreDetailErrorBody, post_store_detail_error_mapper
from ..errors.post_submit_third_party_error import PostSubmitThirdPartyErrorBody, post_submit_third_party_error_mapper
from ..models.store_detail_and_submit_request import StoreDetailAndSubmitRequest, StoreDetailAndSubmitRequestDict
from ..models.store_detail_and_submit_response import StoreDetailAndSubmitResponse
from ..models.store_detail_request import StoreDetailRequest, StoreDetailRequestDict
from ..models.store_detail_response import StoreDetailResponse
from ..models.submit_request import SubmitRequest, SubmitRequestDict
from ..models.submit_response import SubmitResponse
from ..server.server import Server


class Initialization:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InitializationWithRawResponse(client, server, auth)

    def post_store_detail(
        self,
        *,
        body: StoreDetailRequest | StoreDetailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoreDetailResponse:
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

        Stores payment details under the ``PAYOUT`` recurring contract. These payment details can be used later to
        submit a payout via the ``/submitThirdParty`` call.

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
        return self._with_raw_response.post_store_detail(body=body, request_options=request_options).unwrap()

    def post_store_detail_and_submit_third_party(
        self,
        *,
        body: StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoreDetailAndSubmitResponse:
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

        Submits a payout and stores its details for subsequent payouts.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

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
        return self._with_raw_response.post_store_detail_and_submit_third_party(
            body=body, request_options=request_options
        ).unwrap()

    def post_submit_third_party(
        self,
        *,
        body: SubmitRequest | SubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubmitResponse:
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

        Submits a payout using the previously stored payment details. To store payment details, use the ``/storeDetail``
        API call.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

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
        return self._with_raw_response.post_submit_third_party(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InitializationWithRawResponse:
        return self._with_raw_response


class AsyncInitialization:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInitializationWithRawResponse(client, server, auth)

    async def post_store_detail(
        self,
        *,
        body: StoreDetailRequest | StoreDetailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoreDetailResponse:
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

        Stores payment details under the ``PAYOUT`` recurring contract. These payment details can be used later to
        submit a payout via the ``/submitThirdParty`` call.

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
        return (await self._with_raw_response.post_store_detail(body=body, request_options=request_options)).unwrap()

    async def post_store_detail_and_submit_third_party(
        self,
        *,
        body: StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoreDetailAndSubmitResponse:
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

        Submits a payout and stores its details for subsequent payouts.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

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
            await self._with_raw_response.post_store_detail_and_submit_third_party(
                body=body, request_options=request_options
            )
        ).unwrap()

    async def post_submit_third_party(
        self,
        *,
        body: SubmitRequest | SubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubmitResponse:
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

        Submits a payout using the previously stored payment details. To store payment details, use the ``/storeDetail``
        API call.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

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
            await self._with_raw_response.post_submit_third_party(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInitializationWithRawResponse:
        return self._with_raw_response


class InitializationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_store_detail(
        self,
        *,
        body: StoreDetailRequest | StoreDetailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoreDetailResponse, PostStoreDetailErrorBody]:
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

        Stores payment details under the ``PAYOUT`` recurring contract. These payment details can be used later to
        submit a payout via the ``/submitThirdParty`` call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/storeDetail"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreDetailRequest | StoreDetailRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoreDetailResponse],
            error_mapper=post_store_detail_error_mapper,
            request_options=request_options,
        )

    def post_store_detail_and_submit_third_party(
        self,
        *,
        body: StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoreDetailAndSubmitResponse, PostStoreDetailAndSubmitThirdPartyErrorBody]:
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

        Submits a payout and stores its details for subsequent payouts.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/storeDetailAndSubmitThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoreDetailAndSubmitResponse],
            error_mapper=post_store_detail_and_submit_third_party_error_mapper,
            request_options=request_options,
        )

    def post_submit_third_party(
        self,
        *,
        body: SubmitRequest | SubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubmitResponse, PostSubmitThirdPartyErrorBody]:
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

        Submits a payout using the previously stored payment details. To store payment details, use the ``/storeDetail``
        API call.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/submitThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitRequest | SubmitRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SubmitResponse],
            error_mapper=post_submit_third_party_error_mapper,
            request_options=request_options,
        )


class AsyncInitializationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_store_detail(
        self,
        *,
        body: StoreDetailRequest | StoreDetailRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoreDetailResponse, PostStoreDetailErrorBody]:
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

        Stores payment details under the ``PAYOUT`` recurring contract. These payment details can be used later to
        submit a payout via the ``/submitThirdParty`` call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/storeDetail"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreDetailRequest | StoreDetailRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoreDetailResponse],
            error_mapper=post_store_detail_error_mapper,
            request_options=request_options,
        )

    async def post_store_detail_and_submit_third_party(
        self,
        *,
        body: StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoreDetailAndSubmitResponse, PostStoreDetailAndSubmitThirdPartyErrorBody]:
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

        Submits a payout and stores its details for subsequent payouts.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/storeDetailAndSubmitThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoreDetailAndSubmitResponse],
            error_mapper=post_store_detail_and_submit_third_party_error_mapper,
            request_options=request_options,
        )

    async def post_submit_third_party(
        self,
        *,
        body: SubmitRequest | SubmitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubmitResponse, PostSubmitThirdPartyErrorBody]:
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

        Submits a payout using the previously stored payment details. To store payment details, use the ``/storeDetail``
        API call.

        The submitted payout must be confirmed or declined either by a reviewer or via ``/confirmThirdParty`` or
        ``/declineThirdParty`` calls.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default3("/submitThirdParty"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitRequest | SubmitRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SubmitResponse],
            error_mapper=post_submit_third_party_error_mapper,
            request_options=request_options,
        )
