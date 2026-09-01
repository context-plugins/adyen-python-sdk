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
from ..errors.get_companies_company_id_billing_entities_error import (
    GetCompaniesCompanyIdBillingEntitiesErrorBody,
    get_companies_company_id_billing_entities_error_mapper,
)
from ..errors.get_companies_company_id_shipping_locations_error import (
    GetCompaniesCompanyIdShippingLocationsErrorBody,
    get_companies_company_id_shipping_locations_error_mapper,
)
from ..errors.get_companies_company_id_terminal_models_error import (
    GetCompaniesCompanyIdTerminalModelsErrorBody,
    get_companies_company_id_terminal_models_error_mapper,
)
from ..errors.get_companies_company_id_terminal_orders_error import (
    GetCompaniesCompanyIdTerminalOrdersErrorBody,
    get_companies_company_id_terminal_orders_error_mapper,
)
from ..errors.get_companies_company_id_terminal_orders_order_id_error import (
    GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody,
    get_companies_company_id_terminal_orders_order_id_error_mapper,
)
from ..errors.get_companies_company_id_terminal_products_error import (
    GetCompaniesCompanyIdTerminalProductsErrorBody,
    get_companies_company_id_terminal_products_error_mapper,
)
from ..errors.patch_companies_company_id_terminal_orders_order_id_error import (
    PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody,
    patch_companies_company_id_terminal_orders_order_id_error_mapper,
)
from ..errors.post_companies_company_id_shipping_locations_error import (
    PostCompaniesCompanyIdShippingLocationsErrorBody,
    post_companies_company_id_shipping_locations_error_mapper,
)
from ..errors.post_companies_company_id_terminal_orders_error import (
    PostCompaniesCompanyIdTerminalOrdersErrorBody,
    post_companies_company_id_terminal_orders_error_mapper,
)
from ..errors.post_companies_company_id_terminal_orders_order_id_cancel_error import (
    PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody,
    post_companies_company_id_terminal_orders_order_id_cancel_error_mapper,
)
from ..models.billing_entities_response import BillingEntitiesResponse
from ..models.shipping_location import ShippingLocation, ShippingLocationDict
from ..models.shipping_locations_response import ShippingLocationsResponse
from ..models.terminal_models_response import TerminalModelsResponse
from ..models.terminal_order import TerminalOrder
from ..models.terminal_order_request import TerminalOrderRequest, TerminalOrderRequestDict
from ..models.terminal_orders_response import TerminalOrdersResponse
from ..models.terminal_products_response import TerminalProductsResponse
from ..server.server import Server


class TerminalOrdersCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalOrdersCompanyLevelWithRawResponse(client, server, auth)

    def get_companies_company_id_billing_entities(
        self, company_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> BillingEntitiesResponse:
        """Returns the billing entities of the company identified in the path and all merchant accounts belonging to the
        company. A billing entity is a legal entity where we charge orders to. An order for terminal products must
        contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_billing_entities(
            company_id, name=name, request_options=request_options
        ).unwrap()

    def get_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocationsResponse:
        """Returns the shipping locations for the company identified in the path and all merchant accounts belonging to
        the company. A shipping location includes the address where orders can be delivered, and an ID which you need to
        specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_shipping_locations(
            company_id, name=name, offset=offset, limit=limit, request_options=request_options
        ).unwrap()

    def get_companies_company_id_terminal_models(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalModelsResponse:
        """Returns a list of payment terminal models that the company identified in the path has access to. The response
        includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a
        list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
        return self._with_raw_response.get_companies_company_id_terminal_models(
            company_id, request_options=request_options
        ).unwrap()

    def get_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrdersResponse:
        """Returns a lists of terminal products orders for the company identified in the path. To filter the list, use
        one or more of the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            customer_order_reference: Your purchase order number.
            status: The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped,
                Delivered.
            offset: The number of orders to skip.
            limit: The number of orders to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_terminal_orders(
            company_id,
            customer_order_reference=customer_order_reference,
            status=status,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def get_companies_company_id_terminal_orders_order_id(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_terminal_orders_order_id(
            company_id, order_id, request_options=request_options
        ).unwrap()

    def get_companies_company_id_terminal_products(
        self,
        company_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalProductsResponse:
        """Returns a country-specific list of payment terminal packages and parts that the company identified in the
        path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_terminal_products(
            company_id,
            country,
            terminal_model_id=terminal_model_id,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def patch_companies_company_id_terminal_orders_order_id(
        self,
        company_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Updates the terminal products order identified in the path. Updating is only possible while the order has the
        status **Placed**.

        The request body only needs to contain what you want to change. However, to update the products in the ``items``
        array, you must provide the entire array. For example, if the array has three items:
         To remove one item, the array must include the remaining two items. Or to add one item, the array must include
            all four items.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_companies_company_id_terminal_orders_order_id(
            company_id, order_id, body=body, request_options=request_options
        ).unwrap()

    def post_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocation:
        """Creates a shipping location for the company identified in the path. A shipping location defines an address
        where orders can be delivered.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_companies_company_id_shipping_locations(
            company_id, body=body, request_options=request_options
        ).unwrap()

    def post_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Creates an order for payment terminal products for the company identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write
        >Requests to the Management API test endpoint do not create actual orders for test terminals. To order test
        terminals, you need to `submit a sales order
        <https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps>`__ in your Customer
        Area.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_companies_company_id_terminal_orders(
            company_id, body=body, request_options=request_options
        ).unwrap()

    def post_companies_company_id_terminal_orders_order_id_cancel(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_companies_company_id_terminal_orders_order_id_cancel(
            company_id, order_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TerminalOrdersCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalOrdersCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalOrdersCompanyLevelWithRawResponse(client, server, auth)

    async def get_companies_company_id_billing_entities(
        self, company_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> BillingEntitiesResponse:
        """Returns the billing entities of the company identified in the path and all merchant accounts belonging to the
        company. A billing entity is a legal entity where we charge orders to. An order for terminal products must
        contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_billing_entities(
                company_id, name=name, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocationsResponse:
        """Returns the shipping locations for the company identified in the path and all merchant accounts belonging to
        the company. A shipping location includes the address where orders can be delivered, and an ID which you need to
        specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_shipping_locations(
                company_id, name=name, offset=offset, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id_terminal_models(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalModelsResponse:
        """Returns a list of payment terminal models that the company identified in the path has access to. The response
        includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a
        list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
            await self._with_raw_response.get_companies_company_id_terminal_models(
                company_id, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrdersResponse:
        """Returns a lists of terminal products orders for the company identified in the path. To filter the list, use
        one or more of the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            customer_order_reference: Your purchase order number.
            status: The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped,
                Delivered.
            offset: The number of orders to skip.
            limit: The number of orders to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_terminal_orders(
                company_id,
                customer_order_reference=customer_order_reference,
                status=status,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def get_companies_company_id_terminal_orders_order_id(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_terminal_orders_order_id(
                company_id, order_id, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id_terminal_products(
        self,
        company_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalProductsResponse:
        """Returns a country-specific list of payment terminal packages and parts that the company identified in the
        path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_terminal_products(
                company_id,
                country,
                terminal_model_id=terminal_model_id,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_companies_company_id_terminal_orders_order_id(
        self,
        company_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Updates the terminal products order identified in the path. Updating is only possible while the order has the
        status **Placed**.

        The request body only needs to contain what you want to change. However, to update the products in the ``items``
        array, you must provide the entire array. For example, if the array has three items:
         To remove one item, the array must include the remaining two items. Or to add one item, the array must include
            all four items.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
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
            await self._with_raw_response.patch_companies_company_id_terminal_orders_order_id(
                company_id, order_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocation:
        """Creates a shipping location for the company identified in the path. A shipping location defines an address
        where orders can be delivered.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
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
            await self._with_raw_response.post_companies_company_id_shipping_locations(
                company_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Creates an order for payment terminal products for the company identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write
        >Requests to the Management API test endpoint do not create actual orders for test terminals. To order test
        terminals, you need to `submit a sales order
        <https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps>`__ in your Customer
        Area.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
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
            await self._with_raw_response.post_companies_company_id_terminal_orders(
                company_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_companies_company_id_terminal_orders_order_id_cancel(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_companies_company_id_terminal_orders_order_id_cancel(
                company_id, order_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalOrdersCompanyLevelWithRawResponse:
        return self._with_raw_response


class TerminalOrdersCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_companies_company_id_billing_entities(
        self, company_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingEntitiesResponse, GetCompaniesCompanyIdBillingEntitiesErrorBody]:
        """Returns the billing entities of the company identified in the path and all merchant accounts belonging to the
        company. A billing entity is a legal entity where we charge orders to. An order for terminal products must
        contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/billingEntities"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[str | None]("name", name)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BillingEntitiesResponse],
            error_mapper=get_companies_company_id_billing_entities_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocationsResponse, GetCompaniesCompanyIdShippingLocationsErrorBody]:
        """Returns the shipping locations for the company identified in the path and all merchant accounts belonging to
        the company. A shipping location includes the address where orders can be delivered, and an ID which you need to
        specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/shippingLocations"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("name", name), param[int | None]("offset", offset), param[int | None]("limit", limit)
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocationsResponse],
            error_mapper=get_companies_company_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_terminal_models(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalModelsResponse, GetCompaniesCompanyIdTerminalModelsErrorBody]:
        """Returns a list of payment terminal models that the company identified in the path has access to. The response
        includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a
        list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalModels"),
            path_params=[param[str]("companyId", company_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalModelsResponse],
            error_mapper=get_companies_company_id_terminal_models_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrdersResponse, GetCompaniesCompanyIdTerminalOrdersErrorBody]:
        """Returns a lists of terminal products orders for the company identified in the path. To filter the list, use
        one or more of the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            customer_order_reference: Your purchase order number.
            status: The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped,
                Delivered.
            offset: The number of orders to skip.
            limit: The number of orders to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("customerOrderReference", customer_order_reference),
                param[str | None]("status", status),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrdersResponse],
            error_mapper=get_companies_company_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_terminal_orders_order_id(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=get_companies_company_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_terminal_products(
        self,
        company_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalProductsResponse, GetCompaniesCompanyIdTerminalProductsErrorBody]:
        """Returns a country-specific list of payment terminal packages and parts that the company identified in the
        path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalProducts"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str]("country", country),
                param[str | None]("terminalModelId", terminal_model_id),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalProductsResponse],
            error_mapper=get_companies_company_id_terminal_products_error_mapper,
            request_options=request_options,
        )

    def patch_companies_company_id_terminal_orders_order_id(
        self,
        company_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]:
        """Updates the terminal products order identified in the path. Updating is only possible while the order has the
        status **Placed**.

        The request body only needs to contain what you want to change. However, to update the products in the ``items``
        array, you must provide the entire array. For example, if the array has three items:
         To remove one item, the array must include the remaining two items. Or to add one item, the array must include
            all four items.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=patch_companies_company_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocation, PostCompaniesCompanyIdShippingLocationsErrorBody]:
        """Creates a shipping location for the company identified in the path. A shipping location defines an address
        where orders can be delivered.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/shippingLocations"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShippingLocation | ShippingLocationDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocation],
            error_mapper=post_companies_company_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersErrorBody]:
        """Creates an order for payment terminal products for the company identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write
        >Requests to the Management API test endpoint do not create actual orders for test terminals. To order test
        terminals, you need to `submit a sales order
        <https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps>`__ in your Customer
        Area.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_companies_company_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_terminal_orders_order_id_cancel(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody]:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}/cancel"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_companies_company_id_terminal_orders_order_id_cancel_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalOrdersCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_companies_company_id_billing_entities(
        self, company_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingEntitiesResponse, GetCompaniesCompanyIdBillingEntitiesErrorBody]:
        """Returns the billing entities of the company identified in the path and all merchant accounts belonging to the
        company. A billing entity is a legal entity where we charge orders to. An order for terminal products must
        contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/billingEntities"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[str | None]("name", name)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BillingEntitiesResponse],
            error_mapper=get_companies_company_id_billing_entities_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocationsResponse, GetCompaniesCompanyIdShippingLocationsErrorBody]:
        """Returns the shipping locations for the company identified in the path and all merchant accounts belonging to
        the company. A shipping location includes the address where orders can be delivered, and an ID which you need to
        specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/shippingLocations"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("name", name), param[int | None]("offset", offset), param[int | None]("limit", limit)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocationsResponse],
            error_mapper=get_companies_company_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_terminal_models(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalModelsResponse, GetCompaniesCompanyIdTerminalModelsErrorBody]:
        """Returns a list of payment terminal models that the company identified in the path has access to. The response
        includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a
        list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalModels"),
            path_params=[param[str]("companyId", company_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalModelsResponse],
            error_mapper=get_companies_company_id_terminal_models_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrdersResponse, GetCompaniesCompanyIdTerminalOrdersErrorBody]:
        """Returns a lists of terminal products orders for the company identified in the path. To filter the list, use
        one or more of the query parameters.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            customer_order_reference: Your purchase order number.
            status: The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped,
                Delivered.
            offset: The number of orders to skip.
            limit: The number of orders to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("customerOrderReference", customer_order_reference),
                param[str | None]("status", status),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrdersResponse],
            error_mapper=get_companies_company_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_terminal_orders_order_id(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=get_companies_company_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_terminal_products(
        self,
        company_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalProductsResponse, GetCompaniesCompanyIdTerminalProductsErrorBody]:
        """Returns a country-specific list of payment terminal packages and parts that the company identified in the
        path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalProducts"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str]("country", country),
                param[str | None]("terminalModelId", terminal_model_id),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalProductsResponse],
            error_mapper=get_companies_company_id_terminal_products_error_mapper,
            request_options=request_options,
        )

    async def patch_companies_company_id_terminal_orders_order_id(
        self,
        company_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]:
        """Updates the terminal products order identified in the path. Updating is only possible while the order has the
        status **Placed**.

        The request body only needs to contain what you want to change. However, to update the products in the ``items``
        array, you must provide the entire array. For example, if the array has three items:
         To remove one item, the array must include the remaining two items. Or to add one item, the array must include
            all four items.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=patch_companies_company_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_shipping_locations(
        self,
        company_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocation, PostCompaniesCompanyIdShippingLocationsErrorBody]:
        """Creates a shipping location for the company identified in the path. A shipping location defines an address
        where orders can be delivered.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/shippingLocations"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShippingLocation | ShippingLocationDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocation],
            error_mapper=post_companies_company_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_terminal_orders(
        self,
        company_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersErrorBody]:
        """Creates an order for payment terminal products for the company identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write
        >Requests to the Management API test endpoint do not create actual orders for test terminals. To order test
        terminals, you need to `submit a sales order
        <https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps>`__ in your Customer
        Area.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_companies_company_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_terminal_orders_order_id_cancel(
        self, company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody]:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/terminalOrders/{orderId}/cancel"),
            path_params=[param[str]("companyId", company_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_companies_company_id_terminal_orders_order_id_cancel_error_mapper,
            request_options=request_options,
        )
