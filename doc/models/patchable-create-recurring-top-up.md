
# Patchable Create Recurring Top Up

*This model accepts additional fields of type Any.*

## Structure

`PatchableCreateRecurringTopUp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description for the recurring top-up.<br><br>Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `140` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `status` | `Any` | Optional | - |
| `top_up_amount` | [`PatchableTopUpAmount`](../../doc/models/patchable-top-up-amount.md) | Optional | - |
| `trigger` | [`PatchableTrigger`](../../doc/models/patchable-trigger.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_amount_dto import PatchableAmountDto
from adyen.models.patchable_create_recurring_top_up import PatchableCreateRecurringTopUp
from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.patchable_top_up_amount import PatchableTopUpAmount
from adyen.models.patchable_trigger import PatchableTrigger
from adyen.models.schedule_type_1 import ScheduleType1
from adyen.models.threshold_3 import Threshold3

patchable_create_recurring_top_up = PatchableCreateRecurringTopUp(
    description='description6',
    reference_for_beneficiary='referenceForBeneficiary6',
    status=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    top_up_amount=PatchableTopUpAmount(
        fixed=PatchableAmountDto(
            currency='currency2',
            value=164,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        target=PatchableAmountDto(
            currency='currency2',
            value=164,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    trigger=PatchableTrigger(
        schedule=PatchableSchedule(
            mtype=ScheduleType1.MONTHLY,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        threshold=Threshold3(
            currency='currency8',
            value=32,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

