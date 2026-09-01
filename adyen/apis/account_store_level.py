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
from ..errors.get_merchants_merchant_id_stores_error import (
    GetMerchantsMerchantIdStoresErrorBody,
    get_merchants_merchant_id_stores_error_mapper,
)
from ..errors.get_merchants_merchant_id_stores_store_id_error import (
    GetMerchantsMerchantIdStoresStoreIdErrorBody,
    get_merchants_merchant_id_stores_store_id_error_mapper,
)
from ..errors.get_stores_error import GetStoresErrorBody, get_stores_error_mapper
from ..errors.get_stores_store_id_error import GetStoresStoreIdErrorBody, get_stores_store_id_error_mapper
from ..errors.patch_merchants_merchant_id_stores_store_id_error import (
    PatchMerchantsMerchantIdStoresStoreIdErrorBody,
    patch_merchants_merchant_id_stores_store_id_error_mapper,
)
from ..errors.patch_stores_store_id_error import PatchStoresStoreIdErrorBody, patch_stores_store_id_error_mapper
from ..errors.post_merchants_merchant_id_stores_error import (
    PostMerchantsMerchantIdStoresErrorBody,
    post_merchants_merchant_id_stores_error_mapper,
)
from ..errors.post_stores_error import PostStoresErrorBody, post_stores_error_mapper
from ..models.list_stores_response import ListStoresResponse
from ..models.store import Store
from ..models.store_creation_request import StoreCreationRequest, StoreCreationRequestDict
from ..models.store_creation_with_merchant_code_request import (
    StoreCreationWithMerchantCodeRequest,
    StoreCreationWithMerchantCodeRequestDict,
)
from ..models.update_store_request import UpdateStoreRequest, UpdateStoreRequestDict
from ..server.server import Server


class AccountStoreLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountStoreLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoresResponse:
        """Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as
        defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_stores(
            merchant_id,
            page_number=page_number,
            page_size=page_size,
            reference=reference,
            request_options=request_options,
        ).unwrap()

    def get_merchants_merchant_id_stores_store_id(
        self, merchant_id: str, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Store:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_stores_store_id(
            merchant_id, store_id, request_options=request_options
        ).unwrap()

    def get_stores(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        merchant_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoresResponse:
        """Returns a list of stores. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_stores(
            page_number=page_number,
            page_size=page_size,
            reference=reference,
            merchant_id=merchant_id,
            request_options=request_options,
        ).unwrap()

    def get_stores_store_id(self, store_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Store:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_stores_store_id(store_id, request_options=request_options).unwrap()

    def patch_merchants_merchant_id_stores_store_id(
        self,
        merchant_id: str,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_stores_store_id(
            merchant_id, store_id, body=body, request_options=request_options
        ).unwrap()

    def patch_stores_store_id(
        self,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_stores_store_id(
            store_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        body: StoreCreationRequest | StoreCreationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Creates a store for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
        return self._with_raw_response.post_merchants_merchant_id_stores(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_stores(
        self,
        *,
        body: StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Creates a store for the merchant account specified in the request.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
        return self._with_raw_response.post_stores(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountStoreLevelWithRawResponse:
        return self._with_raw_response


class AsyncAccountStoreLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountStoreLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoresResponse:
        """Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as
        defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_stores(
                merchant_id,
                page_number=page_number,
                page_size=page_size,
                reference=reference,
                request_options=request_options,
            )
        ).unwrap()

    async def get_merchants_merchant_id_stores_store_id(
        self, merchant_id: str, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Store:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_stores_store_id(
                merchant_id, store_id, request_options=request_options
            )
        ).unwrap()

    async def get_stores(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        merchant_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoresResponse:
        """Returns a list of stores. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
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
            await self._with_raw_response.get_stores(
                page_number=page_number,
                page_size=page_size,
                reference=reference,
                merchant_id=merchant_id,
                request_options=request_options,
            )
        ).unwrap()

    async def get_stores_store_id(self, store_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Store:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_stores_store_id(store_id, request_options=request_options)).unwrap()

    async def patch_merchants_merchant_id_stores_store_id(
        self,
        merchant_id: str,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
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
            await self._with_raw_response.patch_merchants_merchant_id_stores_store_id(
                merchant_id, store_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def patch_stores_store_id(
        self,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
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
            await self._with_raw_response.patch_stores_store_id(store_id, body=body, request_options=request_options)
        ).unwrap()

    async def post_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        body: StoreCreationRequest | StoreCreationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Creates a store for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
            await self._with_raw_response.post_merchants_merchant_id_stores(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_stores(
        self,
        *,
        body: StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Store:
        """Creates a store for the merchant account specified in the request.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
        return (await self._with_raw_response.post_stores(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountStoreLevelWithRawResponse:
        return self._with_raw_response


class AccountStoreLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoresResponse, GetMerchantsMerchantIdStoresErrorBody]:
        """Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as
        defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("reference", reference),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoresResponse],
            error_mapper=get_merchants_merchant_id_stores_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_stores_store_id(
        self, merchant_id: str, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Store, GetMerchantsMerchantIdStoresStoreIdErrorBody]:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{storeId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=get_merchants_merchant_id_stores_store_id_error_mapper,
            request_options=request_options,
        )

    def get_stores(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        merchant_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoresResponse, GetStoresErrorBody]:
        """Returns a list of stores. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores"),
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("reference", reference),
                param[str | None]("merchantId", merchant_id),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoresResponse],
            error_mapper=get_stores_error_mapper,
            request_options=request_options,
        )

    def get_stores_store_id(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Store, GetStoresStoreIdErrorBody]:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}"),
            path_params=[param[str]("storeId", store_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=get_stores_store_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_stores_store_id(
        self,
        merchant_id: str,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PatchMerchantsMerchantIdStoresStoreIdErrorBody]:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{storeId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateStoreRequest | UpdateStoreRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=patch_merchants_merchant_id_stores_store_id_error_mapper,
            request_options=request_options,
        )

    def patch_stores_store_id(
        self,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PatchStoresStoreIdErrorBody]:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}"),
            path_params=[param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateStoreRequest | UpdateStoreRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=patch_stores_store_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        body: StoreCreationRequest | StoreCreationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PostMerchantsMerchantIdStoresErrorBody]:
        """Creates a store for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/stores"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreCreationRequest | StoreCreationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=post_merchants_merchant_id_stores_error_mapper,
            request_options=request_options,
        )

    def post_stores(
        self,
        *,
        body: StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PostStoresErrorBody]:
        """Creates a store for the merchant account specified in the request.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/stores"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=post_stores_error_mapper,
            request_options=request_options,
        )


class AsyncAccountStoreLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoresResponse, GetMerchantsMerchantIdStoresErrorBody]:
        """Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as
        defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("reference", reference),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoresResponse],
            error_mapper=get_merchants_merchant_id_stores_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_stores_store_id(
        self, merchant_id: str, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Store, GetMerchantsMerchantIdStoresStoreIdErrorBody]:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{storeId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=get_merchants_merchant_id_stores_store_id_error_mapper,
            request_options=request_options,
        )

    async def get_stores(
        self,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        reference: str | None = None,
        merchant_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoresResponse, GetStoresErrorBody]:
        """Returns a list of stores. The list is grouped into pages as defined by the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            reference: The reference of the store.
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores"),
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("reference", reference),
                param[str | None]("merchantId", merchant_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoresResponse],
            error_mapper=get_stores_error_mapper,
            request_options=request_options,
        )

    async def get_stores_store_id(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Store, GetStoresStoreIdErrorBody]:
        """Returns the details of the store identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}"),
            path_params=[param[str]("storeId", store_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=get_stores_store_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_stores_store_id(
        self,
        merchant_id: str,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PatchMerchantsMerchantIdStoresStoreIdErrorBody]:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{storeId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateStoreRequest | UpdateStoreRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=patch_merchants_merchant_id_stores_store_id_error_mapper,
            request_options=request_options,
        )

    async def patch_stores_store_id(
        self,
        store_id: str,
        *,
        body: UpdateStoreRequest | UpdateStoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PatchStoresStoreIdErrorBody]:
        """Updates the store identified in the path. You can only update some store parameters.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}"),
            path_params=[param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateStoreRequest | UpdateStoreRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=patch_stores_store_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_stores(
        self,
        merchant_id: str,
        *,
        body: StoreCreationRequest | StoreCreationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PostMerchantsMerchantIdStoresErrorBody]:
        """Creates a store for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/stores"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreCreationRequest | StoreCreationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=post_merchants_merchant_id_stores_error_mapper,
            request_options=request_options,
        )

    async def post_stores(
        self,
        *,
        body: StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Store, PostStoresErrorBody]:
        """Creates a store for the merchant account specified in the request.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Stores read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/stores"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Store],
            error_mapper=post_stores_error_mapper,
            request_options=request_options,
        )
