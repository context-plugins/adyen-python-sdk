<!-- Generated file — do not edit; regenerated with the SDK. -->

# SplitConfigurationMerchantLevel — operations

Accessor: `client.split_configuration_merchant_level` · Source: `adyen/apis/split_configuration_merchant_level.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.split_configuration_merchant_level.delete_merchants_merchant_id_split_configurations_split_configuration_id

- **Route**: `DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_merchants_merchant_id_split_configurations_split_configuration_id(merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId`
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]`
- **Error**: `DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` | `adyen/errors/delete_merchants_merchant_id_split_configurations_split_configuration_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id

- **Route**: `DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(merchant_id: str, split_configuration_id: str, rule_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`, `rule_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId` · `rule_id` — path `ruleId`
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody]`
- **Error**: `DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody` | `adyen/errors/delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.get_merchants_merchant_id_split_configurations

- **Route**: `GET /merchants/{merchantId}/splitConfigurations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_split_configurations(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `SplitConfigurationList`
- **Returns (raw)**: `ApiResult[SplitConfigurationList, GetMerchantsMerchantIdSplitConfigurationsErrorBody]`
- **Error**: `GetMerchantsMerchantIdSplitConfigurationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfigurationList` | `adyen/models/split_configuration_list.py` |
| `GetMerchantsMerchantIdSplitConfigurationsErrorBody` | `adyen/errors/get_merchants_merchant_id_split_configurations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.get_merchants_merchant_id_split_configurations_split_configuration_id

- **Route**: `GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_split_configurations_split_configuration_id(merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId`
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` | `adyen/errors/get_merchants_merchant_id_split_configurations_split_configuration_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.patch_merchants_merchant_id_split_configurations_split_configuration_id

- **Route**: `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_split_configurations_split_configuration_id(merchant_id: str, split_configuration_id: str, *, body: UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId` · `body` — JSON body
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSplitConfigurationRequest` | `adyen/models/update_split_configuration_request.py` |
| `UpdateSplitConfigurationRequestDict` | `adyen/models/update_split_configuration_request.py` |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_split_configurations_split_configuration_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id

- **Route**: `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(merchant_id: str, split_configuration_id: str, rule_id: str, *, body: UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`, `rule_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId` · `rule_id` — path `ruleId` · `body` — JSON body
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSplitConfigurationRuleRequest` | `adyen/models/update_split_configuration_rule_request.py` |
| `UpdateSplitConfigurationRuleRequestDict` | `adyen/models/update_split_configuration_rule_request.py` |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.patch_merchants_split_configurations_rules_split_logic

- **Route**: `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_split_configurations_rules_split_logic(merchant_id: str, split_configuration_id: str, rule_id: str, split_logic_id: str, *, body: UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`, `rule_id`, `split_logic_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId` · `rule_id` — path `ruleId` · `split_logic_id` — path `splitLogicId` · `body` — JSON body
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody]`
- **Error**: `PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSplitConfigurationLogicRequest` | `adyen/models/update_split_configuration_logic_request.py` |
| `UpdateSplitConfigurationLogicRequestDict` | `adyen/models/update_split_configuration_logic_request.py` |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody` | `adyen/errors/patch_merchants_split_configurations_rules_split_logic_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.post_merchants_merchant_id_split_configurations

- **Route**: `POST /merchants/{merchantId}/splitConfigurations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_split_configurations(merchant_id: str, *, body: SplitConfiguration | SplitConfigurationDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsErrorBody]`
- **Error**: `PostMerchantsMerchantIdSplitConfigurationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `SplitConfigurationDict` | `adyen/models/split_configuration.py` |
| `PostMerchantsMerchantIdSplitConfigurationsErrorBody` | `adyen/errors/post_merchants_merchant_id_split_configurations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.split_configuration_merchant_level.post_merchants_merchant_id_split_configurations_split_configuration_id

- **Route**: `POST /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_split_configurations_split_configuration_id(merchant_id: str, split_configuration_id: str, *, body: SplitConfigurationRule | SplitConfigurationRuleDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `split_configuration_id`
- **Params**: `merchant_id` — path `merchantId` · `split_configuration_id` — path `splitConfigurationId` · `body` — JSON body
- **Returns (parsed)**: `SplitConfiguration`
- **Returns (raw)**: `ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]`
- **Error**: `PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SplitConfigurationRule` | `adyen/models/split_configuration_rule.py` |
| `SplitConfigurationRuleDict` | `adyen/models/split_configuration_rule.py` |
| `SplitConfiguration` | `adyen/models/split_configuration.py` |
| `PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody` | `adyen/errors/post_merchants_merchant_id_split_configurations_split_configuration_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

