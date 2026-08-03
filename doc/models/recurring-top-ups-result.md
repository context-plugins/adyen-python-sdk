
# Recurring Top Ups Result

*This model accepts additional fields of type Any.*

## Structure

`RecurringTopUpsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | [`Link`](../../doc/models/link.md) | Required | - |
| `recurring_top_ups` | [`List[RecurringTopUp]`](../../doc/models/recurring-top-up.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.fixed import Fixed
from adyen.models.last import Last
from adyen.models.link import Link
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous
from adyen.models.recurring_top_up import RecurringTopUp
from adyen.models.recurring_top_ups_result import RecurringTopUpsResult
from adyen.models.schedule_2 import Schedule2
from adyen.models.schedule_type_1 import ScheduleType1
from adyen.models.status_211 import Status211
from adyen.models.target_5 import Target5
from adyen.models.threshold_2 import Threshold2
from adyen.models.top_up_amount import TopUpAmount
from adyen.models.top_up_counterparty import TopUpCounterparty
from adyen.models.trigger import Trigger

recurring_top_ups_result = RecurringTopUpsResult(
    link=Link(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        previous=Previous(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    recurring_top_ups=[
        RecurringTopUp(
            counterparty=TopUpCounterparty(
                transfer_instrument_id='transferInstrumentId4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description0',
            id='id0',
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
            reference_for_beneficiary='referenceForBeneficiary0',
            status=Status211.ACTIVE,
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

