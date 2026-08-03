
# Valuelink Info

*This model accepts additional fields of type Any.*

## Structure

`ValuelinkInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | Authorisation Mid |
| `pin_support` | [`PinSupport`](../../doc/models/pin-support.md) | Required | - |
| `submitter_id` | `str` | Optional | Submitter ID |
| `terminal_id` | `str` | Optional | Terminal ID |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pin_support import PinSupport
from adyen.models.valuelink_info import ValuelinkInfo

valuelink_info = ValuelinkInfo(
    authorisation_mid='authorisationMid2',
    pin_support=PinSupport.PIN,
    submitter_id='submitterId8',
    terminal_id='terminalId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

