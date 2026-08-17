
# Recurring Top Ups Result

## Structure

`RecurringTopUpsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | [`Link`](../../doc/models/link.md) | Required | - |
| `recurring_top_ups` | [`List[RecurringTopUp]`](../../doc/models/recurring-top-up.md) | Required | - |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.link import Link
from adyen.models.links_element import LinksElement
from adyen.models.recurring_top_up import RecurringTopUp
from adyen.models.recurring_top_ups_result import RecurringTopUpsResult
from adyen.models.schedule_21 import Schedule21
from adyen.models.schedule_type_1_enum import ScheduleType1Enum
from adyen.models.status_6_enum import Status6Enum
from adyen.models.top_up_amount_1 import TopUpAmount1
from adyen.models.top_up_counterparty_1 import TopUpCounterparty1
from adyen.models.trigger_1 import Trigger1

recurring_top_ups_result = RecurringTopUpsResult(
    link=Link(
        first=LinksElement(
            href='href2'
        ),
        last=LinksElement(
            href='href2'
        ),
        next=LinksElement(
            href='href4'
        ),
        previous=LinksElement(
            href='href0'
        ),
        mself=LinksElement(
            href='href0'
        )
    ),
    recurring_top_ups=[
        RecurringTopUp(
            counterparty=TopUpCounterparty1(
                transfer_instrument_id='transferInstrumentId4'
            ),
            description='description0',
            id=None,
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
            reference_for_beneficiary='referenceForBeneficiary0',
            status=Status6Enum.ACTIVE
        )
    ]
)
```

