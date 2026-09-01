<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageCardPin — operations

Accessor: `client.manage_card_pin` · Source: `adyen/apis/manage_card_pin.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_card_pin.get_public_key

- **Route**: `GET /publicKey`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_public_key(*, purpose: str | None = None, format: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `purpose` — query · `format` — query
- **Returns (parsed)**: `PublicKeyResponse`
- **Returns (raw)**: `ApiResult[PublicKeyResponse, GetPublicKeyErrorBody]`
- **Error**: `GetPublicKeyErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PublicKeyResponse` | `adyen/models/public_key_response.py` |
| `GetPublicKeyErrorBody` | `adyen/errors/get_public_key_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_card_pin.post_pins_change

- **Route**: `POST /pins/change`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_pins_change(*, body: PinChangeRequest | PinChangeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PinChangeResponse`
- **Returns (raw)**: `ApiResult[PinChangeResponse, PostPinsChangeErrorBody]`
- **Error**: `PostPinsChangeErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PinChangeRequest` | `adyen/models/pin_change_request.py` |
| `PinChangeRequestDict` | `adyen/models/pin_change_request.py` |
| `PinChangeResponse` | `adyen/models/pin_change_response.py` |
| `PostPinsChangeErrorBody` | `adyen/errors/post_pins_change_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_card_pin.post_pins_reveal

- **Route**: `POST /pins/reveal`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_pins_reveal(*, body: RevealPinRequest | RevealPinRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RevealPinResponse`
- **Returns (raw)**: `ApiResult[RevealPinResponse, PostPinsRevealErrorBody]`
- **Error**: `PostPinsRevealErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RevealPinRequest` | `adyen/models/reveal_pin_request.py` |
| `RevealPinRequestDict` | `adyen/models/reveal_pin_request.py` |
| `RevealPinResponse` | `adyen/models/reveal_pin_response.py` |
| `PostPinsRevealErrorBody` | `adyen/errors/post_pins_reveal_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

