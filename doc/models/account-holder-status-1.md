
# Account Holder Status 1

The new status of the Account Holder.

## Structure

`AccountHolderStatus1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List[AccountEvent]`](../../doc/models/account-event.md) | Optional | A list of events scheduled for the account holder. |
| `payout_state` | [`AccountPayoutState2`](../../doc/models/account-payout-state-2.md) | Optional | The payout state of the account holder. |
| `processing_state` | [`AccountProcessingState2`](../../doc/models/account-processing-state-2.md) | Optional | The processing state of the account holder. |
| `status` | [`Status12Enum`](../../doc/models/status-12-enum.md) | Required | The status of the account holder.<br><br>> Permitted values: `Active`, `Inactive`, `Suspended`, `Closed`. |
| `status_reason` | `str` | Optional | The reason why the status was assigned to the account holder. |

## Example

```python
import dateutil.parser

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_status_1 import AccountHolderStatus1
from adyen.models.account_payout_state_2 import AccountPayoutState2
from adyen.models.account_processing_state_2 import AccountProcessingState2
from adyen.models.amount import Amount
from adyen.models.event_enum import EventEnum
from adyen.models.status_12_enum import Status12Enum

account_holder_status_1 = AccountHolderStatus1(
    status=Status12Enum.INACTIVE,
    events=[
        AccountEvent(
            event=EventEnum.INACTIVATEACCOUNT,
            execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            reason='reason6'
        ),
        AccountEvent(
            event=EventEnum.INACTIVATEACCOUNT,
            execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            reason='reason6'
        )
    ],
    payout_state=AccountPayoutState2(
        allow_payout=False,
        disable_reason='disableReason2',
        disabled=False,
        not_allowed_reason='notAllowedReason4',
        payout_limit=Amount(
            currency='currency8',
            value=88
        )
    ),
    processing_state=AccountProcessingState2(
        disable_reason='disableReason2',
        disabled=False,
        processed_from=Amount(
            currency='currency4',
            value=148
        ),
        processed_to=Amount(
            currency='currency2',
            value=54
        ),
        tier_number=156
    ),
    status_reason='statusReason6'
)
```

