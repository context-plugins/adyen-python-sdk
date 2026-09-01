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
from ..errors.delete_me_allowed_origins_origin_id_error import (
    DeleteMeAllowedOriginsOriginIdErrorBody,
    delete_me_allowed_origins_origin_id_error_mapper,
)
from ..errors.get_me_allowed_origins_error import GetMeAllowedOriginsErrorBody, get_me_allowed_origins_error_mapper
from ..errors.get_me_allowed_origins_origin_id_error import (
    GetMeAllowedOriginsOriginIdErrorBody,
    get_me_allowed_origins_origin_id_error_mapper,
)
from ..errors.get_me_error import GetMeErrorBody, get_me_error_mapper
from ..errors.post_me_allowed_origins_error import PostMeAllowedOriginsErrorBody, post_me_allowed_origins_error_mapper
from ..errors.post_me_generate_client_key_error import (
    PostMeGenerateClientKeyErrorBody,
    post_me_generate_client_key_error_mapper,
)
from ..models.allowed_origin import AllowedOrigin
from ..models.allowed_origins_response import AllowedOriginsResponse
from ..models.create_allowed_origin_request import CreateAllowedOriginRequest, CreateAllowedOriginRequestDict
from ..models.generate_client_key_response import GenerateClientKeyResponse
from ..models.me_api_credential import MeApiCredential
from ..server.server import Server


class MyApiCredential:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MyApiCredentialWithRawResponse(client, server, auth)

    def delete_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_me_allowed_origins_origin_id(
            origin_id, request_options=request_options
        ).unwrap()

    def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> MeApiCredential:
        """Returns your `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ details based
        on the API Key you used in the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_me(request_options=request_options).unwrap()

    def get_me_allowed_origins(self, *, request_options: RequestOptionsOrDict | None = None) -> AllowedOriginsResponse:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your `API
        credential <https://docs.adyen.com/development-resources/api-credentials>`__ based on the API key you used in
        the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_me_allowed_origins(request_options=request_options).unwrap()

    def get_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AllowedOrigin:
        """Returns the details of the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_me_allowed_origins_origin_id(
            origin_id, request_options=request_options
        ).unwrap()

    def post_me_allowed_origins(
        self,
        *,
        body: CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Adds an allowed origin to the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your API
        credential. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_me_allowed_origins(body=body, request_options=request_options).unwrap()

    def post_me_generate_client_key(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateClientKeyResponse:
        """Generates a new `client key <https://docs.adyen.com/development-resources/client-side-authentication/>`__
        used to authenticate requests from your payment environment. You can use the new client key a few minutes after
        generating it. The old client key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_me_generate_client_key(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MyApiCredentialWithRawResponse:
        return self._with_raw_response


class AsyncMyApiCredential:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMyApiCredentialWithRawResponse(client, server, auth)

    async def delete_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_me_allowed_origins_origin_id(
                origin_id, request_options=request_options
            )
        ).unwrap()

    async def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> MeApiCredential:
        """Returns your `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ details based
        on the API Key you used in the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_me(request_options=request_options)).unwrap()

    async def get_me_allowed_origins(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AllowedOriginsResponse:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your `API
        credential <https://docs.adyen.com/development-resources/api-credentials>`__ based on the API key you used in
        the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_me_allowed_origins(request_options=request_options)).unwrap()

    async def get_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AllowedOrigin:
        """Returns the details of the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_me_allowed_origins_origin_id(origin_id, request_options=request_options)
        ).unwrap()

    async def post_me_allowed_origins(
        self,
        *,
        body: CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllowedOrigin:
        """Adds an allowed origin to the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your API
        credential. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_me_allowed_origins(body=body, request_options=request_options)
        ).unwrap()

    async def post_me_generate_client_key(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateClientKeyResponse:
        """Generates a new `client key <https://docs.adyen.com/development-resources/client-side-authentication/>`__
        used to authenticate requests from your payment environment. You can use the new client key a few minutes after
        generating it. The old client key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.post_me_generate_client_key(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMyApiCredentialWithRawResponse:
        return self._with_raw_response


class MyApiCredentialWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMeAllowedOriginsOriginIdErrorBody]:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/me/allowedOrigins/{originId}"),
            path_params=[param[str]("originId", origin_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_me_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    def get_me(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MeApiCredential, GetMeErrorBody]:
        """Returns your `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ details based
        on the API Key you used in the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me"),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[MeApiCredential],
            error_mapper=get_me_error_mapper,
            request_options=request_options,
        )

    def get_me_allowed_origins(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOriginsResponse, GetMeAllowedOriginsErrorBody]:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your `API
        credential <https://docs.adyen.com/development-resources/api-credentials>`__ based on the API key you used in
        the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me/allowedOrigins"),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOriginsResponse],
            error_mapper=get_me_allowed_origins_error_mapper,
            request_options=request_options,
        )

    def get_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOrigin, GetMeAllowedOriginsOriginIdErrorBody]:
        """Returns the details of the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me/allowedOrigins/{originId}"),
            path_params=[param[str]("originId", origin_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=get_me_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    def post_me_allowed_origins(
        self,
        *,
        body: CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, PostMeAllowedOriginsErrorBody]:
        """Adds an allowed origin to the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your API
        credential. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/me/allowedOrigins"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=post_me_allowed_origins_error_mapper,
            request_options=request_options,
        )

    def post_me_generate_client_key(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateClientKeyResponse, PostMeGenerateClientKeyErrorBody]:
        """Generates a new `client key <https://docs.adyen.com/development-resources/client-side-authentication/>`__
        used to authenticate requests from your payment environment. You can use the new client key a few minutes after
        generating it. The old client key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/me/generateClientKey"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateClientKeyResponse],
            error_mapper=post_me_generate_client_key_error_mapper,
            request_options=request_options,
        )


class AsyncMyApiCredentialWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMeAllowedOriginsOriginIdErrorBody]:
        """Removes the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/me/allowedOrigins/{originId}"),
            path_params=[param[str]("originId", origin_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_me_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    async def get_me(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MeApiCredential, GetMeErrorBody]:
        """Returns your `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ details based
        on the API Key you used in the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me"),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[MeApiCredential],
            error_mapper=get_me_error_mapper,
            request_options=request_options,
        )

    async def get_me_allowed_origins(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOriginsResponse, GetMeAllowedOriginsErrorBody]:
        """Returns the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your `API
        credential <https://docs.adyen.com/development-resources/api-credentials>`__ based on the API key you used in
        the request.

        You can make this request with any of the Management API roles.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me/allowedOrigins"),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOriginsResponse],
            error_mapper=get_me_allowed_origins_error_mapper,
            request_options=request_options,
        )

    async def get_me_allowed_origins_origin_id(
        self, origin_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AllowedOrigin, GetMeAllowedOriginsOriginIdErrorBody]:
        """Returns the details of the `allowed origin
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ specified in the
        path. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            origin_id: Unique identifier of the allowed origin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/me/allowedOrigins/{originId}"),
            path_params=[param[str]("originId", origin_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=get_me_allowed_origins_origin_id_error_mapper,
            request_options=request_options,
        )

    async def post_me_allowed_origins(
        self,
        *,
        body: CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllowedOrigin, PostMeAllowedOriginsErrorBody]:
        """Adds an allowed origin to the list of `allowed origins
        <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ of your API
        credential. The API key from the request is used to identify the `API credential
        <https://docs.adyen.com/development-resources/api-credentials>`__.

        You can make this request with any of the Management API roles.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/me/allowedOrigins"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AllowedOrigin],
            error_mapper=post_me_allowed_origins_error_mapper,
            request_options=request_options,
        )

    async def post_me_generate_client_key(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateClientKeyResponse, PostMeGenerateClientKeyErrorBody]:
        """Generates a new `client key <https://docs.adyen.com/development-resources/client-side-authentication/>`__
        used to authenticate requests from your payment environment. You can use the new client key a few minutes after
        generating it. The old client key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/me/generateClientKey"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateClientKeyResponse],
            error_mapper=post_me_generate_client_key_error_mapper,
            request_options=request_options,
        )
