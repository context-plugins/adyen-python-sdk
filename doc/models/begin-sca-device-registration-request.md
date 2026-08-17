
# Begin Sca Device Registration Request

## Structure

`BeginScaDeviceRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name of the SCA device that you are registering. You can use it to help your users identify the device.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `64` |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to register the SCA device. You obtain this information by using Adyen's authentication SDK.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `20000` |

## Example

```python
from adyen.models.begin_sca_device_registration_request import BeginScaDeviceRegistrationRequest

begin_sca_device_registration_request = BeginScaDeviceRegistrationRequest(
    name='name2',
    sdk_output='sdkOutput0'
)
```

