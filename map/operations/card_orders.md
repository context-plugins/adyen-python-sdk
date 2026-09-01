<!-- Generated file — do not edit; regenerated with the SDK. -->

# CardOrders — operations

Accessor: `client.card_orders` · Source: `adyen/apis/card_orders.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.card_orders.get_cardorders

- **Route**: `GET /cardorders`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_cardorders(*, id: str | None = None, card_manufacturing_profile_id: str | None = None, status: str | None = None, tx_variant_code: str | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, locked_since: RFC3339DateTime | None = None, locked_until: RFC3339DateTime | None = None, service_center: str | None = None, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — query · `card_manufacturing_profile_id` — query `cardManufacturingProfileId` · `status` — query · `tx_variant_code` — query `txVariantCode` · `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `locked_since` — query `lockedSince` · `locked_until` — query `lockedUntil` · `service_center` — query `serviceCenter` · `offset` — query · `limit` — query
- **Returns (parsed)**: `PaginatedGetCardOrderResponse`
- **Returns (raw)**: `ApiResult[PaginatedGetCardOrderResponse, GetCardordersErrorBody]`
- **Error**: `GetCardordersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedGetCardOrderResponse` | `adyen/models/paginated_get_card_order_response.py` |
| `GetCardordersErrorBody` | `adyen/errors/get_cardorders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.card_orders.get_cardorders_id_items

- **Route**: `GET /cardorders/{id}/items`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_cardorders_id_items(id: str, *, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `offset` — query · `limit` — query
- **Returns (parsed)**: `PaginatedGetCardOrderItemResponse`
- **Returns (raw)**: `ApiResult[PaginatedGetCardOrderItemResponse, GetCardordersIdItemsErrorBody]`
- **Error**: `GetCardordersIdItemsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedGetCardOrderItemResponse` | `adyen/models/paginated_get_card_order_item_response.py` |
| `GetCardordersIdItemsErrorBody` | `adyen/errors/get_cardorders_id_items_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

