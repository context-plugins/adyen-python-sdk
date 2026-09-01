<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentsApp — operations

Accessor: `client.payments_app` · Source: `adyen/apis/payments_app.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payments_app.get_merchants_merchant_id_payments_apps

- **Route**: `GET /merchants/{merchantId}/paymentsApps`
- **Server**: `default26`
- **Signature**: `def get_merchants_merchant_id_payments_apps(merchant_id: str, *, statuses: str | None = None, limit: int | None = 10, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `statuses` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PaymentsAppResponse`
- **Returns (raw)**: `ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdPaymentsAppsErrorBody]`
- **Error**: `GetMerchantsMerchantIdPaymentsAppsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentsAppResponse` | `adyen/models/payments_app_response.py` |
| `GetMerchantsMerchantIdPaymentsAppsErrorBody` | `adyen/errors/get_merchants_merchant_id_payments_apps_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments_app.get_merchants_merchant_id_stores_store_id_payments_apps

- **Route**: `GET /merchants/{merchantId}/stores/{storeId}/paymentsApps`
- **Server**: `default26`
- **Signature**: `def get_merchants_merchant_id_stores_store_id_payments_apps(merchant_id: str, store_id: str, *, statuses: str | None = None, limit: int | None = 10, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `store_id`
- **Params**: `merchant_id` — path `merchantId` · `store_id` — path `storeId` · `statuses` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `PaymentsAppResponse`
- **Returns (raw)**: `ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody]`
- **Error**: `GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentsAppResponse` | `adyen/models/payments_app_response.py` |
| `GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody` | `adyen/errors/get_merchants_merchant_id_stores_store_id_payments_apps_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments_app.post_merchants_merchant_id_generate_payments_app_boarding_token

- **Route**: `POST /merchants/{merchantId}/generatePaymentsAppBoardingToken`
- **Server**: `default26`
- **Signature**: `def post_merchants_merchant_id_generate_payments_app_boarding_token(merchant_id: str, body: BoardingTokenRequest | BoardingTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `body`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `BoardingTokenResponse`
- **Returns (raw)**: `ApiResult[BoardingTokenResponse, PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody]`
- **Error**: `PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BoardingTokenRequest` | `adyen/models/boarding_token_request.py` |
| `BoardingTokenRequestDict` | `adyen/models/boarding_token_request.py` |
| `BoardingTokenResponse` | `adyen/models/boarding_token_response.py` |
| `PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody` | `adyen/errors/post_merchants_merchant_id_generate_payments_app_boarding_token_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments_app.post_merchants_merchant_id_payments_apps_installation_id_revoke

- **Route**: `POST /merchants/{merchantId}/paymentsApps/{installationId}/revoke`
- **Server**: `default26`
- **Signature**: `def post_merchants_merchant_id_payments_apps_installation_id_revoke(merchant_id: str, installation_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `installation_id`
- **Params**: `merchant_id` — path `merchantId` · `installation_id` — path `installationId`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody]`
- **Error**: `PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody` | `adyen/errors/post_merchants_merchant_id_payments_apps_installation_id_revoke_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.payments_app.post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token

- **Route**: `POST /merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken`
- **Server**: `default26`
- **Signature**: `def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(merchant_id: str, store_id: str, body: BoardingTokenRequest | BoardingTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `store_id`, `body`
- **Params**: `merchant_id` — path `merchantId` · `store_id` — path `storeId` · `body` — JSON body
- **Returns (parsed)**: `BoardingTokenResponse`
- **Returns (raw)**: `ApiResult[BoardingTokenResponse, PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody]`
- **Error**: `PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BoardingTokenRequest` | `adyen/models/boarding_token_request.py` |
| `BoardingTokenRequestDict` | `adyen/models/boarding_token_request.py` |
| `BoardingTokenResponse` | `adyen/models/boarding_token_response.py` |
| `PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody` | `adyen/errors/post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

