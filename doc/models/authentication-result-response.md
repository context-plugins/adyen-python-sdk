
# Authentication Result Response

## Structure

`AuthenticationResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_1_result` | [`ThreeDS1Result2`](../../doc/models/three-ds-1-result-2.md) | Optional | The result of the 3D Secure authentication. |
| `three_ds_2_result` | [`ThreeDS2Result`](../../doc/models/three-ds-2-result.md) | Optional | The result of the 3D Secure 2 authentication. |

## Example

```python
from adyen.models.authentication_result_response import AuthenticationResultResponse
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.three_ds_1_result_2 import ThreeDS1Result2
from adyen.models.three_ds_2_result import ThreeDS2Result

authentication_result_response = AuthenticationResultResponse(
    three_ds_1_result=ThreeDS1Result2(
        cavv='cavv2',
        cavv_algorithm='cavvAlgorithm8',
        eci='eci6',
        three_d_authenticated_response='threeDAuthenticatedResponse8',
        three_d_offered_response='threeDOfferedResponse2'
    ),
    three_ds_2_result=ThreeDS2Result(
        authentication_value='authenticationValue8',
        cavv_algorithm='cavvAlgorithm8',
        challenge_cancel=ChallengeCancelEnum.ENUM_06,
        ds_trans_id='dsTransID2',
        eci='eci6'
    )
)
```

