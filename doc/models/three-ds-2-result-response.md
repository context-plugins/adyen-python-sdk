
# Three DS 2 Result Response

## Structure

`ThreeDS2ResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_2_result` | [`ThreeDS2Result`](../../doc/models/three-ds-2-result.md) | Optional | The result of the 3D Secure 2 authentication. |

## Example

```python
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.three_ds_2_result import ThreeDS2Result
from adyen.models.three_ds_2_result_response import ThreeDS2ResultResponse

three_ds_2_result_response = ThreeDS2ResultResponse(
    three_ds_2_result=ThreeDS2Result(
        authentication_value='authenticationValue8',
        cavv_algorithm='cavvAlgorithm8',
        challenge_cancel=ChallengeCancelEnum.ENUM_06,
        ds_trans_id='dsTransID2',
        eci='eci6'
    )
)
```

