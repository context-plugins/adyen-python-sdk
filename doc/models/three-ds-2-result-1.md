
# Three Ds 2 Result 1

Result of the 3D Secure 2 authentication.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDs2Result1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_value` | `str` | Optional | The `authenticationValue` value as defined in the 3D Secure 2 specification. |
| `cavv_algorithm` | `str` | Optional | The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations. |
| `challenge_cancel` | [`ChallengeCancel`](../../doc/models/challenge-cancel.md) | Optional | - |
| `ds_trans_id` | `str` | Optional | The `dsTransID` value as defined in the 3D Secure 2 specification. |
| `eci` | `str` | Optional | The `eci` value as defined in the 3D Secure 2 specification. |
| `exemption_indicator` | [`ExemptionIndicator`](../../doc/models/exemption-indicator.md) | Optional | - |
| `message_version` | `str` | Optional | The `messageVersion` value as defined in the 3D Secure 2 specification. |
| `risk_score` | `str` | Optional | Risk score calculated by Cartes Bancaires Directory Server (DS). |
| `three_ds_requestor_challenge_ind` | [`ThreeDsRequestorChallengeInd`](../../doc/models/three-ds-requestor-challenge-ind.md) | Optional | - |
| `three_ds_server_trans_id` | `str` | Optional | The `threeDSServerTransID` value as defined in the 3D Secure 2 specification. |
| `timestamp` | `str` | Optional | The `timestamp` value of the 3D Secure 2 authentication. |
| `trans_status` | `str` | Optional | The `transStatus` value as defined in the 3D Secure 2 specification. |
| `trans_status_reason` | `str` | Optional | Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |
| `white_list_status` | `str` | Optional | The `whiteListStatus` value as defined in the 3D Secure 2 specification. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.challenge_cancel import ChallengeCancel
from adyen.models.three_ds_2_result_1 import ThreeDs2Result1

three_ds_2_result_1 = ThreeDs2Result1(
    authentication_value='authenticationValue2',
    cavv_algorithm='cavvAlgorithm4',
    challenge_cancel=ChallengeCancel.ENUM_02,
    ds_trans_id='dsTransID6',
    eci='eci0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

