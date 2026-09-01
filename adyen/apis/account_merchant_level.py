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
from ..errors.get_merchants_error import GetMerchantsErrorBody, get_merchants_error_mapper
from ..errors.get_merchants_merchant_id_error import (
    GetMerchantsMerchantIdErrorBody,
    get_merchants_merchant_id_error_mapper,
)
from ..errors.post_merchants_error import PostMerchantsErrorBody, post_merchants_error_mapper
from ..errors.post_merchants_merchant_id_activate_error import (
    PostMerchantsMerchantIdActivateErrorBody,
    post_merchants_merchant_id_activate_error_mapper,
)
from ..models.create_merchant_request import CreateMerchantRequest, CreateMerchantRequestDict
from ..models.create_merchant_response import CreateMerchantResponse
from ..models.list_merchant_response import ListMerchantResponse
from ..models.merchant import Merchant
from ..models.request_activation_response import RequestActivationResponse
from ..server.server import Server


class AccountMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantResponse:
        """Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages
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
        return self._with_raw_response.get_merchants(
            page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Merchant:
        """Returns the merchant account specified in the path. Your API credential must have access to the merchant
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id(merchant_id, request_options=request_options).unwrap()

    def post_merchants(
        self,
        *,
        body: CreateMerchantRequest | CreateMerchantRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMerchantResponse:
        """Creates a merchant account for the company account specified in the request.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

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
        return self._with_raw_response.post_merchants(body=body, request_options=request_options).unwrap()

    def post_merchants_merchant_id_activate(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RequestActivationResponse:
        """Sends a request to activate the merchant account identified in the path.

        You get the result of the activation asynchronously through a
        https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated webhook. Once the
        merchant account is activated, you can start using it to accept payments and payouts.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_activate(
            merchant_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncAccountMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantResponse:
        """Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages
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
            await self._with_raw_response.get_merchants(
                page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Merchant:
        """Returns the merchant account specified in the path. Your API credential must have access to the merchant
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id(merchant_id, request_options=request_options)
        ).unwrap()

    async def post_merchants(
        self,
        *,
        body: CreateMerchantRequest | CreateMerchantRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMerchantResponse:
        """Creates a merchant account for the company account specified in the request.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

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
        return (await self._with_raw_response.post_merchants(body=body, request_options=request_options)).unwrap()

    async def post_merchants_merchant_id_activate(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RequestActivationResponse:
        """Sends a request to activate the merchant account identified in the path.

        You get the result of the activation asynchronously through a
        https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated webhook. Once the
        merchant account is activated, you can start using it to accept payments and payouts.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_activate(
                merchant_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountMerchantLevelWithRawResponse:
        return self._with_raw_response


class AccountMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantResponse, GetMerchantsErrorBody]:
        """Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages
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
            url_template=self._server.default9("/merchants"),
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantResponse],
            error_mapper=get_merchants_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Merchant, GetMerchantsMerchantIdErrorBody]:
        """Returns the merchant account specified in the path. Your API credential must have access to the merchant
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Merchant],
            error_mapper=get_merchants_merchant_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants(
        self,
        *,
        body: CreateMerchantRequest | CreateMerchantRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMerchantResponse, PostMerchantsErrorBody]:
        """Creates a merchant account for the company account specified in the request.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantRequest | CreateMerchantRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateMerchantResponse],
            error_mapper=post_merchants_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_activate(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RequestActivationResponse, PostMerchantsMerchantIdActivateErrorBody]:
        """Sends a request to activate the merchant account identified in the path.

        You get the result of the activation asynchronously through a
        https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated webhook. Once the
        merchant account is activated, you can start using it to accept payments and payouts.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/activate"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RequestActivationResponse],
            error_mapper=post_merchants_merchant_id_activate_error_mapper,
            request_options=request_options,
        )


class AsyncAccountMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantResponse, GetMerchantsErrorBody]:
        """Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages
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
            url_template=self._server.default9("/merchants"),
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListMerchantResponse],
            error_mapper=get_merchants_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Merchant, GetMerchantsMerchantIdErrorBody]:
        """Returns the merchant account specified in the path. Your API credential must have access to the merchant
        account.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Account read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Merchant],
            error_mapper=get_merchants_merchant_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants(
        self,
        *,
        body: CreateMerchantRequest | CreateMerchantRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMerchantResponse, PostMerchantsErrorBody]:
        """Creates a merchant account for the company account specified in the request.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantRequest | CreateMerchantRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateMerchantResponse],
            error_mapper=post_merchants_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_activate(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RequestActivationResponse, PostMerchantsMerchantIdActivateErrorBody]:
        """Sends a request to activate the merchant account identified in the path.

        You get the result of the activation asynchronously through a
        https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated webhook. Once the
        merchant account is activated, you can start using it to accept payments and payouts.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Accounts read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/activate"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RequestActivationResponse],
            error_mapper=post_merchants_merchant_id_activate_error_mapper,
            request_options=request_options,
        )
