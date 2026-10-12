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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error import (
    DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody,
    delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error import (
    GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody,
    get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
)
from ..errors.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error import (
    GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody,
    get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error import (
    PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody,
    post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
)
from ..models.allowed_origin import AllowedOrigin, AllowedOriginDict
from ..models.allowed_origins_response import AllowedOriginsResponse
from ..server.server import Server


class AllowedOriginsMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AllowedOriginsMerchantLevelWithRawResponse(client, server, auth)

    def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
                merchant_id, api_credential_id, origin_id, request_options=request_options
            ),
        )

    def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AllowedOriginsResponse:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ for the API
        credential identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
                merchant_id, api_credential_id, request_options=request_options
            ),
        )

    def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Returns the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
                merchant_id, api_credential_id, origin_id, request_options=request_options
            ),
        )

    def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: AllowedOrigin | AllowedOriginDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Adds a new `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ to the API
        credential's list of allowed origins.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
                merchant_id, api_credential_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AllowedOriginsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncAllowedOriginsMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAllowedOriginsMerchantLevelWithRawResponse(client, server, auth)

    async def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
                merchant_id, api_credential_id, origin_id, request_options=request_options
            ),
        )

    async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AllowedOriginsResponse:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ for the API
        credential identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
                merchant_id, api_credential_id, request_options=request_options
            ),
        )

    async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Returns the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
                merchant_id, api_credential_id, origin_id, request_options=request_options
            ),
        )

    async def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: AllowedOrigin | AllowedOriginDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Adds a new `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ to the API
        credential's list of allowed origins.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
                merchant_id, api_credential_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncAllowedOriginsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AllowedOriginsMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("apiCredentialId", api_credential_id),
                param[str]("originId", origin_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOriginsResponse, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ for the API
        credential identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOriginsResponse],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]:
        """Returns the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("apiCredentialId", api_credential_id),
                param[str]("originId", origin_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: AllowedOrigin | AllowedOriginDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]:
        """Adds a new `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ to the API
        credential's list of allowed origins.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AllowedOrigin | AllowedOriginDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
            request_options=request_options,
        )


class AsyncAllowedOriginsMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("apiCredentialId", api_credential_id),
                param[str]("originId", origin_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOriginsResponse, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ for the API
        credential identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AllowedOriginsResponse],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        origin_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]:
        """Returns the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ identified in the
        path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("apiCredentialId", api_credential_id),
                param[str]("originId", origin_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AllowedOrigin],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: AllowedOrigin | AllowedOriginDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]:
        """Adds a new `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ to the API
        credential's list of allowed origins.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AllowedOrigin | AllowedOriginDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AllowedOrigin],
            error_mapper=post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error_mapper,
            request_options=request_options,
        )
