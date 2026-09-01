<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountStoreLevel — operations

Accessor: `client.account_store_level` · Source: `adyen/apis/account_store_level.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_store_level.get_merchants_merchant_id_stores

- **Route**: `GET /merchants/{merchantId}/stores`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_stores(merchant_id: str, *, page_number: int | None = None, page_size: int | None = None, reference: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `reference` — query
- **Returns (parsed)**: `ListStoresResponse`
- **Returns (raw)**: `ApiResult[ListStoresResponse, GetMerchantsMerchantIdStoresErrorBody]`
- **Error**: `GetMerchantsMerchantIdStoresErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListStoresResponse` | `adyen/models/list_stores_response.py` |
| `GetMerchantsMerchantIdStoresErrorBody` | `adyen/errors/get_merchants_merchant_id_stores_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.get_merchants_merchant_id_stores_store_id

- **Route**: `GET /merchants/{merchantId}/stores/{storeId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_stores_store_id(merchant_id: str, store_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `store_id`
- **Params**: `merchant_id` — path `merchantId` · `store_id` — path `storeId`
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, GetMerchantsMerchantIdStoresStoreIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdStoresStoreIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Store` | `adyen/models/store.py` |
| `GetMerchantsMerchantIdStoresStoreIdErrorBody` | `adyen/errors/get_merchants_merchant_id_stores_store_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.get_stores

- **Route**: `GET /stores`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_stores(*, page_number: int | None = None, page_size: int | None = None, reference: str | None = None, merchant_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `reference` — query · `merchant_id` — query `merchantId`
- **Returns (parsed)**: `ListStoresResponse`
- **Returns (raw)**: `ApiResult[ListStoresResponse, GetStoresErrorBody]`
- **Error**: `GetStoresErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListStoresResponse` | `adyen/models/list_stores_response.py` |
| `GetStoresErrorBody` | `adyen/errors/get_stores_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.get_stores_store_id

- **Route**: `GET /stores/{storeId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_stores_store_id(store_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`
- **Params**: `store_id` — path `storeId`
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, GetStoresStoreIdErrorBody]`
- **Error**: `GetStoresStoreIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Store` | `adyen/models/store.py` |
| `GetStoresStoreIdErrorBody` | `adyen/errors/get_stores_store_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.patch_merchants_merchant_id_stores_store_id

- **Route**: `PATCH /merchants/{merchantId}/stores/{storeId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_stores_store_id(merchant_id: str, store_id: str, *, body: UpdateStoreRequest | UpdateStoreRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `store_id`
- **Params**: `merchant_id` — path `merchantId` · `store_id` — path `storeId` · `body` — JSON body
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, PatchMerchantsMerchantIdStoresStoreIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdStoresStoreIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateStoreRequest` | `adyen/models/update_store_request.py` |
| `UpdateStoreRequestDict` | `adyen/models/update_store_request.py` |
| `Store` | `adyen/models/store.py` |
| `PatchMerchantsMerchantIdStoresStoreIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_stores_store_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.patch_stores_store_id

- **Route**: `PATCH /stores/{storeId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_stores_store_id(store_id: str, *, body: UpdateStoreRequest | UpdateStoreRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`
- **Params**: `store_id` — path `storeId` · `body` — JSON body
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, PatchStoresStoreIdErrorBody]`
- **Error**: `PatchStoresStoreIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateStoreRequest` | `adyen/models/update_store_request.py` |
| `UpdateStoreRequestDict` | `adyen/models/update_store_request.py` |
| `Store` | `adyen/models/store.py` |
| `PatchStoresStoreIdErrorBody` | `adyen/errors/patch_stores_store_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.post_merchants_merchant_id_stores

- **Route**: `POST /merchants/{merchantId}/stores`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_stores(merchant_id: str, *, body: StoreCreationRequest | StoreCreationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, PostMerchantsMerchantIdStoresErrorBody]`
- **Error**: `PostMerchantsMerchantIdStoresErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoreCreationRequest` | `adyen/models/store_creation_request.py` |
| `StoreCreationRequestDict` | `adyen/models/store_creation_request.py` |
| `Store` | `adyen/models/store.py` |
| `PostMerchantsMerchantIdStoresErrorBody` | `adyen/errors/post_merchants_merchant_id_stores_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_store_level.post_stores

- **Route**: `POST /stores`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_stores(*, body: StoreCreationWithMerchantCodeRequest | StoreCreationWithMerchantCodeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Store`
- **Returns (raw)**: `ApiResult[Store, PostStoresErrorBody]`
- **Error**: `PostStoresErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoreCreationWithMerchantCodeRequest` | `adyen/models/store_creation_with_merchant_code_request.py` |
| `StoreCreationWithMerchantCodeRequestDict` | `adyen/models/store_creation_with_merchant_code_request.py` |
| `Store` | `adyen/models/store.py` |
| `PostStoresErrorBody` | `adyen/errors/post_stores_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

