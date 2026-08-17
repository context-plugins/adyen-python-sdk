
# Alma

## Structure

`Alma`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `fee_type` | [`FeeTypeEnum`](../../doc/models/fee-type-enum.md) | Optional | **Alma payment request fee type** |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Optional | The payment method type. |

## Example

```python
from adyen.models.alma import Alma
from adyen.models.fee_type_enum import FeeTypeEnum
from adyen.models.type_3_enum import Type3Enum

alma = Alma(
    checkout_attempt_id='checkoutAttemptId2',
    fee_type=FeeTypeEnum.MERCHANTPAYS,
    sdk_data='sdkData4',
    mtype=Type3Enum.ALMA
)
```

