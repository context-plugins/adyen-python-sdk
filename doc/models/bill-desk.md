
# Bill Desk

## Structure

`BillDesk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Required | The issuer id of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type12Enum`](../../doc/models/type-12-enum.md) | Required | **billdesk** |

## Example

```python
from adyen.models.bill_desk import BillDesk
from adyen.models.type_12_enum import Type12Enum

bill_desk = BillDesk(
    issuer='issuer6',
    mtype=Type12Enum.BILLDESK_ONLINE,
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4'
)
```

