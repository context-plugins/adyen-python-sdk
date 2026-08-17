
# Create Recurring Top Up

## Structure

`CreateRecurringTopUp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty` | [`TopUpCounterparty1`](../../doc/models/top-up-counterparty-1.md) | Required | The details about the counterparty that is funding the top-up. |
| `description` | `str` | Required | Your description for the recurring top-up.<br><br>Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `140` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Optional | The status of the recurring top-up. If not provided, by default, this is set to **active**.<br><br>Possible values:<br><br>* **active**:  the top up is enabled and funds will be pulled in.<br><br>* **inactive**: the top up is disabled and cannot be triggered. |
| `top_up_amount` | [`TopUpAmount1`](../../doc/models/top-up-amount-1.md) | Required | The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount or a target amount. |
| `trigger` | [`Trigger1`](../../doc/models/trigger-1.md) | Required | The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.create_recurring_top_up import CreateRecurringTopUp
from adyen.models.schedule_21 import Schedule21
from adyen.models.schedule_type_1_enum import ScheduleType1Enum
from adyen.models.status_6_enum import Status6Enum
from adyen.models.top_up_amount_1 import TopUpAmount1
from adyen.models.top_up_counterparty_1 import TopUpCounterparty1
from adyen.models.trigger_1 import Trigger1

create_recurring_top_up = CreateRecurringTopUp(
    counterparty=TopUpCounterparty1(
        transfer_instrument_id='transferInstrumentId4'
    ),
    description='description8',
    top_up_amount=TopUpAmount1(
        fixed=Amount17(
            currency='currency0',
            value=164
        ),
        target=Amount17(
            currency='currency2',
            value=188
        )
    ),
    trigger=Trigger1(
        threshold=Amount17(
            currency='currency8',
            value=32
        ),
        schedule=Schedule21(
            mtype=ScheduleType1Enum.WEEKDAYS
        )
    ),
    reference_for_beneficiary='referenceForBeneficiary8',
    status=Status6Enum.ACTIVE
)
```

