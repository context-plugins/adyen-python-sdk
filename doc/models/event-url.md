
# Event Url

*This model accepts additional fields of type Any.*

## Structure

`EventUrl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_local_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more local URLs to send event notifications to when using Terminal API. |
| `event_public_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more public URLs to send event notifications to when using Terminal API. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.event_url import EventUrl
from adyen.models.url import Url

event_url = EventUrl(
    event_local_urls=[
        Url(
            encrypted=False,
            password='password4',
            url='url4',
            username='username0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

