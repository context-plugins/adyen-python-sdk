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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_network_tokens_network_token_id_error import (
    GetNetworkTokensNetworkTokenIdErrorBody,
    get_network_tokens_network_token_id_error_mapper,
)
from ..errors.patch_network_tokens_network_token_id_error import (
    PatchNetworkTokensNetworkTokenIdErrorBody,
    patch_network_tokens_network_token_id_error_mapper,
)
from ..models.get_network_token_response import GetNetworkTokenResponse
from ..models.update_network_token_request import UpdateNetworkTokenRequest, UpdateNetworkTokenRequestDict
from ..server.server import Server


class NetworkTokens:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NetworkTokensWithRawResponse(client, server, auth)

    def get_network_tokens_network_token_id(
        self, network_token_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetNetworkTokenResponse:
        """Returns the details of a network token.

        Args:
            network_token_id: The unique identifier of the network token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_network_tokens_network_token_id(
            network_token_id, request_options=request_options
        ).unwrap()

    def patch_network_tokens_network_token_id(
        self,
        network_token_id: str,
        *,
        body: UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the status of the network token.

        Args:
            network_token_id: The unique identifier of the network token.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_network_tokens_network_token_id(
            network_token_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NetworkTokensWithRawResponse:
        return self._with_raw_response


class AsyncNetworkTokens:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNetworkTokensWithRawResponse(client, server, auth)

    async def get_network_tokens_network_token_id(
        self, network_token_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetNetworkTokenResponse:
        """Returns the details of a network token.

        Args:
            network_token_id: The unique identifier of the network token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_network_tokens_network_token_id(
                network_token_id, request_options=request_options
            )
        ).unwrap()

    async def patch_network_tokens_network_token_id(
        self,
        network_token_id: str,
        *,
        body: UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the status of the network token.

        Args:
            network_token_id: The unique identifier of the network token.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_network_tokens_network_token_id(
                network_token_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNetworkTokensWithRawResponse:
        return self._with_raw_response


class NetworkTokensWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_network_tokens_network_token_id(
        self, network_token_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetNetworkTokenResponse, GetNetworkTokensNetworkTokenIdErrorBody]:
        """Returns the details of a network token.

        Args:
            network_token_id: The unique identifier of the network token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/networkTokens/{networkTokenId}"),
            path_params=[param[str]("networkTokenId", network_token_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNetworkTokenResponse],
            error_mapper=get_network_tokens_network_token_id_error_mapper,
            request_options=request_options,
        )

    def patch_network_tokens_network_token_id(
        self,
        network_token_id: str,
        *,
        body: UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchNetworkTokensNetworkTokenIdErrorBody]:
        """Updates the status of the network token.

        Args:
            network_token_id: The unique identifier of the network token.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/networkTokens/{networkTokenId}"),
            path_params=[param[str]("networkTokenId", network_token_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=patch_network_tokens_network_token_id_error_mapper,
            request_options=request_options,
        )


class AsyncNetworkTokensWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_network_tokens_network_token_id(
        self, network_token_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetNetworkTokenResponse, GetNetworkTokensNetworkTokenIdErrorBody]:
        """Returns the details of a network token.

        Args:
            network_token_id: The unique identifier of the network token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/networkTokens/{networkTokenId}"),
            path_params=[param[str]("networkTokenId", network_token_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNetworkTokenResponse],
            error_mapper=get_network_tokens_network_token_id_error_mapper,
            request_options=request_options,
        )

    async def patch_network_tokens_network_token_id(
        self,
        network_token_id: str,
        *,
        body: UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchNetworkTokensNetworkTokenIdErrorBody]:
        """Updates the status of the network token.

        Args:
            network_token_id: The unique identifier of the network token.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/networkTokens/{networkTokenId}"),
            path_params=[param[str]("networkTokenId", network_token_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateNetworkTokenRequest | UpdateNetworkTokenRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=patch_network_tokens_network_token_id_error_mapper,
            request_options=request_options,
        )
