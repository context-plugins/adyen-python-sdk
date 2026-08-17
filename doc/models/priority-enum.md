
# Priority Enum

Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the [payout frequency](https://docs.adyen.com/account/getting-paid#payout-frequency). Depending on the currencies and banks involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.

Possible values:

* **first**: same day.
* **urgent**: the next day.
* **normal**: between 1 and 3 days.

## Enumeration

`PriorityEnum`

## Fields

| Name |
|  --- |
| `FIRST` |
| `NORMAL` |
| `URGENT` |

## Example

```python
from adyen.models.priority_enum import PriorityEnum

priority = PriorityEnum.URGENT
```

