<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthorizedCardUsers — operations

Accessor: `client.authorized_card_users` · Source: `adyen/apis/authorized_card_users.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authorized_card_users.delete_payment_instruments_payment_instrument_id_authorised_card_users

- **Route**: `DELETE /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`
- **Server**: `default13`
- **Signature**: `def delete_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_instrument_id`
- **Params**: `payment_instrument_id` — path `paymentInstrumentId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]`
- **Error**: `DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` | `adyen/errors/delete_payment_instruments_payment_instrument_id_authorised_card_users_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.authorized_card_users.get_payment_instruments_payment_instrument_id_authorised_card_users

- **Route**: `GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`
- **Server**: `default13`
- **Signature**: `def get_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_instrument_id`
- **Params**: `payment_instrument_id` — path `paymentInstrumentId`
- **Returns (parsed)**: `AuthorisedCardUsers`
- **Returns (raw)**: `ApiResult[AuthorisedCardUsers, GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]`
- **Error**: `GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthorisedCardUsers` | `adyen/models/authorised_card_users.py` |
| `GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` | `adyen/errors/get_payment_instruments_payment_instrument_id_authorised_card_users_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.authorized_card_users.patch_payment_instruments_payment_instrument_id_authorised_card_users

- **Route**: `PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`
- **Server**: `default13`
- **Signature**: `def patch_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id: str, body: AuthorisedCardUsers | AuthorisedCardUsersDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_instrument_id`, `body`
- **Params**: `payment_instrument_id` — path `paymentInstrumentId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]`
- **Error**: `PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthorisedCardUsers` | `adyen/models/authorised_card_users.py` |
| `AuthorisedCardUsersDict` | `adyen/models/authorised_card_users.py` |
| `PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` | `adyen/errors/patch_payment_instruments_payment_instrument_id_authorised_card_users_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.authorized_card_users.post_payment_instruments_payment_instrument_id_authorised_card_users

- **Route**: `POST /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`
- **Server**: `default13`
- **Signature**: `def post_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id: str, body: AuthorisedCardUsers | AuthorisedCardUsersDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_instrument_id`, `body`
- **Params**: `payment_instrument_id` — path `paymentInstrumentId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]`
- **Error**: `PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AuthorisedCardUsers` | `adyen/models/authorised_card_users.py` |
| `AuthorisedCardUsersDict` | `adyen/models/authorised_card_users.py` |
| `PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody` | `adyen/errors/post_payment_instruments_payment_instrument_id_authorised_card_users_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

