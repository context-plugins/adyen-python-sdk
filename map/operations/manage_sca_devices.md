<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageScaDevices — operations

Accessor: `client.manage_sca_devices` · Source: `adyen/apis/manage_sca_devices.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_sca_devices.delete_registered_devices_id

- **Route**: `DELETE /registeredDevices/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def delete_registered_devices_id(id: str, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `payment_instrument_id`
- **Params**: `id` — path · `payment_instrument_id` — query `paymentInstrumentId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteRegisteredDevicesIdErrorBody]`
- **Error**: `DeleteRegisteredDevicesIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteRegisteredDevicesIdErrorBody` | `adyen/errors/delete_registered_devices_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_sca_devices.get_registered_devices

- **Route**: `GET /registeredDevices`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_registered_devices(payment_instrument_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_instrument_id`
- **Params**: `payment_instrument_id` — query `paymentInstrumentId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `SearchRegisteredDevicesResponse`
- **Returns (raw)**: `ApiResult[SearchRegisteredDevicesResponse, GetRegisteredDevicesErrorBody]`
- **Error**: `GetRegisteredDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SearchRegisteredDevicesResponse` | `adyen/models/search_registered_devices_response.py` |
| `GetRegisteredDevicesErrorBody` | `adyen/errors/get_registered_devices_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_sca_devices.patch_registered_devices_device_id_associations

- **Route**: `PATCH /registeredDevices/{deviceId}/associations`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_registered_devices_device_id_associations(device_id: str, *, body: AssociationFinaliseRequest | AssociationFinaliseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `AssociationFinaliseResponse`
- **Returns (raw)**: `ApiResult[AssociationFinaliseResponse, PatchRegisteredDevicesDeviceIdAssociationsErrorBody]`
- **Error**: `PatchRegisteredDevicesDeviceIdAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AssociationFinaliseRequest` | `adyen/models/association_finalise_request.py` |
| `AssociationFinaliseRequestDict` | `adyen/models/association_finalise_request.py` |
| `AssociationFinaliseResponse` | `adyen/models/association_finalise_response.py` |
| `PatchRegisteredDevicesDeviceIdAssociationsErrorBody` | `adyen/errors/patch_registered_devices_device_id_associations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_sca_devices.patch_registered_devices_id

- **Route**: `PATCH /registeredDevices/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_registered_devices_id(id: str, *, body: RegisterScarequest | RegisterScarequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `RegisterScafinalResponse`
- **Returns (raw)**: `ApiResult[RegisterScafinalResponse, PatchRegisteredDevicesIdErrorBody]`
- **Error**: `PatchRegisteredDevicesIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RegisterScarequest` | `adyen/models/register_scarequest.py` |
| `RegisterScarequestDict` | `adyen/models/register_scarequest.py` |
| `RegisterScafinalResponse` | `adyen/models/register_scafinal_response.py` |
| `PatchRegisteredDevicesIdErrorBody` | `adyen/errors/patch_registered_devices_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_sca_devices.post_registered_devices

- **Route**: `POST /registeredDevices`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_registered_devices(*, body: RegisterScarequest | RegisterScarequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RegisterScaresponse`
- **Returns (raw)**: `ApiResult[RegisterScaresponse, PostRegisteredDevicesErrorBody]`
- **Error**: `PostRegisteredDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RegisterScarequest` | `adyen/models/register_scarequest.py` |
| `RegisterScarequestDict` | `adyen/models/register_scarequest.py` |
| `RegisterScaresponse` | `adyen/models/register_scaresponse.py` |
| `PostRegisteredDevicesErrorBody` | `adyen/errors/post_registered_devices_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.manage_sca_devices.post_registered_devices_device_id_associations

- **Route**: `POST /registeredDevices/{deviceId}/associations`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_registered_devices_device_id_associations(device_id: str, *, body: AssociationInitiateRequest | AssociationInitiateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `AssociationInitiateResponse`
- **Returns (raw)**: `ApiResult[AssociationInitiateResponse, PostRegisteredDevicesDeviceIdAssociationsErrorBody]`
- **Error**: `PostRegisteredDevicesDeviceIdAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AssociationInitiateRequest` | `adyen/models/association_initiate_request.py` |
| `AssociationInitiateRequestDict` | `adyen/models/association_initiate_request.py` |
| `AssociationInitiateResponse` | `adyen/models/association_initiate_response.py` |
| `PostRegisteredDevicesDeviceIdAssociationsErrorBody` | `adyen/errors/post_registered_devices_device_id_associations_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

