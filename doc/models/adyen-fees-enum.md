
# Adyen Fees Enum

Deducts the fees due to Adyen (markup or commission) from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`AdyenFeesEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.adyen_fees_enum import AdyenFeesEnum

adyen_fees = AdyenFeesEnum.DEDUCTFROMLIABLEACCOUNT
```

