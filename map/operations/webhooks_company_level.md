<!-- Generated file — do not edit; regenerated with the SDK. -->

# WebhooksCompanyLevel — operations

Accessor: `client.webhooks_company_level` · Source: `adyen/apis/webhooks_company_level.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.webhooks_company_level.delete_companies_company_id_webhooks_webhook_id

- **Route**: `DELETE /companies/{companyId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_companies_company_id_webhooks_webhook_id(company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `webhook_id`
- **Params**: `company_id` — path `companyId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody]`
- **Error**: `DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody` | `adyen/errors/delete_companies_company_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.get_companies_company_id_webhooks

- **Route**: `GET /companies/{companyId}/webhooks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_webhooks(company_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListWebhooksResponse`
- **Returns (raw)**: `ApiResult[ListWebhooksResponse, GetCompaniesCompanyIdWebhooksErrorBody]`
- **Error**: `GetCompaniesCompanyIdWebhooksErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListWebhooksResponse` | `adyen/models/list_webhooks_response.py` |
| `GetCompaniesCompanyIdWebhooksErrorBody` | `adyen/errors/get_companies_company_id_webhooks_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.get_companies_company_id_webhooks_webhook_id

- **Route**: `GET /companies/{companyId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_webhooks_webhook_id(company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `webhook_id`
- **Params**: `company_id` — path `companyId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, GetCompaniesCompanyIdWebhooksWebhookIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Webhook` | `adyen/models/webhook.py` |
| `GetCompaniesCompanyIdWebhooksWebhookIdErrorBody` | `adyen/errors/get_companies_company_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.patch_companies_company_id_webhooks_webhook_id

- **Route**: `PATCH /companies/{companyId}/webhooks/{webhookId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_webhooks_webhook_id(company_id: str, webhook_id: str, *, body: UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `webhook_id`
- **Params**: `company_id` — path `companyId` · `webhook_id` — path `webhookId` · `body` — JSON body
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateCompanyWebhookRequest` | `adyen/models/update_company_webhook_request.py` |
| `UpdateCompanyWebhookRequestDict` | `adyen/models/update_company_webhook_request.py` |
| `Webhook` | `adyen/models/webhook.py` |
| `PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody` | `adyen/errors/patch_companies_company_id_webhooks_webhook_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.post_companies_company_id_webhooks

- **Route**: `POST /companies/{companyId}/webhooks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_webhooks(company_id: str, *, body: CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `Webhook`
- **Returns (raw)**: `ApiResult[Webhook, PostCompaniesCompanyIdWebhooksErrorBody]`
- **Error**: `PostCompaniesCompanyIdWebhooksErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateCompanyWebhookRequest` | `adyen/models/create_company_webhook_request.py` |
| `CreateCompanyWebhookRequestDict` | `adyen/models/create_company_webhook_request.py` |
| `Webhook` | `adyen/models/webhook.py` |
| `PostCompaniesCompanyIdWebhooksErrorBody` | `adyen/errors/post_companies_company_id_webhooks_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.post_companies_company_id_webhooks_webhook_id_generate_hmac

- **Route**: `POST /companies/{companyId}/webhooks/{webhookId}/generateHmac`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_webhooks_webhook_id_generate_hmac(company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `webhook_id`
- **Params**: `company_id` — path `companyId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `GenerateHmacKeyResponse`
- **Returns (raw)**: `ApiResult[GenerateHmacKeyResponse, PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody]`
- **Error**: `PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateHmacKeyResponse` | `adyen/models/generate_hmac_key_response.py` |
| `PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody` | `adyen/errors/post_companies_company_id_webhooks_webhook_id_generate_hmac_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.webhooks_company_level.post_companies_company_id_webhooks_webhook_id_test

- **Route**: `POST /companies/{companyId}/webhooks/{webhookId}/test`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_webhooks_webhook_id_test(company_id: str, webhook_id: str, *, body: TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `webhook_id`
- **Params**: `company_id` — path `companyId` · `webhook_id` — path `webhookId` · `body` — JSON body
- **Returns (parsed)**: `TestWebhookResponse`
- **Returns (raw)**: `ApiResult[TestWebhookResponse, PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody]`
- **Error**: `PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TestCompanyWebhookRequest` | `adyen/models/test_company_webhook_request.py` |
| `TestCompanyWebhookRequestDict` | `adyen/models/test_company_webhook_request.py` |
| `TestWebhookResponse` | `adyen/models/test_webhook_response.py` |
| `PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody` | `adyen/errors/post_companies_company_id_webhooks_webhook_id_test_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

