
# Balance Webhook Setting

*This model accepts additional fields of type Any.*

## Structure

`BalanceWebhookSetting`

## Inherits From

[`WebhookSetting`](../../doc/models/webhook-setting.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List[Condition]`](../../doc/models/condition.md) | Optional | The list of settings and criteria for triggering the [balance webhook](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_type import BalanceType
from adyen.models.condition import Condition
from adyen.models.condition_type import ConditionType
from adyen.models.target import Target
from adyen.models.type_18 import Type18
from adyen.models.webhook_setting import BalanceWebhookSetting

balance_webhook_setting = BalanceWebhookSetting(
    currency='currency6',
    id='id6',
    status='status2',
    target=Target(
        id='id2',
        mtype=Type18.BALANCEACCOUNT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    conditions=[
        Condition(
            balance_type=BalanceType.BALANCE,
            condition_type=ConditionType.LESSTHAN,
            value=214,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Condition(
            balance_type=BalanceType.BALANCE,
            condition_type=ConditionType.LESSTHAN,
            value=214,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Condition(
            balance_type=BalanceType.BALANCE,
            condition_type=ConditionType.LESSTHAN,
            value=214,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    mtype='balance',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

