
# Adyen Fees

Deducts the fees due to Adyen (markup or commission) from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`AdyenFees`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.adyen_fees import AdyenFees

adyen_fees = AdyenFees.DEDUCTFROMLIABLEACCOUNT
```

