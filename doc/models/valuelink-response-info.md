
# Valuelink Response Info

*This model accepts additional fields of type Any.*

## Structure

`ValuelinkResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Optional | Authorisation Mid |
| `pin_support` | [`PinSupport`](../../doc/models/pin-support.md) | Optional | - |
| `submitter_id` | `str` | Optional | Submitter ID |
| `terminal_id` | `str` | Optional | Terminal ID |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pin_support import PinSupport
from adyen.models.valuelink_response_info import ValuelinkResponseInfo

valuelink_response_info = ValuelinkResponseInfo(
    authorisation_mid='authorisationMid6',
    pin_support=PinSupport.PIN,
    submitter_id='submitterId2',
    terminal_id='terminalId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

