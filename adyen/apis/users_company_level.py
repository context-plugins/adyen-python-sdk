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
from ..errors.get_companies_company_id_users_error import (
    GetCompaniesCompanyIdUsersErrorBody,
    get_companies_company_id_users_error_mapper,
)
from ..errors.get_companies_company_id_users_user_id_error import (
    GetCompaniesCompanyIdUsersUserIdErrorBody,
    get_companies_company_id_users_user_id_error_mapper,
)
from ..errors.patch_companies_company_id_users_user_id_error import (
    PatchCompaniesCompanyIdUsersUserIdErrorBody,
    patch_companies_company_id_users_user_id_error_mapper,
)
from ..errors.post_companies_company_id_users_error import (
    PostCompaniesCompanyIdUsersErrorBody,
    post_companies_company_id_users_error_mapper,
)
from ..models.company_user import CompanyUser
from ..models.create_company_user_request import CreateCompanyUserRequest, CreateCompanyUserRequestDict
from ..models.create_company_user_response import CreateCompanyUserResponse
from ..models.list_company_users_response import ListCompanyUsersResponse
from ..models.update_company_user_request import UpdateCompanyUserRequest, UpdateCompanyUserRequestDict
from ..server.server import Server


class UsersCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersCompanyLevelWithRawResponse(client, server, auth)

    def get_companies_company_id_users(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompanyUsersResponse:
        """Returns the list of users for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to return.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
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
            self._with_raw_response.get_companies_company_id_users(
                company_id,
                page_number=page_number,
                page_size=page_size,
                username=username,
                request_options=request_options,
            ),
        )

    def get_companies_company_id_users_user_id(
        self, company_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyUser:
        """Returns user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
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
            self._with_raw_response.get_companies_company_id_users_user_id(
                company_id, user_id, request_options=request_options
            ),
        )

    def patch_companies_company_id_users_user_id(
        self,
        company_id: str,
        user_id: str,
        *,
        body: UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompanyUser:
        """Updates user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
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
            self._with_raw_response.patch_companies_company_id_users_user_id(
                company_id, user_id, body=body, request_options=request_options
            ),
        )

    def post_companies_company_id_users(
        self,
        company_id: str,
        *,
        body: CreateCompanyUserRequest | CreateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCompanyUserResponse:
        """Creates the user for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
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
            self._with_raw_response.post_companies_company_id_users(
                company_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> UsersCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncUsersCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersCompanyLevelWithRawResponse(client, server, auth)

    async def get_companies_company_id_users(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompanyUsersResponse:
        """Returns the list of users for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to return.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
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
            await self._with_raw_response.get_companies_company_id_users(
                company_id,
                page_number=page_number,
                page_size=page_size,
                username=username,
                request_options=request_options,
            ),
        )

    async def get_companies_company_id_users_user_id(
        self, company_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyUser:
        """Returns user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
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
            await self._with_raw_response.get_companies_company_id_users_user_id(
                company_id, user_id, request_options=request_options
            ),
        )

    async def patch_companies_company_id_users_user_id(
        self,
        company_id: str,
        user_id: str,
        *,
        body: UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompanyUser:
        """Updates user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
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
            await self._with_raw_response.patch_companies_company_id_users_user_id(
                company_id, user_id, body=body, request_options=request_options
            ),
        )

    async def post_companies_company_id_users(
        self,
        company_id: str,
        *,
        body: CreateCompanyUserRequest | CreateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCompanyUserResponse:
        """Creates the user for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
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
            await self._with_raw_response.post_companies_company_id_users(
                company_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncUsersCompanyLevelWithRawResponse:
        return self._with_raw_response


class UsersCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_companies_company_id_users(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompanyUsersResponse, GetCompaniesCompanyIdUsersErrorBody]:
        """Returns the list of users for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to return.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/users"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("username", username),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListCompanyUsersResponse],
            error_mapper=get_companies_company_id_users_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_users_user_id(
        self, company_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyUser, GetCompaniesCompanyIdUsersUserIdErrorBody]:
        """Returns user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/users/{userId}"),
            path_params=[param[str]("companyId", company_id), param[str]("userId", user_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CompanyUser],
            error_mapper=get_companies_company_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    def patch_companies_company_id_users_user_id(
        self,
        company_id: str,
        user_id: str,
        *,
        body: UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompanyUser, PatchCompaniesCompanyIdUsersUserIdErrorBody]:
        """Updates user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/users/{userId}"),
            path_params=[param[str]("companyId", company_id), param[str]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CompanyUser],
            error_mapper=patch_companies_company_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_users(
        self,
        company_id: str,
        *,
        body: CreateCompanyUserRequest | CreateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCompanyUserResponse, PostCompaniesCompanyIdUsersErrorBody]:
        """Creates the user for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/users"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCompanyUserRequest | CreateCompanyUserRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateCompanyUserResponse],
            error_mapper=post_companies_company_id_users_error_mapper,
            request_options=request_options,
        )


class AsyncUsersCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_companies_company_id_users(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        username: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompanyUsersResponse, GetCompaniesCompanyIdUsersErrorBody]:
        """Returns the list of users for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to return.
            page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a
                page.
            username: The partial or complete username to select all users that match.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/users"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("username", username),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ListCompanyUsersResponse],
            error_mapper=get_companies_company_id_users_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_users_user_id(
        self, company_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyUser, GetCompaniesCompanyIdUsersUserIdErrorBody]:
        """Returns user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/users/{userId}"),
            path_params=[param[str]("companyId", company_id), param[str]("userId", user_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CompanyUser],
            error_mapper=get_companies_company_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    async def patch_companies_company_id_users_user_id(
        self,
        company_id: str,
        user_id: str,
        *,
        body: UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompanyUser, PatchCompaniesCompanyIdUsersUserIdErrorBody]:
        """Updates user details for the ``userId`` and the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            user_id: The unique identifier of the user.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/users/{userId}"),
            path_params=[param[str]("companyId", company_id), param[str]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCompanyUserRequest | UpdateCompanyUserRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CompanyUser],
            error_mapper=patch_companies_company_id_users_user_id_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_users(
        self,
        company_id: str,
        *,
        body: CreateCompanyUserRequest | CreateCompanyUserRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCompanyUserResponse, PostCompaniesCompanyIdUsersErrorBody]:
        """Creates the user for the ``companyId`` identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Users read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/users"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCompanyUserRequest | CreateCompanyUserRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CreateCompanyUserResponse],
            error_mapper=post_companies_company_id_users_error_mapper,
            request_options=request_options,
        )
