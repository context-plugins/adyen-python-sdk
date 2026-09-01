<!-- Generated file — do not edit; regenerated with the SDK. -->

# ScaDeviceManagement — operations

Accessor: `client.sca_device_management` · Source: `adyen/apis/sca_device_management.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sca_device_management.delete_sca_devices_device_id

- **Route**: `DELETE /scaDevices/{deviceId}`
- **Server**: `default13`
- **Signature**: `def delete_sca_devices_device_id(device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path `deviceId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteScaDevicesDeviceIdErrorBody]`
- **Error**: `DeleteScaDevicesDeviceIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteScaDevicesDeviceIdErrorBody` | `adyen/errors/delete_sca_devices_device_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.sca_device_management.patch_sca_devices_device_id

- **Route**: `PATCH /scaDevices/{deviceId}`
- **Server**: `default13`
- **Signature**: `def patch_sca_devices_device_id(device_id: str, *, body: FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `FinishScaDeviceRegistrationResponse`
- **Returns (raw)**: `ApiResult[FinishScaDeviceRegistrationResponse, PatchScaDevicesDeviceIdErrorBody]`
- **Error**: `PatchScaDevicesDeviceIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FinishScaDeviceRegistrationRequest` | `adyen/models/finish_sca_device_registration_request.py` |
| `FinishScaDeviceRegistrationRequestDict` | `adyen/models/finish_sca_device_registration_request.py` |
| `FinishScaDeviceRegistrationResponse` | `adyen/models/finish_sca_device_registration_response.py` |
| `PatchScaDevicesDeviceIdErrorBody` | `adyen/errors/patch_sca_devices_device_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.sca_device_management.post_sca_devices

- **Route**: `POST /scaDevices`
- **Server**: `default13`
- **Signature**: `def post_sca_devices(*, body: BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BeginScaDeviceRegistrationResponse`
- **Returns (raw)**: `ApiResult[BeginScaDeviceRegistrationResponse, PostScaDevicesErrorBody]`
- **Error**: `PostScaDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BeginScaDeviceRegistrationRequest` | `adyen/models/begin_sca_device_registration_request.py` |
| `BeginScaDeviceRegistrationRequestDict` | `adyen/models/begin_sca_device_registration_request.py` |
| `BeginScaDeviceRegistrationResponse` | `adyen/models/begin_sca_device_registration_response.py` |
| `PostScaDevicesErrorBody` | `adyen/errors/post_sca_devices_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.sca_device_management.post_sca_devices_device_id_sca_associations

- **Route**: `POST /scaDevices/{deviceId}/scaAssociations`
- **Server**: `default13`
- **Signature**: `def post_sca_devices_device_id_sca_associations(device_id: str, *, body: SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `SubmitScaAssociationResponse`
- **Returns (raw)**: `ApiResult[SubmitScaAssociationResponse, PostScaDevicesDeviceIdScaAssociationsErrorBody]`
- **Error**: `PostScaDevicesDeviceIdScaAssociationsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubmitScaAssociationRequest` | `adyen/models/submit_sca_association_request.py` |
| `SubmitScaAssociationRequestDict` | `adyen/models/submit_sca_association_request.py` |
| `SubmitScaAssociationResponse` | `adyen/models/submit_sca_association_response.py` |
| `PostScaDevicesDeviceIdScaAssociationsErrorBody` | `adyen/errors/post_sca_devices_device_id_sca_associations_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

