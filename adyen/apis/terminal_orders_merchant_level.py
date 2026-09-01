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
from ..errors.get_merchants_merchant_id_billing_entities_error import (
    GetMerchantsMerchantIdBillingEntitiesErrorBody,
    get_merchants_merchant_id_billing_entities_error_mapper,
)
from ..errors.get_merchants_merchant_id_shipping_locations_error import (
    GetMerchantsMerchantIdShippingLocationsErrorBody,
    get_merchants_merchant_id_shipping_locations_error_mapper,
)
from ..errors.get_merchants_merchant_id_terminal_models_error import (
    GetMerchantsMerchantIdTerminalModelsErrorBody,
    get_merchants_merchant_id_terminal_models_error_mapper,
)
from ..errors.get_merchants_merchant_id_terminal_orders_error import (
    GetMerchantsMerchantIdTerminalOrdersErrorBody,
    get_merchants_merchant_id_terminal_orders_error_mapper,
)
from ..errors.get_merchants_merchant_id_terminal_orders_order_id_error import (
    GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody,
    get_merchants_merchant_id_terminal_orders_order_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_terminal_products_error import (
    GetMerchantsMerchantIdTerminalProductsErrorBody,
    get_merchants_merchant_id_terminal_products_error_mapper,
)
from ..errors.patch_merchants_merchant_id_terminal_orders_order_id_error import (
    PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody,
    patch_merchants_merchant_id_terminal_orders_order_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_shipping_locations_error import (
    PostMerchantsMerchantIdShippingLocationsErrorBody,
    post_merchants_merchant_id_shipping_locations_error_mapper,
)
from ..errors.post_merchants_merchant_id_terminal_orders_error import (
    PostMerchantsMerchantIdTerminalOrdersErrorBody,
    post_merchants_merchant_id_terminal_orders_error_mapper,
)
from ..errors.post_merchants_merchant_id_terminal_orders_order_id_cancel_error import (
    PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody,
    post_merchants_merchant_id_terminal_orders_order_id_cancel_error_mapper,
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


class TerminalOrdersMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalOrdersMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_billing_entities(
        self, merchant_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> BillingEntitiesResponse:
        """Returns the billing entities of the merchant account identified in the path. A billing entity is a legal
        entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_billing_entities(
            merchant_id, name=name, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocationsResponse:
        """Returns the shipping locations for the merchant account identified in the path. A shipping location includes
        the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
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
        return self._with_raw_response.get_merchants_merchant_id_shipping_locations(
            merchant_id, name=name, offset=offset, limit=limit, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_terminal_models(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalModelsResponse:
        """Returns the payment terminal models that the merchant account identified in the path has access to. The
        response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals
        or a list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
        return self._with_raw_response.get_merchants_merchant_id_terminal_models(
            merchant_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrdersResponse:
        """Returns a list of terminal products orders for the merchant account identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: Value sent with the request.
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
        return self._with_raw_response.get_merchants_merchant_id_terminal_orders(
            merchant_id,
            customer_order_reference=customer_order_reference,
            status=status,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def get_merchants_merchant_id_terminal_orders_order_id(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_terminal_orders_order_id(
            merchant_id, order_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_terminal_products(
        self,
        merchant_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalProductsResponse:
        """Returns a country-specific list of payment terminal packages and parts that the merchant account identified
        in the path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels
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
        return self._with_raw_response.get_merchants_merchant_id_terminal_products(
            merchant_id,
            country,
            terminal_model_id=terminal_model_id,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def patch_merchants_merchant_id_terminal_orders_order_id(
        self,
        merchant_id: str,
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
            merchant_id: The unique identifier of the merchant account.
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
        return self._with_raw_response.patch_merchants_merchant_id_terminal_orders_order_id(
            merchant_id, order_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocation:
        """Creates a shipping location for the merchant account identified in the path. A shipping location defines an
        address where orders can be shipped to.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

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
        return self._with_raw_response.post_merchants_merchant_id_shipping_locations(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Creates an order for payment terminal products for the merchant account identified in the path.

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
        return self._with_raw_response.post_merchants_merchant_id_terminal_orders(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_terminal_orders_order_id_cancel(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
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
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_terminal_orders_order_id_cancel(
            merchant_id, order_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TerminalOrdersMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalOrdersMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalOrdersMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_billing_entities(
        self, merchant_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> BillingEntitiesResponse:
        """Returns the billing entities of the merchant account identified in the path. A billing entity is a legal
        entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.get_merchants_merchant_id_billing_entities(
                merchant_id, name=name, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocationsResponse:
        """Returns the shipping locations for the merchant account identified in the path. A shipping location includes
        the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.get_merchants_merchant_id_shipping_locations(
                merchant_id, name=name, offset=offset, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_terminal_models(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalModelsResponse:
        """Returns the payment terminal models that the merchant account identified in the path has access to. The
        response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals
        or a list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

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
            await self._with_raw_response.get_merchants_merchant_id_terminal_models(
                merchant_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrdersResponse:
        """Returns a list of terminal products orders for the merchant account identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: Value sent with the request.
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
            await self._with_raw_response.get_merchants_merchant_id_terminal_orders(
                merchant_id,
                customer_order_reference=customer_order_reference,
                status=status,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def get_merchants_merchant_id_terminal_orders_order_id(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalOrder:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.get_merchants_merchant_id_terminal_orders_order_id(
                merchant_id, order_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_terminal_products(
        self,
        merchant_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalProductsResponse:
        """Returns a country-specific list of payment terminal packages and parts that the merchant account identified
        in the path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels
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
            await self._with_raw_response.get_merchants_merchant_id_terminal_products(
                merchant_id,
                country,
                terminal_model_id=terminal_model_id,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_merchants_merchant_id_terminal_orders_order_id(
        self,
        merchant_id: str,
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
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.patch_merchants_merchant_id_terminal_orders_order_id(
                merchant_id, order_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShippingLocation:
        """Creates a shipping location for the merchant account identified in the path. A shipping location defines an
        address where orders can be shipped to.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

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
            await self._with_raw_response.post_merchants_merchant_id_shipping_locations(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalOrder:
        """Creates an order for payment terminal products for the merchant account identified in the path.

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
            await self._with_raw_response.post_merchants_merchant_id_terminal_orders(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_terminal_orders_order_id_cancel(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
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
            merchant_id: The unique identifier of the merchant account.
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
            await self._with_raw_response.post_merchants_merchant_id_terminal_orders_order_id_cancel(
                merchant_id, order_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalOrdersMerchantLevelWithRawResponse:
        return self._with_raw_response


class TerminalOrdersMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_billing_entities(
        self, merchant_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingEntitiesResponse, GetMerchantsMerchantIdBillingEntitiesErrorBody]:
        """Returns the billing entities of the merchant account identified in the path. A billing entity is a legal
        entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/billingEntities"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str | None]("name", name)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BillingEntitiesResponse],
            error_mapper=get_merchants_merchant_id_billing_entities_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocationsResponse, GetMerchantsMerchantIdShippingLocationsErrorBody]:
        """Returns the shipping locations for the merchant account identified in the path. A shipping location includes
        the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/shippingLocations"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("name", name), param[int | None]("offset", offset), param[int | None]("limit", limit)
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocationsResponse],
            error_mapper=get_merchants_merchant_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_terminal_models(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalModelsResponse, GetMerchantsMerchantIdTerminalModelsErrorBody]:
        """Returns the payment terminal models that the merchant account identified in the path has access to. The
        response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals
        or a list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalModels"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalModelsResponse],
            error_mapper=get_merchants_merchant_id_terminal_models_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrdersResponse, GetMerchantsMerchantIdTerminalOrdersErrorBody]:
        """Returns a list of terminal products orders for the merchant account identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: Value sent with the request.
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
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("customerOrderReference", customer_order_reference),
                param[str | None]("status", status),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrdersResponse],
            error_mapper=get_merchants_merchant_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_terminal_orders_order_id(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=get_merchants_merchant_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_terminal_products(
        self,
        merchant_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalProductsResponse, GetMerchantsMerchantIdTerminalProductsErrorBody]:
        """Returns a country-specific list of payment terminal packages and parts that the merchant account identified
        in the path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalProducts"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str]("country", country),
                param[str | None]("terminalModelId", terminal_model_id),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalProductsResponse],
            error_mapper=get_merchants_merchant_id_terminal_products_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_terminal_orders_order_id(
        self,
        merchant_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]:
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
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=patch_merchants_merchant_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocation, PostMerchantsMerchantIdShippingLocationsErrorBody]:
        """Creates a shipping location for the merchant account identified in the path. A shipping location defines an
        address where orders can be shipped to.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

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
            url_template=self._server.default9("/merchants/{merchantId}/shippingLocations"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShippingLocation | ShippingLocationDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocation],
            error_mapper=post_merchants_merchant_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersErrorBody]:
        """Creates an order for payment terminal products for the merchant account identified in the path.

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
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_merchants_merchant_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_terminal_orders_order_id_cancel(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody]:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}/cancel"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_merchants_merchant_id_terminal_orders_order_id_cancel_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalOrdersMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_billing_entities(
        self, merchant_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingEntitiesResponse, GetMerchantsMerchantIdBillingEntitiesErrorBody]:
        """Returns the billing entities of the merchant account identified in the path. A billing entity is a legal
        entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            name: The name of the billing entity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/billingEntities"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str | None]("name", name)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BillingEntitiesResponse],
            error_mapper=get_merchants_merchant_id_billing_entities_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        name: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocationsResponse, GetMerchantsMerchantIdShippingLocationsErrorBody]:
        """Returns the shipping locations for the merchant account identified in the path. A shipping location includes
        the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            name: The name of the shipping location.
            offset: The number of locations to skip.
            limit: The number of locations to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/shippingLocations"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("name", name), param[int | None]("offset", offset), param[int | None]("limit", limit)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocationsResponse],
            error_mapper=get_merchants_merchant_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_terminal_models(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalModelsResponse, GetMerchantsMerchantIdTerminalModelsErrorBody]:
        """Returns the payment terminal models that the merchant account identified in the path has access to. The
        response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals
        or a list of products for ordering.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalModels"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalModelsResponse],
            error_mapper=get_merchants_merchant_id_terminal_models_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        customer_order_reference: str | None = None,
        status: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrdersResponse, GetMerchantsMerchantIdTerminalOrdersErrorBody]:
        """Returns a list of terminal products orders for the merchant account identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: Value sent with the request.
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
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("customerOrderReference", customer_order_reference),
                param[str | None]("status", status),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrdersResponse],
            error_mapper=get_merchants_merchant_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_terminal_orders_order_id(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]:
        """Returns the details of the terminal products order identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=get_merchants_merchant_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_terminal_products(
        self,
        merchant_id: str,
        country: str,
        *,
        terminal_model_id: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalProductsResponse, GetMerchantsMerchantIdTerminalProductsErrorBody]:
        """Returns a country-specific list of payment terminal packages and parts that the merchant account identified
        in the path has access to.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            country: The country to return products for, in `ISO 3166-1 alpha-2
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **US**
            terminal_model_id: The terminal model to return products for. Use the ID returned in the
                https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels
                response. For example, **Verifone.M400**
            offset: The number of products to skip.
            limit: The number of products to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalProducts"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str]("country", country),
                param[str | None]("terminalModelId", terminal_model_id),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalProductsResponse],
            error_mapper=get_merchants_merchant_id_terminal_products_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_terminal_orders_order_id(
        self,
        merchant_id: str,
        order_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]:
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
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=patch_merchants_merchant_id_terminal_orders_order_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_shipping_locations(
        self,
        merchant_id: str,
        *,
        body: ShippingLocation | ShippingLocationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShippingLocation, PostMerchantsMerchantIdShippingLocationsErrorBody]:
        """Creates a shipping location for the merchant account identified in the path. A shipping location defines an
        address where orders can be shipped to.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

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
            url_template=self._server.default9("/merchants/{merchantId}/shippingLocations"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShippingLocation | ShippingLocationDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ShippingLocation],
            error_mapper=post_merchants_merchant_id_shipping_locations_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_terminal_orders(
        self,
        merchant_id: str,
        *,
        body: TerminalOrderRequest | TerminalOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersErrorBody]:
        """Creates an order for payment terminal products for the merchant account identified in the path.

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
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalOrderRequest | TerminalOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_merchants_merchant_id_terminal_orders_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_terminal_orders_order_id_cancel(
        self, merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody]:
        """Cancels the terminal products order identified in the path. Cancelling is only possible while the order has
        the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the
        full order details, but with the status changed to **Cancelled**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal ordering read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            order_id: The unique identifier of the order.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/terminalOrders/{orderId}/cancel"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("orderId", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalOrder],
            error_mapper=post_merchants_merchant_id_terminal_orders_order_id_cancel_error_mapper,
            request_options=request_options,
        )
