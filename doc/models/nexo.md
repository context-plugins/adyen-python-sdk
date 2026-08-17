
# Nexo

## Structure

`Nexo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_urls` | [`NotificationUrl2`](../../doc/models/notification-url-2.md) | Optional | The list of local and public URLs to send display notifications to when using Terminal API. |
| `encryption_key` | [`Key1`](../../doc/models/key-1.md) | Optional | The key you share with Adyen to secure local communications when using Terminal API. |
| `event_urls` | [`EventUrl2`](../../doc/models/event-url-2.md) | Optional | The list of local and public URLs to send event notifications to when using Terminal API. |
| `nexo_event_urls` | `List[str]` | Optional | One or more URLs to send event messages to when using Terminal API. |
| `notification` | [`Notification2`](../../doc/models/notification-2.md) | Optional | Configures sending event notifications by pressing a button on a terminal, for example used for pay-at-table. |

## Example

```python
from adyen.models.category_enum import CategoryEnum
from adyen.models.event_url_2 import EventUrl2
from adyen.models.key_1 import Key1
from adyen.models.nexo import Nexo
from adyen.models.notification_2 import Notification2
from adyen.models.notification_url_2 import NotificationUrl2
from adyen.models.url import Url

nexo = Nexo(
    display_urls=NotificationUrl2(
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
            )
        ]
    ),
    encryption_key=Key1(
        identifier='identifier6',
        passphrase='passphrase6',
        version=8
    ),
    event_urls=EventUrl2(
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
    ),
    nexo_event_urls=[
        'nexoEventUrls4'
    ],
    notification=Notification2(
        category=CategoryEnum.SALEWAKEUP,
        details='details2',
        enabled=False,
        show_button=False,
        title='title2'
    )
)
```

