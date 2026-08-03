
# Balance Type

Define the type of balance about which you want to get notified. Possible values:

* **available**: the balance available for use.

* **balance**: the sum of transactions that have already been settled.

* **pending**: the sum of transactions that will be settled in the future.

* **reserved**: the balance currently held in reserve.

## Enumeration

`BalanceType`

## Fields

| Name |
|  --- |
| `BALANCE` |
| `AVAILABLE` |
| `PENDING` |
| `RESERVED` |

## Example

```python
from adyen.models.balance_type import BalanceType

balance_type = BalanceType.BALANCE
```

