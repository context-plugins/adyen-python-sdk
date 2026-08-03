
# Balance Sweep Configurations Response

*This model accepts additional fields of type Any.*

## Structure

`BalanceSweepConfigurationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |
| `sweeps` | [`List[SweepConfigurationV2]`](../../doc/models/sweep-configuration-v2.md) | Required | List of sweeps associated with the balance account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_sweep_configurations_response import BalanceSweepConfigurationsResponse
from adyen.models.category import Category
from adyen.models.priority import Priority
from adyen.models.reason import Reason
from adyen.models.sweep_configuration_v_2 import SweepConfigurationV2
from adyen.models.sweep_counterparty import SweepCounterparty
from adyen.models.sweep_schedule import SweepSchedule
from adyen.models.type_6 import Type6

balance_sweep_configurations_response = BalanceSweepConfigurationsResponse(
    has_next=False,
    has_previous=False,
    sweeps=[
        SweepConfigurationV2(
            counterparty=SweepCounterparty(
                balance_account_id='balanceAccountId0',
                merchant_account='merchantAccount0',
                transfer_instrument_id='transferInstrumentId4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            currency='currency2',
            id='id2',
            schedule=SweepSchedule(
                mtype=Type6.WEEKLY,
                cron_expression='cronExpression4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            category=Category.PLATFORMPAYMENT,
            description='description2',
            priorities=[
                Priority.REGULAR,
                Priority.WIRE,
                Priority.CROSSBORDER
            ],
            reason=Reason.ACCOUNTHIERARCHYNOTACTIVE,
            reason_detail='reasonDetail8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

