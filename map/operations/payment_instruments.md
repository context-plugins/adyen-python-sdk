<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentInstruments — operations

Accessor: `client.payment_instruments` · Source: `adyen/apis/payment_instruments.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payment_instruments.get_payment_instruments_id

- **Route**: `GET /paymentInstruments/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `PaymentInstrument1`
- **Returns (raw)**: `ApiResult[PaymentInstrument1, GetPaymentInstrumentsIdErrorBody]`
- **Error**: `GetPaymentInstrumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrument1` | `adyen/models/payment_instrument1.py` |
| `GetPaymentInstrumentsIdErrorBody` | `adyen/errors/get_payment_instruments_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.get_payment_instruments_id_network_token_activation_data

- **Route**: `GET /paymentInstruments/{id}/networkTokenActivationData`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_id_network_token_activation_data(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `NetworkTokenActivationDataResponse`
- **Returns (raw)**: `ApiResult[NetworkTokenActivationDataResponse, GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]`
- **Error**: `GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NetworkTokenActivationDataResponse` | `adyen/models/network_token_activation_data_response.py` |
| `GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody` | `adyen/errors/get_payment_instruments_id_network_token_activation_data_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.get_payment_instruments_id_network_tokens

- **Route**: `GET /paymentInstruments/{id}/networkTokens`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_id_network_tokens(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `ListNetworkTokensResponse`
- **Returns (raw)**: `ApiResult[ListNetworkTokensResponse, GetPaymentInstrumentsIdNetworkTokensErrorBody]`
- **Error**: `GetPaymentInstrumentsIdNetworkTokensErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListNetworkTokensResponse` | `adyen/models/list_network_tokens_response.py` |
| `GetPaymentInstrumentsIdNetworkTokensErrorBody` | `adyen/errors/get_payment_instruments_id_network_tokens_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.get_payment_instruments_id_reveal

- **Route**: `GET /paymentInstruments/{id}/reveal`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_id_reveal(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `PaymentInstrumentRevealInfo`
- **Returns (raw)**: `ApiResult[PaymentInstrumentRevealInfo, GetPaymentInstrumentsIdRevealErrorBody]`
- **Error**: `GetPaymentInstrumentsIdRevealErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentRevealInfo` | `adyen/models/payment_instrument_reveal_info.py` |
| `GetPaymentInstrumentsIdRevealErrorBody` | `adyen/errors/get_payment_instruments_id_reveal_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.get_payment_instruments_id_transaction_rules

- **Route**: `GET /paymentInstruments/{id}/transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_id_transaction_rules(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `TransactionRulesResponse`
- **Returns (raw)**: `ApiResult[TransactionRulesResponse, GetPaymentInstrumentsIdTransactionRulesErrorBody]`
- **Error**: `GetPaymentInstrumentsIdTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRulesResponse` | `adyen/models/transaction_rules_response.py` |
| `GetPaymentInstrumentsIdTransactionRulesErrorBody` | `adyen/errors/get_payment_instruments_id_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.patch_payment_instruments_id

- **Route**: `PATCH /paymentInstruments/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_payment_instruments_id(id: str, *, body: PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdatePaymentInstrument`
- **Returns (raw)**: `ApiResult[UpdatePaymentInstrument, PatchPaymentInstrumentsIdErrorBody]`
- **Error**: `PatchPaymentInstrumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentUpdateRequest` | `adyen/models/payment_instrument_update_request.py` |
| `PaymentInstrumentUpdateRequestDict` | `adyen/models/payment_instrument_update_request.py` |
| `UpdatePaymentInstrument` | `adyen/models/update_payment_instrument.py` |
| `PatchPaymentInstrumentsIdErrorBody` | `adyen/errors/patch_payment_instruments_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.post_payment_instruments

- **Route**: `POST /paymentInstruments`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_payment_instruments(*, body: PaymentInstrumentInfo | PaymentInstrumentInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInstrument1`
- **Returns (raw)**: `ApiResult[PaymentInstrument1, PostPaymentInstrumentsErrorBody]`
- **Error**: `PostPaymentInstrumentsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentInfo` | `adyen/models/payment_instrument_info.py` |
| `PaymentInstrumentInfoDict` | `adyen/models/payment_instrument_info.py` |
| `PaymentInstrument1` | `adyen/models/payment_instrument1.py` |
| `PostPaymentInstrumentsErrorBody` | `adyen/errors/post_payment_instruments_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.post_payment_instruments_id_network_token_activation_data

- **Route**: `POST /paymentInstruments/{id}/networkTokenActivationData`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_payment_instruments_id_network_token_activation_data(id: str, *, body: NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `NetworkTokenActivationDataResponse`
- **Returns (raw)**: `ApiResult[NetworkTokenActivationDataResponse, PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]`
- **Error**: `PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NetworkTokenActivationDataRequest` | `adyen/models/network_token_activation_data_request.py` |
| `NetworkTokenActivationDataRequestDict` | `adyen/models/network_token_activation_data_request.py` |
| `NetworkTokenActivationDataResponse` | `adyen/models/network_token_activation_data_response.py` |
| `PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody` | `adyen/errors/post_payment_instruments_id_network_token_activation_data_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.payment_instruments.post_payment_instruments_reveal

- **Route**: `POST /paymentInstruments/reveal`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_payment_instruments_reveal(*, body: PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInstrumentRevealResponse`
- **Returns (raw)**: `ApiResult[PaymentInstrumentRevealResponse, PostPaymentInstrumentsRevealErrorBody]`
- **Error**: `PostPaymentInstrumentsRevealErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentInstrumentRevealRequest` | `adyen/models/payment_instrument_reveal_request.py` |
| `PaymentInstrumentRevealRequestDict` | `adyen/models/payment_instrument_reveal_request.py` |
| `PaymentInstrumentRevealResponse` | `adyen/models/payment_instrument_reveal_response.py` |
| `PostPaymentInstrumentsRevealErrorBody` | `adyen/errors/post_payment_instruments_reveal_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

