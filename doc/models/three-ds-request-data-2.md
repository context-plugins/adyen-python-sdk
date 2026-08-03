
# Three Ds Request Data 2

Object with additional parameters for the 3D Secure authentication flow.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDsRequestData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `challenge_window_size` | [`ChallengeWindowSize`](../../doc/models/challenge-window-size.md) | Optional | - |
| `data_only` | [`DataOnly`](../../doc/models/data-only.md) | Optional | - |
| `native_three_ds` | [`NativeThreeDs`](../../doc/models/native-three-ds.md) | Optional | - |
| `three_ds_version` | [`ThreeDsVersion`](../../doc/models/three-ds-version.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.challenge_window_size import ChallengeWindowSize
from adyen.models.data_only import DataOnly
from adyen.models.native_three_ds import NativeThreeDs
from adyen.models.three_ds_request_data_2 import ThreeDsRequestData2
from adyen.models.three_ds_version import ThreeDsVersion

three_ds_request_data_2 = ThreeDsRequestData2(
    challenge_window_size=ChallengeWindowSize.ENUM_03,
    data_only=DataOnly.FALSE,
    native_three_ds=NativeThreeDs.PREFERRED,
    three_ds_version=ThreeDsVersion.ENUM_210,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

