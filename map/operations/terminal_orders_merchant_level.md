<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalOrdersMerchantLevel — operations

Accessor: `client.terminal_orders_merchant_level` · Source: `adyen/apis/terminal_orders_merchant_level.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_orders_merchant_level.get_merchants_merchant_id_billing_entities

- **Route**: `GET /merchants/{merchantId}/billingEntities`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_billing_entities(merchant_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `name` — query
- **Returns (parsed)**: `BillingEntitiesResponse`
- **Returns (raw)**: `ApiResult[BillingEntitiesResponse, GetMerchantsMerchantIdBillingEntitiesErrorBody]`
- **Error**: `GetMerchantsMerchantIdBillingEntitiesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BillingEntitiesResponse` | `adyen/models/billing_entities_response.py` |
| `GetMerchantsMerchantIdBillingEntitiesErrorBody` | `adyen/errors/get_merchants_merchant_id_billing_entities_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.get_merchants_merchant_id_shipping_locations

- **Route**: `GET /merchants/{merchantId}/shippingLocations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_shipping_locations(merchant_id: str, *, name: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `name` — query · `offset` — query · `limit` — query
- **Returns (parsed)**: `ShippingLocationsResponse`
- **Returns (raw)**: `ApiResult[ShippingLocationsResponse, GetMerchantsMerchantIdShippingLocationsErrorBody]`
- **Error**: `GetMerchantsMerchantIdShippingLocationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShippingLocationsResponse` | `adyen/models/shipping_locations_response.py` |
| `GetMerchantsMerchantIdShippingLocationsErrorBody` | `adyen/errors/get_merchants_merchant_id_shipping_locations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.get_merchants_merchant_id_terminal_models

- **Route**: `GET /merchants/{merchantId}/terminalModels`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_models(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `TerminalModelsResponse`
- **Returns (raw)**: `ApiResult[TerminalModelsResponse, GetMerchantsMerchantIdTerminalModelsErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalModelsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalModelsResponse` | `adyen/models/terminal_models_response.py` |
| `GetMerchantsMerchantIdTerminalModelsErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_models_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.get_merchants_merchant_id_terminal_orders

- **Route**: `GET /merchants/{merchantId}/terminalOrders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_orders(merchant_id: str, *, customer_order_reference: str | None = None, status: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `customer_order_reference` — query `customerOrderReference` · `status` — query · `offset` — query · `limit` — query
- **Returns (parsed)**: `TerminalOrdersResponse`
- **Returns (raw)**: `ApiResult[TerminalOrdersResponse, GetMerchantsMerchantIdTerminalOrdersErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrdersResponse` | `adyen/models/terminal_orders_response.py` |
| `GetMerchantsMerchantIdTerminalOrdersErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_orders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.get_merchants_merchant_id_terminal_orders_order_id

- **Route**: `GET /merchants/{merchantId}/terminalOrders/{orderId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_orders_order_id(merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `order_id`
- **Params**: `merchant_id` — path `merchantId` · `order_id` — path `orderId`
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `GetMerchantsMerchantIdTerminalOrdersOrderIdErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_orders_order_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.get_merchants_merchant_id_terminal_products

- **Route**: `GET /merchants/{merchantId}/terminalProducts`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_products(merchant_id: str, country: str, *, terminal_model_id: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `country`
- **Params**: `merchant_id` — path `merchantId` · `country` — query · `terminal_model_id` — query `terminalModelId` · `offset` — query · `limit` — query
- **Returns (parsed)**: `TerminalProductsResponse`
- **Returns (raw)**: `ApiResult[TerminalProductsResponse, GetMerchantsMerchantIdTerminalProductsErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalProductsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalProductsResponse` | `adyen/models/terminal_products_response.py` |
| `GetMerchantsMerchantIdTerminalProductsErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_products_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.patch_merchants_merchant_id_terminal_orders_order_id

- **Route**: `PATCH /merchants/{merchantId}/terminalOrders/{orderId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_terminal_orders_order_id(merchant_id: str, order_id: str, *, body: TerminalOrderRequest | TerminalOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `order_id`
- **Params**: `merchant_id` — path `merchantId` · `order_id` — path `orderId` · `body` — JSON body
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrderRequest` | `adyen/models/terminal_order_request.py` |
| `TerminalOrderRequestDict` | `adyen/models/terminal_order_request.py` |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PatchMerchantsMerchantIdTerminalOrdersOrderIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_terminal_orders_order_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.post_merchants_merchant_id_shipping_locations

- **Route**: `POST /merchants/{merchantId}/shippingLocations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_shipping_locations(merchant_id: str, *, body: ShippingLocation | ShippingLocationDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `ShippingLocation`
- **Returns (raw)**: `ApiResult[ShippingLocation, PostMerchantsMerchantIdShippingLocationsErrorBody]`
- **Error**: `PostMerchantsMerchantIdShippingLocationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShippingLocation` | `adyen/models/shipping_location.py` |
| `ShippingLocationDict` | `adyen/models/shipping_location.py` |
| `PostMerchantsMerchantIdShippingLocationsErrorBody` | `adyen/errors/post_merchants_merchant_id_shipping_locations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.post_merchants_merchant_id_terminal_orders

- **Route**: `POST /merchants/{merchantId}/terminalOrders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_terminal_orders(merchant_id: str, *, body: TerminalOrderRequest | TerminalOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersErrorBody]`
- **Error**: `PostMerchantsMerchantIdTerminalOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrderRequest` | `adyen/models/terminal_order_request.py` |
| `TerminalOrderRequestDict` | `adyen/models/terminal_order_request.py` |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PostMerchantsMerchantIdTerminalOrdersErrorBody` | `adyen/errors/post_merchants_merchant_id_terminal_orders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_merchant_level.post_merchants_merchant_id_terminal_orders_order_id_cancel

- **Route**: `POST /merchants/{merchantId}/terminalOrders/{orderId}/cancel`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_terminal_orders_order_id_cancel(merchant_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `order_id`
- **Params**: `merchant_id` — path `merchantId` · `order_id` — path `orderId`
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody]`
- **Error**: `PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PostMerchantsMerchantIdTerminalOrdersOrderIdCancelErrorBody` | `adyen/errors/post_merchants_merchant_id_terminal_orders_order_id_cancel_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

