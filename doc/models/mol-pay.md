
# MOL Pay

## Structure

`MOLPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Required | The shopper's bank. Specify this with the issuer value that corresponds to this bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type38Enum`](../../doc/models/type-38-enum.md) | Required | **molpay** |

## Example

```python
from adyen.models.mol_pay import MOLPay
from adyen.models.type_38_enum import Type38Enum

mol_pay = MOLPay(
    issuer='issuer6',
    mtype=Type38Enum.MOLPAY_EBANKING_FPX_MY,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4'
)
```

