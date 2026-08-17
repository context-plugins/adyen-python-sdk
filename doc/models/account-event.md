
# Account Event

## Structure

`AccountEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event` | [`EventEnum`](../../doc/models/event-enum.md) | Optional | The event.<br><br>> Permitted values: `InactivateAccount`, `RefundNotPaidOutTransfers`.<br>> For more information, refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-process). |
| `execution_date` | `datetime` | Optional | The date on which the event will take place. |
| `reason` | `str` | Optional | The reason why this event has been created. |

## Example

```python
import dateutil.parser

from adyen.models.account_event import AccountEvent
from adyen.models.event_enum import EventEnum

account_event = AccountEvent(
    event=EventEnum.INACTIVATEACCOUNT,
    execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    reason='reason0'
)
```

