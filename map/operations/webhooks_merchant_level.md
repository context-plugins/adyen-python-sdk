<!-- Generated file — do not edit; regenerated with the SDK. -->

# WebhooksMerchantLevel — operations

Accessor: `client.webhooks_merchant_level` · Source: `adyen/apis/webhooks_merchant_level.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.webhooks_merchant_level.delete_merchants_merchant_id_webhooks_webhook_id

- **Route**: `DELETE /merchants/{merchantId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_merchants_merchant_id_webhooks_webhook_id(merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `webhook_id`
- **Params**: `merchant_id` — path `merchantId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody]`
- **Error**: `DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody` | `adyen/errors/delete_merchants_merchant_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.get_merchants_merchant_id_webhooks

- **Route**: `GET /merchants/{merchantId}/webhooks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_webhooks(merchant_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListWebhooksResponse`
- **Returns (raw)**: `ApiResult[ListWebhooksResponse, GetMerchantsMerchantIdWebhooksErrorBody]`
- **Error**: `GetMerchantsMerchantIdWebhooksErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListWebhooksResponse` | `adyen/models/list_webhooks_response.py` |
| `GetMerchantsMerchantIdWebhooksErrorBody` | `adyen/errors/get_merchants_merchant_id_webhooks_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.get_merchants_merchant_id_webhooks_webhook_id

- **Route**: `GET /merchants/{merchantId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_webhooks_webhook_id(merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `webhook_id`
- **Params**: `merchant_id` — path `merchantId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, GetMerchantsMerchantIdWebhooksWebhookIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Webhook` | `adyen/models/webhook.py` |
| `GetMerchantsMerchantIdWebhooksWebhookIdErrorBody` | `adyen/errors/get_merchants_merchant_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.patch_merchants_merchant_id_webhooks_webhook_id

- **Route**: `PATCH /merchants/{merchantId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_webhooks_webhook_id(merchant_id: str, webhook_id: str, *, body: UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `webhook_id`
- **Params**: `merchant_id` — path `merchantId` · `webhook_id` — path `webhookId` · `body` — JSON body
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateMerchantWebhookRequest` | `adyen/models/update_merchant_webhook_request.py` |
| `UpdateMerchantWebhookRequestDict` | `adyen/models/update_merchant_webhook_request.py` |
| `Webhook` | `adyen/models/webhook.py` |
| `PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.post_merchants_merchant_id_webhooks

- **Route**: `POST /merchants/{merchantId}/webhooks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_webhooks(merchant_id: str, *, body: CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, PostMerchantsMerchantIdWebhooksErrorBody]`
- **Error**: `PostMerchantsMerchantIdWebhooksErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMerchantWebhookRequest` | `adyen/models/create_merchant_webhook_request.py` |
| `CreateMerchantWebhookRequestDict` | `adyen/models/create_merchant_webhook_request.py` |
| `Webhook` | `adyen/models/webhook.py` |
| `PostMerchantsMerchantIdWebhooksErrorBody` | `adyen/errors/post_merchants_merchant_id_webhooks_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.post_merchants_merchant_id_webhooks_webhook_id_generate_hmac

- **Route**: `POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `webhook_id`
- **Params**: `merchant_id` — path `merchantId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `GenerateHmacKeyResponse`
- **Returns (raw)**: `ApiResult[GenerateHmacKeyResponse, PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody]`
- **Error**: `PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateHmacKeyResponse` | `adyen/models/generate_hmac_key_response.py` |
| `PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody` | `adyen/errors/post_merchants_merchant_id_webhooks_webhook_id_generate_hmac_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_merchant_level.post_merchants_merchant_id_webhooks_webhook_id_test

- **Route**: `POST /merchants/{merchantId}/webhooks/{webhookId}/test`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_webhooks_webhook_id_test(merchant_id: str, webhook_id: str, *, body: TestWebhookRequest | TestWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `webhook_id`
- **Params**: `merchant_id` — path `merchantId` · `webhook_id` — path `webhookId` · `body` — JSON body
- **Returns (parsed)**: `TestWebhookResponse`
- **Returns (raw)**: `ApiResult[TestWebhookResponse, PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody]`
- **Error**: `PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TestWebhookRequest` | `adyen/models/test_webhook_request.py` |
| `TestWebhookRequestDict` | `adyen/models/test_webhook_request.py` |
| `TestWebhookResponse` | `adyen/models/test_webhook_response.py` |
| `PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody` | `adyen/errors/post_merchants_merchant_id_webhooks_webhook_id_test_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

