<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransferInstruments — operations

Accessor: `client.transfer_instruments` · Source: `adyen/apis/transfer_instruments.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfer_instruments.delete_transfer_instruments_id

- **Route**: `DELETE /transferInstruments/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def delete_transfer_instruments_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTransferInstrumentsIdErrorBody]`
- **Error**: `DeleteTransferInstrumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTransferInstrumentsIdErrorBody` | `adyen/errors/delete_transfer_instruments_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.transfer_instruments.get_transfer_instruments_id

- **Route**: `GET /transferInstruments/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_transfer_instruments_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `TransferInstrument`
- **Returns (raw)**: `ApiResult[TransferInstrument, GetTransferInstrumentsIdErrorBody]`
- **Error**: `GetTransferInstrumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferInstrument` | `adyen/models/transfer_instrument.py` |
| `GetTransferInstrumentsIdErrorBody` | `adyen/errors/get_transfer_instruments_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.transfer_instruments.patch_transfer_instruments_id

- **Route**: `PATCH /transferInstruments/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def patch_transfer_instruments_id(id: str, *, x_requested_verification_code: str | None = None, body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `TransferInstrument`
- **Returns (raw)**: `ApiResult[TransferInstrument, PatchTransferInstrumentsIdErrorBody]`
- **Error**: `PatchTransferInstrumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferInstrumentInfo` | `adyen/models/transfer_instrument_info.py` |
| `TransferInstrumentInfoDict` | `adyen/models/transfer_instrument_info.py` |
| `TransferInstrument` | `adyen/models/transfer_instrument.py` |
| `PatchTransferInstrumentsIdErrorBody` | `adyen/errors/patch_transfer_instruments_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.transfer_instruments.post_transfer_instruments

- **Route**: `POST /transferInstruments`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_transfer_instruments(*, x_requested_verification_code: str | None = None, body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `TransferInstrument`
- **Returns (raw)**: `ApiResult[TransferInstrument, PostTransferInstrumentsErrorBody]`
- **Error**: `PostTransferInstrumentsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferInstrumentInfo` | `adyen/models/transfer_instrument_info.py` |
| `TransferInstrumentInfoDict` | `adyen/models/transfer_instrument_info.py` |
| `TransferInstrument` | `adyen/models/transfer_instrument.py` |
| `PostTransferInstrumentsErrorBody` | `adyen/errors/post_transfer_instruments_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

