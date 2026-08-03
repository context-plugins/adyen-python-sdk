
# Authentication Result Response

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_1_result` | [`ThreeDs1Result`](../../doc/models/three-ds-1-result.md) | Optional | - |
| `three_ds_2_result` | [`ThreeDs2Result2`](../../doc/models/three-ds-2-result-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_result_response import AuthenticationResultResponse
from adyen.models.challenge_cancel import ChallengeCancel
from adyen.models.three_ds_1_result import ThreeDs1Result
from adyen.models.three_ds_2_result_2 import ThreeDs2Result2

authentication_result_response = AuthenticationResultResponse(
    three_ds_1_result=ThreeDs1Result(
        cavv='cavv2',
        cavv_algorithm='cavvAlgorithm8',
        eci='eci6',
        three_d_authenticated_response='threeDAuthenticatedResponse8',
        three_d_offered_response='threeDOfferedResponse2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    three_ds_2_result=ThreeDs2Result2(
        authentication_value='authenticationValue8',
        cavv_algorithm='cavvAlgorithm8',
        challenge_cancel=ChallengeCancel.ENUM_06,
        ds_trans_id='dsTransID2',
        eci='eci6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

