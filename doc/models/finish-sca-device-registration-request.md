
# Finish Sca Device Registration Request

*This model accepts additional fields of type Any.*

## Structure

`FinishScaDeviceRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to register the SCA device. You obtain this information by using Adyen's authentication SDK.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `20000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.finish_sca_device_registration_request import FinishScaDeviceRegistrationRequest

finish_sca_device_registration_request = FinishScaDeviceRegistrationRequest(
    sdk_output='sdkOutput2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

