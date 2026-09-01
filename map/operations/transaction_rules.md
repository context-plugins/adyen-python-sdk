<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransactionRules — operations

Accessor: `client.transaction_rules` · Source: `adyen/apis/transaction_rules.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transaction_rules.delete_transaction_rules_transaction_rule_id

- **Route**: `DELETE /transactionRules/{transactionRuleId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def delete_transaction_rules_transaction_rule_id(transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_rule_id`
- **Params**: `transaction_rule_id` — path `transactionRuleId`
- **Returns (parsed)**: `TransactionRule`
- **Returns (raw)**: `ApiResult[TransactionRule, DeleteTransactionRulesTransactionRuleIdErrorBody]`
- **Error**: `DeleteTransactionRulesTransactionRuleIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRule` | `adyen/models/transaction_rule.py` |
| `DeleteTransactionRulesTransactionRuleIdErrorBody` | `adyen/errors/delete_transaction_rules_transaction_rule_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.transaction_rules.get_transaction_rules_transaction_rule_id

- **Route**: `GET /transactionRules/{transactionRuleId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_transaction_rules_transaction_rule_id(transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_rule_id`
- **Params**: `transaction_rule_id` — path `transactionRuleId`
- **Returns (parsed)**: `TransactionRuleResponse`
- **Returns (raw)**: `ApiResult[TransactionRuleResponse, GetTransactionRulesTransactionRuleIdErrorBody]`
- **Error**: `GetTransactionRulesTransactionRuleIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRuleResponse` | `adyen/models/transaction_rule_response.py` |
| `GetTransactionRulesTransactionRuleIdErrorBody` | `adyen/errors/get_transaction_rules_transaction_rule_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.transaction_rules.patch_transaction_rules_transaction_rule_id

- **Route**: `PATCH /transactionRules/{transactionRuleId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_transaction_rules_transaction_rule_id(transaction_rule_id: str, *, body: TransactionRuleInfo | TransactionRuleInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_rule_id`
- **Params**: `transaction_rule_id` — path `transactionRuleId` · `body` — JSON body
- **Returns (parsed)**: `TransactionRule`
- **Returns (raw)**: `ApiResult[TransactionRule, PatchTransactionRulesTransactionRuleIdErrorBody]`
- **Error**: `PatchTransactionRulesTransactionRuleIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRuleInfo` | `adyen/models/transaction_rule_info.py` |
| `TransactionRuleInfoDict` | `adyen/models/transaction_rule_info.py` |
| `TransactionRule` | `adyen/models/transaction_rule.py` |
| `PatchTransactionRulesTransactionRuleIdErrorBody` | `adyen/errors/patch_transaction_rules_transaction_rule_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.transaction_rules.post_transaction_rules

- **Route**: `POST /transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_transaction_rules(*, body: TransactionRuleInfo | TransactionRuleInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionRule`
- **Returns (raw)**: `ApiResult[TransactionRule, PostTransactionRulesErrorBody]`
- **Error**: `PostTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRuleInfo` | `adyen/models/transaction_rule_info.py` |
| `TransactionRuleInfoDict` | `adyen/models/transaction_rule_info.py` |
| `TransactionRule` | `adyen/models/transaction_rule.py` |
| `PostTransactionRulesErrorBody` | `adyen/errors/post_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

