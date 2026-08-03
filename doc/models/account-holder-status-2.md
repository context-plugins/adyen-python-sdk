
# Account Holder Status 2

The status of the new account holder.

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderStatus2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List[AccountEvent]`](../../doc/models/account-event.md) | Optional | A list of events scheduled for the account holder. |
| `payout_state` | [`AccountPayoutState`](../../doc/models/account-payout-state.md) | Optional | - |
| `processing_state` | [`AccountProcessingState`](../../doc/models/account-processing-state.md) | Optional | - |
| `status` | [`Status1`](../../doc/models/status-1.md) | Required | - |
| `status_reason` | `str` | Optional | The reason why the status was assigned to the account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_status_2 import AccountHolderStatus2
from adyen.models.account_payout_state import AccountPayoutState
from adyen.models.account_processing_state import AccountProcessingState
from adyen.models.event import Event
from adyen.models.payout_limit import PayoutLimit
from adyen.models.processed_from import ProcessedFrom
from adyen.models.processed_to import ProcessedTo
from adyen.models.status_1 import Status1

account_holder_status_2 = AccountHolderStatus2(
    status=Status1.ACTIVE,
    events=[
        AccountEvent(
            event=Event.INACTIVATEACCOUNT,
            execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            reason='reason6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    payout_state=AccountPayoutState(
        allow_payout=False,
        disable_reason='disableReason2',
        disabled=False,
        not_allowed_reason='notAllowedReason4',
        payout_limit=PayoutLimit(
            currency='currency8',
            value=88,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    processing_state=AccountProcessingState(
        disable_reason='disableReason2',
        disabled=False,
        processed_from=ProcessedFrom(
            currency='currency4',
            value=148,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        processed_to=ProcessedTo(
            currency='currency2',
            value=54,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        tier_number=156,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    status_reason='statusReason8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

