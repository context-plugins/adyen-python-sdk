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
from ..errors.get_merchants_merchant_id_users_error import (
    GetMerchantsMerchantIdUsersErrorBody,
    get_merchants_merchant_id_users_error_mapper,
)
from ..errors.get_merchants_merchant_id_users_user_id_error import (
    GetMerchantsMerchantIdUsersUserIdErrorBody,
    get_merchants_merchant_id_users_user_id_error_mapper,
)
from ..errors.patch_merchants_merchant_id_users_user_id_error import (
    PatchMerchantsMerchantIdUsersUserIdErrorBody,
    patch_merchants_merchant_id_users_user_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_users_error import (
    PostMerchantsMerchantIdUsersErrorBody,
    post_merchants_merchant_id_users_error_mapper,
)
from ..models.create_merchant_user_request import CreateMerchantUserRequest, CreateMerchantUserRequestDict
from ..models.create_user_response import CreateUserResponse
from ..models.list_merchant_users_response import ListMerchantUsersResponse
from ..models.update_merchant_user_request import UpdateMerchantUserRequest, UpdateMerchantUserRequestDict
from ..models.user import User
from ..server.server import Server


class UsersMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantUsersResponse:
        """Returns a list of users associated with the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_users(
            merchant_id,
            page_number=page_number,
            page_size=page_size,
            username=username,
            request_options=request_options,
        ).unwrap()

    def get_merchants_merchant_id_users_user_id(
        self, merchant_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """Returns user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_users_user_id(
            merchant_id, user_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_users_user_id(
        self,
        merchant_id: str,
        user_id: str,
        *,
        body: UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """Updates user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_users_user_id(
            merchant_id, user_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantUserRequest | CreateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateUserResponse:
        """Creates a user for the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_users(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncUsersMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantUsersResponse:
        """Returns a list of users associated with the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_users(
                merchant_id,
                page_number=page_number,
                page_size=page_size,
                username=username,
                request_options=request_options,
            )
        ).unwrap()

    async def get_merchants_merchant_id_users_user_id(
        self, merchant_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> User:
        """Returns user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_users_user_id(
                merchant_id, user_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_users_user_id(
        self,
        merchant_id: str,
        user_id: str,
        *,
        body: UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> User:
        """Updates user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
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
            await self._with_raw_response.patch_merchants_merchant_id_users_user_id(
                merchant_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantUserRequest | CreateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateUserResponse:
        """Creates a user for the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
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
            await self._with_raw_response.post_merchants_merchant_id_users(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersMerchantLevelWithRawResponse:
        return self._with_raw_response


class UsersMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantUsersResponse, GetMerchantsMerchantIdUsersErrorBody]:
        """Returns a list of users associated with the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/users"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("username", username),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantUsersResponse],
            error_mapper=get_merchants_merchant_id_users_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_users_user_id(
        self, merchant_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, GetMerchantsMerchantIdUsersUserIdErrorBody]:
        """Returns user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/users/{userId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("userId", user_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[User],
            error_mapper=get_merchants_merchant_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_users_user_id(
        self,
        merchant_id: str,
        user_id: str,
        *,
        body: UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, PatchMerchantsMerchantIdUsersUserIdErrorBody]:
        """Updates user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/users/{userId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[User],
            error_mapper=patch_merchants_merchant_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantUserRequest | CreateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateUserResponse, PostMerchantsMerchantIdUsersErrorBody]:
        """Creates a user for the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/users"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantUserRequest | CreateMerchantUserRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateUserResponse],
            error_mapper=post_merchants_merchant_id_users_error_mapper,
            request_options=request_options,
        )


class AsyncUsersMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantUsersResponse, GetMerchantsMerchantIdUsersErrorBody]:
        """Returns a list of users associated with the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/users"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("username", username),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantUsersResponse],
            error_mapper=get_merchants_merchant_id_users_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_users_user_id(
        self, merchant_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[User, GetMerchantsMerchantIdUsersUserIdErrorBody]:
        """Returns user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/users/{userId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("userId", user_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[User],
            error_mapper=get_merchants_merchant_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_users_user_id(
        self,
        merchant_id: str,
        user_id: str,
        *,
        body: UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[User, PatchMerchantsMerchantIdUsersUserIdErrorBody]:
        """Updates user details for the ``userId`` and the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            user_id: Unique identifier of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/users/{userId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[User],
            error_mapper=patch_merchants_merchant_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_users(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantUserRequest | CreateMerchantUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateUserResponse, PostMerchantsMerchantIdUsersErrorBody]:
        """Creates a user for the ``merchantId`` specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            merchant_id: Unique identifier of the merchant.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/users"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantUserRequest | CreateMerchantUserRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateUserResponse],
            error_mapper=post_merchants_merchant_id_users_error_mapper,
            request_options=request_options,
        )
