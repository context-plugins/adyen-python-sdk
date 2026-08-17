
# Adyen Markup Enum

Deducts the transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/what-is-interchange) from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`AdyenMarkupEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.adyen_markup_enum import AdyenMarkupEnum

adyen_markup = AdyenMarkupEnum.DEDUCTFROMLIABLEACCOUNT
```

