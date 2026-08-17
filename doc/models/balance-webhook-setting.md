
# Balance Webhook Setting

## Structure

`BalanceWebhookSetting`

## Inherits From

[`WebhookSetting`](../../doc/models/webhook-setting.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List[Condition]`](../../doc/models/condition.md) | Optional | The list of settings and criteria for triggering the [balance webhook](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated). |

## Example

```python
from adyen.models.balance_type_enum import BalanceTypeEnum
from adyen.models.condition import Condition
from adyen.models.condition_type_enum import ConditionTypeEnum
from adyen.models.target_3 import Target3
from adyen.models.type_181_enum import Type181Enum
from adyen.models.webhook_setting import BalanceWebhookSetting

balance_webhook_setting = BalanceWebhookSetting(
    currency='currency6',
    id='id6',
    status='status2',
    target=Target3(
        id='id2',
        mtype=Type181Enum.BALANCEACCOUNT
    ),
    conditions=[
        Condition(
            balance_type=BalanceTypeEnum.BALANCE,
            condition_type=ConditionTypeEnum.LESSTHAN,
            value=214
        ),
        Condition(
            balance_type=BalanceTypeEnum.BALANCE,
            condition_type=ConditionTypeEnum.LESSTHAN,
            value=214
        ),
        Condition(
            balance_type=BalanceTypeEnum.BALANCE,
            condition_type=ConditionTypeEnum.LESSTHAN,
            value=214
        )
    ],
    mtype='balance'
)
```

