<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `cloud_device_api/client.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.get_merchants_merchant_account_connected_devices

- **Route**: `GET /merchants/{merchantAccount}/connectedDevices`
- **Signature**: `def get_merchants_merchant_account_connected_devices(merchant_account: str, *, store: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_account`
- **Params**: `merchant_account` — path `merchantAccount` · `store` — query
- **Returns (parsed)**: `ConnectedDevicesResponse`
- **Returns (raw)**: `ApiResult[ConnectedDevicesResponse, GetMerchantsMerchantAccountConnectedDevicesErrorBody]`
- **Error**: `GetMerchantsMerchantAccountConnectedDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectedDevicesResponse` | `cloud_device_api/models/connected_devices_response.py` |
| `GetMerchantsMerchantAccountConnectedDevicesErrorBody` | `cloud_device_api/errors/get_merchants_merchant_account_connected_devices_error.py` |
| `DefaultErrorResponseEntity` | `cloud_device_api/models/default_error_response_entity.py` |

### client.get_merchants_merchant_account_devices_device_id_status

- **Route**: `GET /merchants/{merchantAccount}/devices/{deviceId}/status`
- **Signature**: `def get_merchants_merchant_account_devices_device_id_status(merchant_account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_account`, `device_id`
- **Params**: `merchant_account` — path `merchantAccount` · `device_id` — path `deviceId`
- **Returns (parsed)**: `DeviceStatusResponse`
- **Returns (raw)**: `ApiResult[DeviceStatusResponse, GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody]`
- **Error**: `GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceStatusResponse` | `cloud_device_api/models/device_status_response.py` |
| `GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody` | `cloud_device_api/errors/get_merchants_merchant_account_devices_device_id_status_error.py` |
| `DefaultErrorResponseEntity` | `cloud_device_api/models/default_error_response_entity.py` |

### client.post_merchants_merchant_account_devices_device_id_async

- **Route**: `POST /merchants/{merchantAccount}/devices/{deviceId}/async`
- **Signature**: `def post_merchants_merchant_account_devices_device_id_async(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_account`, `device_id`
- **Params**: `merchant_account` — path `merchantAccount` · `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, RawError]`
- **Error**: `RawError` — **Case B**

### client.post_merchants_merchant_account_devices_device_id_sync

- **Route**: `POST /merchants/{merchantAccount}/devices/{deviceId}/sync`
- **Signature**: `def post_merchants_merchant_account_devices_device_id_sync(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_account`, `device_id`
- **Params**: `merchant_account` — path `merchantAccount` · `device_id` — path `deviceId` · `body` — JSON body
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, RawError]`
- **Error**: `RawError` — **Case B**

