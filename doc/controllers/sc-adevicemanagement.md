# SC Adevicemanagement

```python
sc_adevicemanagement_api = client.sc_adevicemanagement
```

## Class Name

`SCAdevicemanagementApi`

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

[`BeginScaDeviceRegistrationResponse`](../../doc/models/begin-sca-device-registration-response.md)

## Example Usage

```python
body = BeginScaDeviceRegistrationRequest(
    name='My Device',
    sdk_output='eyJjaGFsbGVuZ2UiOiJVWEZaTURONGNXWjZUVFExUlhWV2JuaEJPVzVzTm05cVVEUktUbFZtZGtrPSJ9'
)

result = sca_device_management_api.post_sca_devices(
    body=body
)
print(result)
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
| 400 | Bad Request - The request contains invalid input and fails validation. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


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

`void`

## Example Usage

```python
device_id = 'deviceId0'

sca_device_management_api.delete_sca_devices_device_id(device_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request contains invalid input and fails validation. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | Not Found - Device not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


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

[`FinishScaDeviceRegistrationResponse`](../../doc/models/finish-sca-device-registration-response.md)

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
print(result)
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
| 400 | Bad Request - The request contains invalid input and fails validation. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | Not Found - Device not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


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

[`SubmitScaAssociationResponse`](../../doc/models/submit-sca-association-response.md)

## Example Usage

```python
device_id = 'deviceId0'

body = SubmitScaAssociationRequest(
    entities=[
        ScaEntity(
            id='AH00000000000000000000001',
            mtype=ScaEntityType4Enum.ACCOUNTHOLDER
        )
    ]
)

result = sca_device_management_api.post_sca_devices_device_id_sca_associations(
    device_id,
    body=body
)
print(result)
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
| 400 | Bad Request - The request contains invalid input and fails validation. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | Not Found - Device not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

