<!-- Generated file — do not edit; regenerated with the SDK. -->

# PayoutSettingsMerchantLevel — operations

Accessor: `client.payout_settings_merchant_level` · Source: `adyen/apis/payout_settings_merchant_level.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payout_settings_merchant_level.delete_merchants_merchant_id_payout_settings_payout_settings_id

- **Route**: `DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payout_settings_id`
- **Params**: `merchant_id` — path `merchantId` · `payout_settings_id` — path `payoutSettingsId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]`
- **Error**: `DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` | `adyen/errors/delete_merchants_merchant_id_payout_settings_payout_settings_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payout_settings_merchant_level.get_merchants_merchant_id_payout_settings

- **Route**: `GET /merchants/{merchantId}/payoutSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_payout_settings(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `PayoutSettingsResponse`
- **Returns (raw)**: `ApiResult[PayoutSettingsResponse, GetMerchantsMerchantIdPayoutSettingsErrorBody]`
- **Error**: `GetMerchantsMerchantIdPayoutSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutSettingsResponse` | `adyen/models/payout_settings_response.py` |
| `GetMerchantsMerchantIdPayoutSettingsErrorBody` | `adyen/errors/get_merchants_merchant_id_payout_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payout_settings_merchant_level.get_merchants_merchant_id_payout_settings_payout_settings_id

- **Route**: `GET /merchants/{merchantId}/payoutSettings/{payoutSettingsId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payout_settings_id`
- **Params**: `merchant_id` — path `merchantId` · `payout_settings_id` — path `payoutSettingsId`
- **Returns (parsed)**: `PayoutSettings`
- **Returns (raw)**: `ApiResult[PayoutSettings, GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutSettings` | `adyen/models/payout_settings.py` |
| `GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` | `adyen/errors/get_merchants_merchant_id_payout_settings_payout_settings_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payout_settings_merchant_level.patch_merchants_merchant_id_payout_settings_payout_settings_id

- **Route**: `PATCH /merchants/{merchantId}/payoutSettings/{payoutSettingsId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id: str, payout_settings_id: str, *, body: UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `payout_settings_id`
- **Params**: `merchant_id` — path `merchantId` · `payout_settings_id` — path `payoutSettingsId` · `body` — JSON body
- **Returns (parsed)**: `PayoutSettings`
- **Returns (raw)**: `ApiResult[PayoutSettings, PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdatePayoutSettingsRequest` | `adyen/models/update_payout_settings_request.py` |
| `UpdatePayoutSettingsRequestDict` | `adyen/models/update_payout_settings_request.py` |
| `PayoutSettings` | `adyen/models/payout_settings.py` |
| `PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_payout_settings_payout_settings_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payout_settings_merchant_level.post_merchants_merchant_id_payout_settings

- **Route**: `POST /merchants/{merchantId}/payoutSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_payout_settings(merchant_id: str, *, body: PayoutSettingsRequest | PayoutSettingsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `PayoutSettings`
- **Returns (raw)**: `ApiResult[PayoutSettings, PostMerchantsMerchantIdPayoutSettingsErrorBody]`
- **Error**: `PostMerchantsMerchantIdPayoutSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutSettingsRequest` | `adyen/models/payout_settings_request.py` |
| `PayoutSettingsRequestDict` | `adyen/models/payout_settings_request.py` |
| `PayoutSettings` | `adyen/models/payout_settings.py` |
| `PostMerchantsMerchantIdPayoutSettingsErrorBody` | `adyen/errors/post_merchants_merchant_id_payout_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

