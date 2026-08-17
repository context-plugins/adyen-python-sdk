
# Notification Url

## Structure

`NotificationUrl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more local URLs to send notifications to when using Terminal API. |
| `public_urls` | [`List[Url]`](../../doc/models/url.md) | Optional | One or more public URLs to send notifications to when using Terminal API. |

## Example

```python
from adyen.models.notification_url import NotificationUrl
from adyen.models.url import Url

notification_url = NotificationUrl(
    local_urls=[
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
        ),
        Url(
            encrypted=False,
            password='password4',
            url='url4',
            username='username0'
        )
    ],
    public_urls=[
        Url(
            encrypted=False,
            password='password6',
            url='url6',
            username='username2'
        ),
        Url(
            encrypted=False,
            password='password6',
            url='url6',
            username='username2'
        )
    ]
)
```

