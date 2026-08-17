
# Doku

## Structure

`Doku`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `first_name` | `str` | Required | The shopper's first name. |
| `last_name` | `str` | Required | The shopper's last name. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Required | The shopper's email. |
| `mtype` | [`Type23Enum`](../../doc/models/type-23-enum.md) | Required | **doku** |

## Example

```python
from adyen.models.doku import Doku
from adyen.models.type_23_enum import Type23Enum

doku = Doku(
    first_name='firstName8',
    last_name='lastName0',
    shopper_email='shopperEmail0',
    mtype=Type23Enum.DOKU_OVO,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4'
)
```

