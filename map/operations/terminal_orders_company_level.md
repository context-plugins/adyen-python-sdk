<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalOrdersCompanyLevel — operations

Accessor: `client.terminal_orders_company_level` · Source: `adyen/apis/terminal_orders_company_level.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_orders_company_level.get_companies_company_id_billing_entities

- **Route**: `GET /companies/{companyId}/billingEntities`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_billing_entities(company_id: str, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `name` — query
- **Returns (parsed)**: `BillingEntitiesResponse`
- **Returns (raw)**: `ApiResult[BillingEntitiesResponse, GetCompaniesCompanyIdBillingEntitiesErrorBody]`
- **Error**: `GetCompaniesCompanyIdBillingEntitiesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BillingEntitiesResponse` | `adyen/models/billing_entities_response.py` |
| `GetCompaniesCompanyIdBillingEntitiesErrorBody` | `adyen/errors/get_companies_company_id_billing_entities_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.get_companies_company_id_shipping_locations

- **Route**: `GET /companies/{companyId}/shippingLocations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_shipping_locations(company_id: str, *, name: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `name` — query · `offset` — query · `limit` — query
- **Returns (parsed)**: `ShippingLocationsResponse`
- **Returns (raw)**: `ApiResult[ShippingLocationsResponse, GetCompaniesCompanyIdShippingLocationsErrorBody]`
- **Error**: `GetCompaniesCompanyIdShippingLocationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShippingLocationsResponse` | `adyen/models/shipping_locations_response.py` |
| `GetCompaniesCompanyIdShippingLocationsErrorBody` | `adyen/errors/get_companies_company_id_shipping_locations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.get_companies_company_id_terminal_models

- **Route**: `GET /companies/{companyId}/terminalModels`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_models(company_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId`
- **Returns (parsed)**: `TerminalModelsResponse`
- **Returns (raw)**: `ApiResult[TerminalModelsResponse, GetCompaniesCompanyIdTerminalModelsErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalModelsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalModelsResponse` | `adyen/models/terminal_models_response.py` |
| `GetCompaniesCompanyIdTerminalModelsErrorBody` | `adyen/errors/get_companies_company_id_terminal_models_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.get_companies_company_id_terminal_orders

- **Route**: `GET /companies/{companyId}/terminalOrders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_orders(company_id: str, *, customer_order_reference: str | None = None, status: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `customer_order_reference` — query `customerOrderReference` · `status` — query · `offset` — query · `limit` — query
- **Returns (parsed)**: `TerminalOrdersResponse`
- **Returns (raw)**: `ApiResult[TerminalOrdersResponse, GetCompaniesCompanyIdTerminalOrdersErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrdersResponse` | `adyen/models/terminal_orders_response.py` |
| `GetCompaniesCompanyIdTerminalOrdersErrorBody` | `adyen/errors/get_companies_company_id_terminal_orders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.get_companies_company_id_terminal_orders_order_id

- **Route**: `GET /companies/{companyId}/terminalOrders/{orderId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_orders_order_id(company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `order_id`
- **Params**: `company_id` — path `companyId` · `order_id` — path `orderId`
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `GetCompaniesCompanyIdTerminalOrdersOrderIdErrorBody` | `adyen/errors/get_companies_company_id_terminal_orders_order_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.get_companies_company_id_terminal_products

- **Route**: `GET /companies/{companyId}/terminalProducts`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_products(company_id: str, country: str, *, terminal_model_id: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `country`
- **Params**: `company_id` — path `companyId` · `country` — query · `terminal_model_id` — query `terminalModelId` · `offset` — query · `limit` — query
- **Returns (parsed)**: `TerminalProductsResponse`
- **Returns (raw)**: `ApiResult[TerminalProductsResponse, GetCompaniesCompanyIdTerminalProductsErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalProductsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalProductsResponse` | `adyen/models/terminal_products_response.py` |
| `GetCompaniesCompanyIdTerminalProductsErrorBody` | `adyen/errors/get_companies_company_id_terminal_products_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.patch_companies_company_id_terminal_orders_order_id

- **Route**: `PATCH /companies/{companyId}/terminalOrders/{orderId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_terminal_orders_order_id(company_id: str, order_id: str, *, body: TerminalOrderRequest | TerminalOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `order_id`
- **Params**: `company_id` — path `companyId` · `order_id` — path `orderId` · `body` — JSON body
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrderRequest` | `adyen/models/terminal_order_request.py` |
| `TerminalOrderRequestDict` | `adyen/models/terminal_order_request.py` |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PatchCompaniesCompanyIdTerminalOrdersOrderIdErrorBody` | `adyen/errors/patch_companies_company_id_terminal_orders_order_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.post_companies_company_id_shipping_locations

- **Route**: `POST /companies/{companyId}/shippingLocations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_shipping_locations(company_id: str, *, body: ShippingLocation | ShippingLocationDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `ShippingLocation`
- **Returns (raw)**: `ApiResult[ShippingLocation, PostCompaniesCompanyIdShippingLocationsErrorBody]`
- **Error**: `PostCompaniesCompanyIdShippingLocationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShippingLocation` | `adyen/models/shipping_location.py` |
| `ShippingLocationDict` | `adyen/models/shipping_location.py` |
| `PostCompaniesCompanyIdShippingLocationsErrorBody` | `adyen/errors/post_companies_company_id_shipping_locations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.post_companies_company_id_terminal_orders

- **Route**: `POST /companies/{companyId}/terminalOrders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_terminal_orders(company_id: str, *, body: TerminalOrderRequest | TerminalOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersErrorBody]`
- **Error**: `PostCompaniesCompanyIdTerminalOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrderRequest` | `adyen/models/terminal_order_request.py` |
| `TerminalOrderRequestDict` | `adyen/models/terminal_order_request.py` |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PostCompaniesCompanyIdTerminalOrdersErrorBody` | `adyen/errors/post_companies_company_id_terminal_orders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_orders_company_level.post_companies_company_id_terminal_orders_order_id_cancel

- **Route**: `POST /companies/{companyId}/terminalOrders/{orderId}/cancel`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_terminal_orders_order_id_cancel(company_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `order_id`
- **Params**: `company_id` — path `companyId` · `order_id` — path `orderId`
- **Returns (parsed)**: `TerminalOrder`
- **Returns (raw)**: `ApiResult[TerminalOrder, PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody]`
- **Error**: `PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalOrder` | `adyen/models/terminal_order.py` |
| `PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody` | `adyen/errors/post_companies_company_id_terminal_orders_order_id_cancel_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

