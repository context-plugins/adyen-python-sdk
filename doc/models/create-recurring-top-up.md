
# Create Recurring Top Up

*This model accepts additional fields of type Any.*

## Structure

`CreateRecurringTopUp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty` | [`TopUpCounterparty`](../../doc/models/top-up-counterparty.md) | Required | - |
| `description` | `str` | Required | Your description for the recurring top-up.<br><br>Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `140` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `status` | [`Status211`](../../doc/models/status-211.md) | Optional | - |
| `top_up_amount` | [`TopUpAmount`](../../doc/models/top-up-amount.md) | Required | - |
| `trigger` | [`Trigger`](../../doc/models/trigger.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_recurring_top_up import CreateRecurringTopUp
from adyen.models.fixed import Fixed
from adyen.models.schedule_2 import Schedule2
from adyen.models.schedule_type_1 import ScheduleType1
from adyen.models.status_211 import Status211
from adyen.models.target_5 import Target5
from adyen.models.threshold_2 import Threshold2
from adyen.models.top_up_amount import TopUpAmount
from adyen.models.top_up_counterparty import TopUpCounterparty
from adyen.models.trigger import Trigger

create_recurring_top_up = CreateRecurringTopUp(
    counterparty=TopUpCounterparty(
        transfer_instrument_id='transferInstrumentId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description8',
    top_up_amount=TopUpAmount(
        fixed=Fixed(
            currency='currency0',
            value=164,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        target=Target5(
            currency='currency2',
            value=188,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    trigger=Trigger(
        threshold=Threshold2(
            currency='currency8',
            value=32,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        schedule=Schedule2(
            mtype=ScheduleType1.WEEKDAYS,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference_for_beneficiary='referenceForBeneficiary8',
    status=Status211.ACTIVE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

