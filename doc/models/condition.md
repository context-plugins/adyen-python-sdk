
# Condition

## Structure

`Condition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_type` | [`BalanceTypeEnum`](../../doc/models/balance-type-enum.md) | Required | Define the type of balance about which you want to get notified. Possible values:<br><br>* **available**: the balance available for use.<br><br>* **balance**: the sum of transactions that have already been settled.<br><br>* **pending**: the sum of transactions that will be settled in the future.<br><br>* **reserved**: the balance currently held in reserve. |
| `condition_type` | [`ConditionTypeEnum`](../../doc/models/condition-type-enum.md) | Required | Define when you want to get notified about a balance change. Possible values:<br><br>* **greaterThan**: the balance in the account(s) exceeds the specified `value`.<br><br>* **greaterThanOrEqual**: the balance in the account(s) reaches or exceeds the specified `value`.<br><br>* **lessThan**: the balance in the account(s) drops below the specified `value`.<br><br>* **lessThanOrEqual**: the balance in the account(s) reaches to drops below the specified `value`. |
| `value` | `int` | Required | The value limit in the specified balance type and currency, in minor units. |

## Example

```python
from adyen.models.balance_type_enum import BalanceTypeEnum
from adyen.models.condition import Condition
from adyen.models.condition_type_enum import ConditionTypeEnum

condition = Condition(
    balance_type=BalanceTypeEnum.BALANCE,
    condition_type=ConditionTypeEnum.LESSTHAN,
    value=194
)
```

