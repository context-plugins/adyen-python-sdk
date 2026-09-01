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
from ..errors.get_merchants_merchant_id_api_credentials_api_credential_id_error import (
    GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody,
    get_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_api_credentials_error import (
    GetMerchantsMerchantIdApiCredentialsErrorBody,
    get_merchants_merchant_id_api_credentials_error_mapper,
)
from ..errors.patch_merchants_merchant_id_api_credentials_api_credential_id_error import (
    PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody,
    patch_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_api_credentials_error import (
    PostMerchantsMerchantIdApiCredentialsErrorBody,
    post_merchants_merchant_id_api_credentials_error_mapper,
)
from ..models.api_credential import ApiCredential
from ..models.create_api_credential_response import CreateApiCredentialResponse
from ..models.create_merchant_api_credential_request import (
    CreateMerchantApiCredentialRequest,
    CreateMerchantApiCredentialRequestDict,
)
from ..models.list_merchant_api_credentials_response import ListMerchantApiCredentialsResponse
from ..models.update_merchant_api_credential_request import (
    UpdateMerchantApiCredentialRequest,
    UpdateMerchantApiCredentialRequestDict,
)
from ..server.server import Server


class ApiCredentialsMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiCredentialsMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantApiCredentialsResponse:
        """Returns the list of `API credentials <https://docs.adyen.com/development-resources/api-credentials>`__ for
        the merchant account. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_api_credentials(
            merchant_id, page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_api_credentials_api_credential_id(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiCredential:
        """Returns the `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ identified in
        the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id(
            merchant_id, api_credential_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_api_credentials_api_credential_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiCredential:
        """Changes the API credential's roles, or allowed origins. The request has the new values for the fields you
        want to change. The response contains the full updated API credential, including the new values from the
        request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_api_credentials_api_credential_id(
            merchant_id, api_credential_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateApiCredentialResponse:
        """Creates an `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ for the company
        account identified in the path. In the request, you can specify the roles and allowed origins for the new API
        credential.

        The response includes the:
        * `API key <https://docs.adyen.com/development-resources/api-authentication#api-key-authentication>`__: used for
            API request authentication.
        * `Client key <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__: public
            key used for client-side authentication.
        * `Username and password
            <https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication>`__: used for
            basic authentication.

        > Make sure you store the API key securely in your system. You won't be able to retrieve it later.

        If your API key is lost or compromised, you need to `generate a new API key
        <https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_api_credentials(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ApiCredentialsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncApiCredentialsMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiCredentialsMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantApiCredentialsResponse:
        """Returns the list of `API credentials <https://docs.adyen.com/development-resources/api-credentials>`__ for
        the merchant account. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_api_credentials(
                merchant_id, page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_api_credentials_api_credential_id(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiCredential:
        """Returns the `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ identified in
        the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_api_credentials_api_credential_id(
                merchant_id, api_credential_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_api_credentials_api_credential_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiCredential:
        """Changes the API credential's roles, or allowed origins. The request has the new values for the fields you
        want to change. The response contains the full updated API credential, including the new values from the
        request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
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
            await self._with_raw_response.patch_merchants_merchant_id_api_credentials_api_credential_id(
                merchant_id, api_credential_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateApiCredentialResponse:
        """Creates an `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ for the company
        account identified in the path. In the request, you can specify the roles and allowed origins for the new API
        credential.

        The response includes the:
        * `API key <https://docs.adyen.com/development-resources/api-authentication#api-key-authentication>`__: used for
            API request authentication.
        * `Client key <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__: public
            key used for client-side authentication.
        * `Username and password
            <https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication>`__: used for
            basic authentication.

        > Make sure you store the API key securely in your system. You won't be able to retrieve it later.

        If your API key is lost or compromised, you need to `generate a new API key
        <https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.post_merchants_merchant_id_api_credentials(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApiCredentialsMerchantLevelWithRawResponse:
        return self._with_raw_response


class ApiCredentialsMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantApiCredentialsResponse, GetMerchantsMerchantIdApiCredentialsErrorBody]:
        """Returns the list of `API credentials <https://docs.adyen.com/development-resources/api-credentials>`__ for
        the merchant account. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantApiCredentialsResponse],
            error_mapper=get_merchants_merchant_id_api_credentials_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_api_credentials_api_credential_id(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiCredential, GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]:
        """Returns the `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ identified in
        the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials/{apiCredentialId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApiCredential],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_api_credentials_api_credential_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiCredential, PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]:
        """Changes the API credential's roles, or allowed origins. The request has the new values for the fields you
        want to change. The response contains the full updated API credential, including the new values from the
        request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials/{apiCredentialId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApiCredential],
            error_mapper=patch_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateApiCredentialResponse, PostMerchantsMerchantIdApiCredentialsErrorBody]:
        """Creates an `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ for the company
        account identified in the path. In the request, you can specify the roles and allowed origins for the new API
        credential.

        The response includes the:
        * `API key <https://docs.adyen.com/development-resources/api-authentication#api-key-authentication>`__: used for
            API request authentication.
        * `Client key <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__: public
            key used for client-side authentication.
        * `Username and password
            <https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication>`__: used for
            basic authentication.

        > Make sure you store the API key securely in your system. You won't be able to retrieve it later.

        If your API key is lost or compromised, you need to `generate a new API key
        <https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateApiCredentialResponse],
            error_mapper=post_merchants_merchant_id_api_credentials_error_mapper,
            request_options=request_options,
        )


class AsyncApiCredentialsMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantApiCredentialsResponse, GetMerchantsMerchantIdApiCredentialsErrorBody]:
        """Returns the list of `API credentials <https://docs.adyen.com/development-resources/api-credentials>`__ for
        the merchant account. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantApiCredentialsResponse],
            error_mapper=get_merchants_merchant_id_api_credentials_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_api_credentials_api_credential_id(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiCredential, GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]:
        """Returns the `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ identified in
        the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials/{apiCredentialId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApiCredential],
            error_mapper=get_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_api_credentials_api_credential_id(
        self,
        merchant_id: str,
        api_credential_id: str,
        *,
        body: UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiCredential, PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]:
        """Changes the API credential's roles, or allowed origins. The request has the new values for the fields you
        want to change. The response contains the full updated API credential, including the new values from the
        request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials/{apiCredentialId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApiCredential],
            error_mapper=patch_merchants_merchant_id_api_credentials_api_credential_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_api_credentials(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateApiCredentialResponse, PostMerchantsMerchantIdApiCredentialsErrorBody]:
        """Creates an `API credential <https://docs.adyen.com/development-resources/api-credentials>`__ for the company
        account identified in the path. In the request, you can specify the roles and allowed origins for the new API
        credential.

        The response includes the:
        * `API key <https://docs.adyen.com/development-resources/api-authentication#api-key-authentication>`__: used for
            API request authentication.
        * `Client key <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__: public
            key used for client-side authentication.
        * `Username and password
            <https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication>`__: used for
            basic authentication.

        > Make sure you store the API key securely in your system. You won't be able to retrieve it later.

        If your API key is lost or compromised, you need to `generate a new API key
        <https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/apiCredentials"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateApiCredentialResponse],
            error_mapper=post_merchants_merchant_id_api_credentials_error_mapper,
            request_options=request_options,
        )
