# SC Adevicemanagement

```python
sc_adevicemanagement_api = client.sc_adevicemanagement
```

## Class Name

`ScAdevicemanagementApi`

## Methods

* [Post-Sca Devices](../../doc/controllers/sc-adevicemanagement.md#post-sca-devices)
* [Delete-Sca Devices-Device Id](../../doc/controllers/sc-adevicemanagement.md#delete-sca-devices-device-id)
* [Patch-Sca Devices-Device Id](../../doc/controllers/sc-adevicemanagement.md#patch-sca-devices-device-id)
* [Post-Sca Devices-Device Id-Sca Associations](../../doc/controllers/sc-adevicemanagement.md#post-sca-devices-device-id-sca-associations)


# Post-Sca Devices

Begins the registration process for a new Strong Customer Authentication (SCA) device.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_sca_devices(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BeginScaDeviceRegistrationRequest`](../../doc/models/begin-sca-device-registration-request.md) | Body, Optional | - |

## Response Type

**201**: Created - A device resource is created. The initial step of registration is complete, but the device isn't ready for use.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BeginScaDeviceRegistrationResponse`](../../doc/models/begin-sca-device-registration-response.md).

## Example Usage

```python
body = BeginScaDeviceRegistrationRequest(
    name='My Device',
    sdk_output='eyJjaGFsbGVuZ2UiOiJVWEZaTURONGNXWjZUVFExUlhWV2JuaEJPVzVzTm05cVVEUktUbFZtZGtrPSJ9'
)

result = sca_device_management_api.post_sca_devices(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "scaDevice": {
    "id": "BSDR42XV3223223S5N6CDQDGH53M8H",
    "name": "My Device",
    "type": "ios"
  },
  "sdkInput": "eyJjaGFsbGVuZ2UiOiJVWEZaTURONGNXWjZUVFExUlhWV2JuaEJPVzVzTm05cVVEUktUbFZtZGtrPSJ9"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request contains invalid input and fails validation. | [`ScaDevices400ErrorException`](../../doc/models/sca-devices-400-error-exception.md) |
| 401 | Unauthorized - Authentication required. | [`ScaDevices401ErrorException`](../../doc/models/sca-devices-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaDevices403ErrorException`](../../doc/models/sca-devices-403-error-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`ScaDevices422ErrorException`](../../doc/models/sca-devices-422-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaDevices500ErrorException`](../../doc/models/sca-devices-500-error-exception.md) |


# Delete-Sca Devices-Device Id

Deletes a Strong Customer Authentication (SCA) device.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_sca_devices_device_id(self,
                                device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Template, Required | The unique identifier of the SCA device to delete.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |

## Response Type

**204**: No Content - The device was deleted successfully.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
device_id = 'deviceId0'

result = sca_device_management_api.delete_sca_devices_device_id(device_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request contains invalid input and fails validation. | [`ScaDevices400ErrorException`](../../doc/models/sca-devices-400-error-exception.md) |
| 401 | Unauthorized - Authentication required. | [`ScaDevices401ErrorException`](../../doc/models/sca-devices-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaDevices403ErrorException`](../../doc/models/sca-devices-403-error-exception.md) |
| 404 | Not Found - Device not found. | [`ScaDevices404ErrorException`](../../doc/models/sca-devices-404-error-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`ScaDevices422ErrorException`](../../doc/models/sca-devices-422-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaDevices500ErrorException`](../../doc/models/sca-devices-500-error-exception.md) |


# Patch-Sca Devices-Device Id

Finishes the registration process for a new Strong Customer Authentication (SCA) device.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_sca_devices_device_id(self,
                               device_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Template, Required | The unique identifier of the SCA device that you are associating with a resource.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `body` | [`FinishScaDeviceRegistrationRequest`](../../doc/models/finish-sca-device-registration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - Device registration was completed successfully.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FinishScaDeviceRegistrationResponse`](../../doc/models/finish-sca-device-registration-response.md).

## Example Usage

```python
device_id = 'deviceId0'

body = FinishScaDeviceRegistrationRequest(
    sdk_output='eyJjaGFsbGVuZ2UiOiJVWEZaTURONGNXWjZUVFExUlhWV2JuaEJPVzVzTm05cVVEUktUbFZtZGtrPSJ9'
)

result = sca_device_management_api.patch_sca_devices_device_id(
    device_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "scaDevice": {
    "id": "BSDR42XV3223223S5N6CDQDGH53M8H",
    "name": "Device",
    "type": "ios"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request contains invalid input and fails validation. | [`ScaDevices400ErrorException`](../../doc/models/sca-devices-400-error-exception.md) |
| 401 | Unauthorized - Authentication required. | [`ScaDevices401ErrorException`](../../doc/models/sca-devices-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaDevices403ErrorException`](../../doc/models/sca-devices-403-error-exception.md) |
| 404 | Not Found - Device not found. | [`ScaDevices404ErrorException`](../../doc/models/sca-devices-404-error-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`ScaDevices422ErrorException`](../../doc/models/sca-devices-422-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaDevices500ErrorException`](../../doc/models/sca-devices-500-error-exception.md) |


# Post-Sca Devices-Device Id-Sca Associations

Creates an association between an SCA-enabled device and an entity, such as an account holder. This action does not guarantee the association is immediately ready for use; its status may be `pendingApproval` if the account holder has existing devices.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_sca_devices_device_id_sca_associations(self,
                                               device_id,
                                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Template, Required | The unique identifier of the SCA device that you are associating with a resource.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `body` | [`SubmitScaAssociationRequest`](../../doc/models/submit-sca-association-request.md) | Body, Optional | - |

## Response Type

**201**: Created - Association created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubmitScaAssociationResponse`](../../doc/models/submit-sca-association-response.md).

## Example Usage

```python
device_id = 'deviceId0'

body = SubmitScaAssociationRequest(
    entities=[
        ScaEntity(
            id='AH00000000000000000000001',
            mtype=ScaEntityType4.ACCOUNTHOLDER
        )
    ]
)

result = sca_device_management_api.post_sca_devices_device_id_sca_associations(
    device_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "scaAssociations": [
    {
      "scaDeviceId": "BSDR11111111111A1AAA1AAAAA1AA1",
      "entityType": "accountHolder",
      "entityId": "AH00000000000000000000001",
      "status": "pendingApproval"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request contains invalid input and fails validation. | [`ScaDevicesScaAssociations400ErrorException`](../../doc/models/sca-devices-sca-associations-400-error-exception.md) |
| 401 | Unauthorized - Authentication required. | [`ScaDevicesScaAssociations401ErrorException`](../../doc/models/sca-devices-sca-associations-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaDevicesScaAssociations403ErrorException`](../../doc/models/sca-devices-sca-associations-403-error-exception.md) |
| 404 | Not Found - Device not found. | [`ScaDevicesScaAssociations404ErrorException`](../../doc/models/sca-devices-sca-associations-404-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`ScaDevicesScaAssociations422ErrorException`](../../doc/models/sca-devices-sca-associations-422-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaDevicesScaAssociations500ErrorException`](../../doc/models/sca-devices-sca-associations-500-error-exception.md) |

