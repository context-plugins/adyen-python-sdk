
# Priority 1

Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the [payout frequency](https://docs.adyen.com/account/getting-paid#payout-frequency). Depending on the currencies and banks involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.

Possible values:

* **first**: same day.
* **urgent**: the next day.
* **normal**: between 1 and 3 days.

## Enumeration

`Priority1`

## Fields

| Name |
|  --- |
| `FIRST` |
| `NORMAL` |
| `URGENT` |

## Example

```python
from adyen.models.priority_1 import Priority1

priority_1 = Priority1.NORMAL
```

