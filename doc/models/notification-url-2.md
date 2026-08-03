
# Notification Url 2

The list of local and public URLs to send display notifications to when using Terminal API.

*This model accepts additional fields of type Any.*

## Structure

`NotificationUrl2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more local URLs to send notifications to when using Terminal API. |
| `public_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more public URLs to send notifications to when using Terminal API. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.notification_url_2 import NotificationUrl2
from adyen.models.url import Url

notification_url_2 = NotificationUrl2(
    local_urls=[
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
    public_urls=[
        Url(
            encrypted=False,
            password='password6',
            url='url6',
            username='username2',
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

