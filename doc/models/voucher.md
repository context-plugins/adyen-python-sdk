
# Voucher

## Structure

`Voucher`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `first_name` | `str` | Required | The shopper's first name. |
| `last_name` | `str` | Required | The shopper's last name. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Required | The shopper's email. |
| `telephone_number` | `str` | Required | The shopper's contact number. It must have an international number format, for example **+31 20 779 1846**. Formats like **+31 (0)20 779 1846** or **0031 20 779 1846** are not accepted. |
| `mtype` | [`Type29Enum`](../../doc/models/type-29-enum.md) | Required | **econtextvoucher** |

## Example

```python
from adyen.models.type_29_enum import Type29Enum
from adyen.models.voucher import Voucher

voucher = Voucher(
    first_name='firstName2',
    last_name='lastName6',
    shopper_email='shopperEmail6',
    telephone_number='telephoneNumber4',
    mtype=Type29Enum.ECONTEXT_STORES,
    checkout_attempt_id='checkoutAttemptId8',
    sdk_data='sdkData8'
)
```

