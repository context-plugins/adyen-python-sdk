
# Balance Webhook Setting Info Update

*This model accepts additional fields of type Any.*

## Structure

`BalanceWebhookSettingInfoUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List[Condition]`](../../doc/models/condition.md) | Optional | The array of conditions a balance change must meet for Adyen to send the webhook.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `20` |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance.<br><br>**Constraints**: *Minimum Length*: `1` |
| `status` | [`Status19`](../../doc/models/status-19.md) | Optional | - |
| `target` | [`TargetUpdate`](../../doc/models/target-update.md) | Optional | - |
| `mtype` | [`Type20`](../../doc/models/type-20.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_type import BalanceType
from adyen.models.balance_webhook_setting_info_update import BalanceWebhookSettingInfoUpdate
from adyen.models.condition import Condition
from adyen.models.condition_type import ConditionType
from adyen.models.status_19 import Status19
from adyen.models.target_update import TargetUpdate
from adyen.models.type_18 import Type18
from adyen.models.type_20 import Type20

balance_webhook_setting_info_update = BalanceWebhookSettingInfoUpdate(
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
        )
    ],
    currency='currency2',
    status=Status19.ACTIVE,
    target=TargetUpdate(
        id='id2',
        mtype=Type18.BALANCEACCOUNT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mtype=Type20.BALANCE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

