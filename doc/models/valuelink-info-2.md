
# Valuelink Info 2

Details to provide if `type` is **valuelink**.

*This model accepts additional fields of type Any.*

## Structure

`ValuelinkInfo2`

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
from adyen.models.valuelink_info_2 import ValuelinkInfo2

valuelink_info_2 = ValuelinkInfo2(
    authorisation_mid='authorisationMid2',
    pin_support=PinSupport.PIN,
    submitter_id='submitterId8',
    terminal_id='terminalId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

