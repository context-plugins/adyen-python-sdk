from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_companies_company_id_error import (
    GetCompaniesCompanyIdErrorBody,
    get_companies_company_id_error_mapper,
)
from ..errors.get_companies_company_id_merchants_error import (
    GetCompaniesCompanyIdMerchantsErrorBody,
    get_companies_company_id_merchants_error_mapper,
)
from ..errors.get_companies_error import GetCompaniesErrorBody, get_companies_error_mapper
from ..models.company2 import Company2
from ..models.list_company_response import ListCompanyResponse
from ..models.list_merchant_response import ListMerchantResponse
from ..server.server import Server


class AccountCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountCompanyLevelWithRawResponse(client, server, auth)

    def get_companies(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompanyResponse:
        """Returns the list of company accounts that your API credential has access to. The list is grouped into pages
        as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Account read

        Args:
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
        return self._with_raw_response.get_companies(
            page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    def get_companies_company_id(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Company2:
        """Returns the company account specified in the path. Your API credential must have access to the company
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id(company_id, request_options=request_options).unwrap()

    def get_companies_company_id_merchants(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantResponse:
        """Returns the list of merchant accounts under the company account specified in the path. The list only includes
        merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query
        parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
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
        return self._with_raw_response.get_companies_company_id_merchants(
            company_id, page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncAccountCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountCompanyLevelWithRawResponse(client, server, auth)

    async def get_companies(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCompanyResponse:
        """Returns the list of company accounts that your API credential has access to. The list is grouped into pages
        as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Account read

        Args:
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
            await self._with_raw_response.get_companies(
                page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Company2:
        """Returns the company account specified in the path. Your API credential must have access to the company
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id(company_id, request_options=request_options)
        ).unwrap()

    async def get_companies_company_id_merchants(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantResponse:
        """Returns the list of merchant accounts under the company account specified in the path. The list only includes
        merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query
        parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
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
            await self._with_raw_response.get_companies_company_id_merchants(
                company_id, page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountCompanyLevelWithRawResponse:
        return self._with_raw_response


class AccountCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_companies(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompanyResponse, GetCompaniesErrorBody]:
        """Returns the list of company accounts that your API credential has access to. The list is grouped into pages
        as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Account read

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies"),
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListCompanyResponse],
            error_mapper=get_companies_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Company2, GetCompaniesCompanyIdErrorBody]:
        """Returns the company account specified in the path. Your API credential must have access to the company
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}"),
            path_params=[param[str]("companyId", company_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Company2],
            error_mapper=get_companies_company_id_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_merchants(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantResponse, GetCompaniesCompanyIdMerchantsErrorBody]:
        """Returns the list of merchant accounts under the company account specified in the path. The list only includes
        merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query
        parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/merchants"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantResponse],
            error_mapper=get_companies_company_id_merchants_error_mapper,
            request_options=request_options,
        )


class AsyncAccountCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_companies(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCompanyResponse, GetCompaniesErrorBody]:
        """Returns the list of company accounts that your API credential has access to. The list is grouped into pages
        as defined by the query parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Account read

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies"),
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListCompanyResponse],
            error_mapper=get_companies_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Company2, GetCompaniesCompanyIdErrorBody]:
        """Returns the company account specified in the path. Your API credential must have access to the company
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}"),
            path_params=[param[str]("companyId", company_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Company2],
            error_mapper=get_companies_company_id_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_merchants(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantResponse, GetCompaniesCompanyIdMerchantsErrorBody]:
        """Returns the list of merchant accounts under the company account specified in the path. The list only includes
        merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query
        parameters.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/merchants"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantResponse],
            error_mapper=get_companies_company_id_merchants_error_mapper,
            request_options=request_options,
        )
