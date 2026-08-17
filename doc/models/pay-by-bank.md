
# Pay by Bank

## Structure

`PayByBank`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The PayByBank issuer value of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | `str` | Required, Constant | **paybybank**<br><br>**Value**: `"paybybank"` |

## Example

```python
from adyen.models.pay_by_bank import PayByBank

pay_by_bank = PayByBank(
    checkout_attempt_id='checkoutAttemptId6',
    issuer='issuer0',
    sdk_data='sdkData0'
)
```

