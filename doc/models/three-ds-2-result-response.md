
# Three Ds 2 Result Response

*This model accepts additional fields of type Any.*

## Structure

`ThreeDs2ResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_2_result` | [`ThreeDs2Result2`](../../doc/models/three-ds-2-result-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.challenge_cancel import ChallengeCancel
from adyen.models.three_ds_2_result_2 import ThreeDs2Result2
from adyen.models.three_ds_2_result_response import ThreeDs2ResultResponse

three_ds_2_result_response = ThreeDs2ResultResponse(
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

