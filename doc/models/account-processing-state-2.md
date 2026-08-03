
# Account Processing State 2

The processing state of the account holder.

*This model accepts additional fields of type Any.*

## Structure

`AccountProcessingState2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disable_reason` | `str` | Optional | The reason why processing has been disabled. |
| `disabled` | `bool` | Optional | Indicates whether the processing of payments is allowed. |
| `processed_from` | [`ProcessedFrom`](../../doc/models/processed-from.md) | Optional | - |
| `processed_to` | [`ProcessedTo`](../../doc/models/processed-to.md) | Optional | - |
| `tier_number` | `int` | Optional | The processing tier that the account holder occupies. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_processing_state_2 import AccountProcessingState2
from adyen.models.processed_from import ProcessedFrom
from adyen.models.processed_to import ProcessedTo

account_processing_state_2 = AccountProcessingState2(
    disable_reason='disableReason4',
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
    tier_number=88,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

