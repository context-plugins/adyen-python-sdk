<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentInstrumentGroups — operations

Accessor: `client.payment_instrument_groups` · Source: `adyen/apis/payment_instrument_groups.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payment_instrument_groups.get_payment_instrument_groups_id

- **Route**: `GET /paymentInstrumentGroups/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instrument_groups_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `PaymentInstrumentGroup`
- **Returns (raw)**: `ApiResult[PaymentInstrumentGroup, GetPaymentInstrumentGroupsIdErrorBody]`
- **Error**: `GetPaymentInstrumentGroupsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentGroup` | `adyen/models/payment_instrument_group.py` |
| `GetPaymentInstrumentGroupsIdErrorBody` | `adyen/errors/get_payment_instrument_groups_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instrument_groups.get_payment_instrument_groups_id_transaction_rules

- **Route**: `GET /paymentInstrumentGroups/{id}/transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instrument_groups_id_transaction_rules(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `TransactionRulesResponse`
- **Returns (raw)**: `ApiResult[TransactionRulesResponse, GetPaymentInstrumentGroupsIdTransactionRulesErrorBody]`
- **Error**: `GetPaymentInstrumentGroupsIdTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRulesResponse` | `adyen/models/transaction_rules_response.py` |
| `GetPaymentInstrumentGroupsIdTransactionRulesErrorBody` | `adyen/errors/get_payment_instrument_groups_id_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instrument_groups.post_payment_instrument_groups

- **Route**: `POST /paymentInstrumentGroups`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_payment_instrument_groups(*, body: PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInstrumentGroup`
- **Returns (raw)**: `ApiResult[PaymentInstrumentGroup, PostPaymentInstrumentGroupsErrorBody]`
- **Error**: `PostPaymentInstrumentGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentGroupInfo` | `adyen/models/payment_instrument_group_info.py` |
| `PaymentInstrumentGroupInfoDict` | `adyen/models/payment_instrument_group_info.py` |
| `PaymentInstrumentGroup` | `adyen/models/payment_instrument_group.py` |
| `PostPaymentInstrumentGroupsErrorBody` | `adyen/errors/post_payment_instrument_groups_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

