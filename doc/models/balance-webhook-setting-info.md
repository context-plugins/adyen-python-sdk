
# Balance Webhook Setting Info

## Structure

`BalanceWebhookSettingInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List[Condition]`](../../doc/models/condition.md) | Optional | The array of conditions a balance change must meet for Adyen to send the webhook.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `20` |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance.<br><br>**Constraints**: *Minimum Length*: `1` |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Required | The status of the webhook setting. Possible values:<br><br>* **active**: You receive a balance webhook if any of the conditions in this setting are met.<br>* **inactive**: You do not receive a balance webhook even if the conditions in this settings are met. |
| `target` | [`Target1`](../../doc/models/target-1.md) | Required | The type and ID of the resource about whose balance changes you want to be notified. |
| `mtype` | `str` | Required, Constant | The type of the webhook you are configuring. Set to **balance**.<br><br>**Value**: `"balance"` |

## Example

```python
from adyen.models.balance_type_enum import BalanceTypeEnum
from adyen.models.balance_webhook_setting_info import BalanceWebhookSettingInfo
from adyen.models.condition import Condition
from adyen.models.condition_type_enum import ConditionTypeEnum
from adyen.models.status_6_enum import Status6Enum
from adyen.models.target_1 import Target1
from adyen.models.type_181_enum import Type181Enum

balance_webhook_setting_info = BalanceWebhookSettingInfo(
    currency='currency8',
    status=Status6Enum.ACTIVE,
    target=Target1(
        id='id2',
        mtype=Type181Enum.BALANCEACCOUNT
    ),
    conditions=[
        Condition(
            balance_type=BalanceTypeEnum.BALANCE,
            condition_type=ConditionTypeEnum.LESSTHAN,
            value=214
        )
    ]
)
```

