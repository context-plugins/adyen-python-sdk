
# Connectivity 1

Settings for terminal connectivity features.

*This model accepts additional fields of type Any.*

## Structure

`Connectivity1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `simcard_status` | [`SimcardStatus`](../../doc/models/simcard-status.md) | Optional | - |
| `terminal_ip_address_url` | [`EventUrl`](../../doc/models/event-url.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.connectivity_1 import Connectivity1
from adyen.models.event_url import EventUrl
from adyen.models.simcard_status import SimcardStatus
from adyen.models.url import Url

connectivity_1 = Connectivity1(
    simcard_status=SimcardStatus.ACTIVATED,
    terminal_ip_address_url=EventUrl(
        event_local_urls=[
            Url(
                encrypted=False,
                password='password4',
                url='url4',
                username='username0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        event_public_urls=[
            Url(
                encrypted=False,
                password='password8',
                url='url8',
                username='username4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Url(
                encrypted=False,
                password='password8',
                url='url8',
                username='username4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

