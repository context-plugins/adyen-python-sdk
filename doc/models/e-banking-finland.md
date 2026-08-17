
# E Banking Finland

## Structure

`EBankingFinland`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The Ebanking Finland issuer value of the shopper's selected bank. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | `str` | Required, Constant | **ebanking_FI**<br><br>**Value**: `"ebanking_FI"` |

## Example

```python
from adyen.models.e_banking_finland import EBankingFinland

e_banking_finland = EBankingFinland(
    checkout_attempt_id='checkoutAttemptId8',
    issuer='issuer2',
    sdk_data='sdkData8'
)
```

