
# Authentication Data

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attempt_authentication` | [`AttemptAuthentication`](../../doc/models/attempt-authentication.md) | Optional | - |
| `authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.<br>Default: **false**.<br><br>**Default**: `False` |
| `three_ds_request_data` | [`ThreeDsRequestData`](../../doc/models/three-ds-request-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.attempt_authentication import AttemptAuthentication
from adyen.models.authentication_data import AuthenticationData
from adyen.models.challenge_window_size import ChallengeWindowSize
from adyen.models.data_only import DataOnly
from adyen.models.native_three_ds import NativeThreeDs
from adyen.models.three_ds_request_data import ThreeDsRequestData
from adyen.models.three_ds_version import ThreeDsVersion

authentication_data = AuthenticationData(
    attempt_authentication=AttemptAuthentication.ALWAYS,
    authentication_only=False,
    three_ds_request_data=ThreeDsRequestData(
        challenge_window_size=ChallengeWindowSize.ENUM_03,
        data_only=DataOnly.FALSE,
        native_three_ds=NativeThreeDs.PREFERRED,
        three_ds_version=ThreeDsVersion.ENUM_210,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

