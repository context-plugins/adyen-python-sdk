<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountMerchantLevel — operations

Accessor: `client.account_merchant_level` · Source: `adyen/apis/account_merchant_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_merchant_level.get_merchants

- **Route**: `GET /merchants`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants(*, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListMerchantResponse`
- **Returns (raw)**: `ApiResult[ListMerchantResponse, GetMerchantsErrorBody]`
- **Error**: `GetMerchantsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMerchantResponse` | `adyen/models/list_merchant_response.py` |
| `GetMerchantsErrorBody` | `adyen/errors/get_merchants_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_merchant_level.get_merchants_merchant_id

- **Route**: `GET /merchants/{merchantId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `Merchant`
- **Returns (raw)**: `ApiResult[Merchant, GetMerchantsMerchantIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Merchant` | `adyen/models/merchant.py` |
| `GetMerchantsMerchantIdErrorBody` | `adyen/errors/get_merchants_merchant_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_merchant_level.post_merchants

- **Route**: `POST /merchants`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants(*, body: CreateMerchantRequest | CreateMerchantRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateMerchantResponse`
- **Returns (raw)**: `ApiResult[CreateMerchantResponse, PostMerchantsErrorBody]`
- **Error**: `PostMerchantsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMerchantRequest` | `adyen/models/create_merchant_request.py` |
| `CreateMerchantRequestDict` | `adyen/models/create_merchant_request.py` |
| `CreateMerchantResponse` | `adyen/models/create_merchant_response.py` |
| `PostMerchantsErrorBody` | `adyen/errors/post_merchants_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_merchant_level.post_merchants_merchant_id_activate

- **Route**: `POST /merchants/{merchantId}/activate`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_activate(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `RequestActivationResponse`
- **Returns (raw)**: `ApiResult[RequestActivationResponse, PostMerchantsMerchantIdActivateErrorBody]`
- **Error**: `PostMerchantsMerchantIdActivateErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RequestActivationResponse` | `adyen/models/request_activation_response.py` |
| `PostMerchantsMerchantIdActivateErrorBody` | `adyen/errors/post_merchants_merchant_id_activate_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

