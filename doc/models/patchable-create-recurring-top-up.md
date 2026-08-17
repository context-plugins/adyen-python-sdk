
# Patchable Create Recurring Top Up

## Structure

`PatchableCreateRecurringTopUp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description for the recurring top-up.<br><br>Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `140` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Optional | The status of the recurring top-up. If not provided, by default, this is set to **active**.<br><br>Possible values:<br><br>* **active**:  the top up is enabled and funds will be pulled in.<br><br>* **inactive**: the top up is disabled and cannot be triggered. |
| `top_up_amount` | [`PatchableTopUpAmount2`](../../doc/models/patchable-top-up-amount-2.md) | Optional | The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount or a target amount. |
| `trigger` | [`PatchableTrigger2`](../../doc/models/patchable-trigger-2.md) | Optional | The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold. |

## Example

```python
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.patchable_amount_dto_1 import PatchableAmountDTO1
from adyen.models.patchable_create_recurring_top_up import PatchableCreateRecurringTopUp
from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.patchable_top_up_amount_2 import PatchableTopUpAmount2
from adyen.models.patchable_trigger_2 import PatchableTrigger2
from adyen.models.schedule_type_1_enum import ScheduleType1Enum
from adyen.models.status_6_enum import Status6Enum

patchable_create_recurring_top_up = PatchableCreateRecurringTopUp(
    description='description6',
    reference_for_beneficiary='referenceForBeneficiary6',
    status=Status6Enum.ACTIVE,
    top_up_amount=PatchableTopUpAmount2(
        fixed=PatchableAmountDTO(
            currency='currency2',
            value=164
        ),
        target=PatchableAmountDTO(
            currency='currency2',
            value=164
        )
    ),
    trigger=PatchableTrigger2(
        schedule=PatchableSchedule(
            mtype=ScheduleType1Enum.MONTHLY
        ),
        threshold=PatchableAmountDTO1(
            currency='currency8',
            value=32
        )
    )
)
```

