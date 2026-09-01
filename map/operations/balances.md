<!-- Generated file — do not edit; regenerated with the SDK. -->

# Balances — operations

Accessor: `client.balances` · Source: `adyen/apis/balances.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.balances.delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id

- **Route**: `DELETE /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}`
- **Server**: `default13`
- **Signature**: `def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(balance_platform_id: str, webhook_id: str, setting_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `webhook_id`, `setting_id`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `webhook_id` — path `webhookId` · `setting_id` — path `settingId`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]`
- **Error**: `DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` | `adyen/errors/delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.balances.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings

- **Route**: `GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(balance_platform_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `webhook_id`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `webhook_id` — path `webhookId`
- **Returns (parsed)**: `WebhookSettings`
- **Returns (raw)**: `ApiResult[WebhookSettings, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]`
- **Error**: `GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WebhookSettings` | `adyen/models/webhook_settings.py` |
| `GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody` | `adyen/errors/get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.balances.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id

- **Route**: `GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(balance_platform_id: str, webhook_id: str, setting_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `webhook_id`, `setting_id`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `webhook_id` — path `webhookId` · `setting_id` — path `settingId`
- **Returns (parsed)**: `WebhookSetting`
- **Returns (raw)**: `ApiResult[WebhookSetting, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]`
- **Error**: `GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WebhookSetting` | `adyen/models/unions/webhook_setting.py` |
| `GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` | `adyen/errors/get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.balances.patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id

- **Route**: `PATCH /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}`
- **Server**: `default13`
- **Signature**: `def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(balance_platform_id: str, webhook_id: str, setting_id: str, body: BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `webhook_id`, `setting_id`, `body`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `webhook_id` — path `webhookId` · `setting_id` — path `settingId` · `body` — JSON body
- **Returns (parsed)**: `WebhookSetting`
- **Returns (raw)**: `ApiResult[WebhookSetting, PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]`
- **Error**: `PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceWebhookSettingInfoUpdate` | `adyen/models/balance_webhook_setting_info_update.py` |
| `BalanceWebhookSettingInfoUpdateDict` | `adyen/models/balance_webhook_setting_info_update.py` |
| `WebhookSetting` | `adyen/models/unions/webhook_setting.py` |
| `PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody` | `adyen/errors/patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.balances.post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings

- **Route**: `POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings`
- **Server**: `default13`
- **Signature**: `def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(balance_platform_id: str, webhook_id: str, body: BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `webhook_id`, `body`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `webhook_id` — path `webhookId` · `body` — JSON body
- **Returns (parsed)**: `WebhookSetting`
- **Returns (raw)**: `ApiResult[WebhookSetting, PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]`
- **Error**: `PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceWebhookSettingInfo` | `adyen/models/balance_webhook_setting_info.py` |
| `BalanceWebhookSettingInfoDict` | `adyen/models/balance_webhook_setting_info.py` |
| `WebhookSetting` | `adyen/models/unions/webhook_setting.py` |
| `PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody` | `adyen/errors/post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

