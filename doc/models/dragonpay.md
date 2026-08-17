
# Dragonpay

## Structure

`Dragonpay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Required | The Dragonpay issuer value of the shopper's selected bank. Set this to an **id** of a Dragonpay issuer to preselect it. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Optional | The shopper’s email address. |
| `mtype` | [`Type28Enum`](../../doc/models/type-28-enum.md) | Required | **dragonpay** |

## Example

```python
from adyen.models.dragonpay import Dragonpay
from adyen.models.type_28_enum import Type28Enum

dragonpay = Dragonpay(
    issuer='issuer0',
    mtype=Type28Enum.DRAGONPAY_OTC_NON_BANKING,
    checkout_attempt_id='checkoutAttemptId6',
    sdk_data='sdkData0',
    shopper_email='shopperEmail4'
)
```

