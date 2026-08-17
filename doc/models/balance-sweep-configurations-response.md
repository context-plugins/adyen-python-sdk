
# Balance Sweep Configurations Response

## Structure

`BalanceSweepConfigurationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |
| `sweeps` | [`List[SweepConfigurationV2]`](../../doc/models/sweep-configuration-v2.md) | Required | List of sweeps associated with the balance account. |

## Example

```python
from adyen.models.balance_sweep_configurations_response import BalanceSweepConfigurationsResponse
from adyen.models.category_1_enum import Category1Enum
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.sweep_configuration_v_2 import SweepConfigurationV2
from adyen.models.sweep_counterparty_1 import SweepCounterparty1
from adyen.models.sweep_schedule_1 import SweepSchedule1
from adyen.models.type_62_enum import Type62Enum
from adyen.models.type_72_enum import Type72Enum

balance_sweep_configurations_response = BalanceSweepConfigurationsResponse(
    has_next=False,
    has_previous=False,
    sweeps=[
        SweepConfigurationV2(
            counterparty=SweepCounterparty1(
                balance_account_id='balanceAccountId0',
                merchant_account='merchantAccount0',
                transfer_instrument_id='transferInstrumentId4'
            ),
            currency='currency2',
            id=None,
            schedule=SweepSchedule1(
                mtype=Type62Enum.WEEKLY,
                cron_expression='cronExpression4'
            ),
            category=Category1Enum.PLATFORMPAYMENT,
            description='description2',
            priorities=[
                Priority1Enum.REGULAR,
                Priority1Enum.WIRE,
                Priority1Enum.CROSSBORDER
            ],
            mtype=Type72Enum.PUSH
        )
    ]
)
```

