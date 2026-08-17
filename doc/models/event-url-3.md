
# Event Url 3

The list of local and public URLs to send notifications to when using local integrations.

## Structure

`EventUrl3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_local_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more local URLs to send event notifications to when using Terminal API. |
| `event_public_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more public URLs to send event notifications to when using Terminal API. |

## Example

```python
from adyen.models.event_url_3 import EventUrl3
from adyen.models.url import Url

event_url_3 = EventUrl3(
    event_local_urls=[
        Url(
            encrypted=False,
            password='password4',
            url='url4',
            username='username0'
        ),
        Url(
            encrypted=False,
            password='password4',
            url='url4',
            username='username0'
        )
    ],
    event_public_urls=[
        Url(
            encrypted=False,
            password='password8',
            url='url8',
            username='username4'
        )
    ]
)
```

