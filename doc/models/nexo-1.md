
# Nexo 1

Settings for a Terminal API integration.

*This model accepts additional fields of type Any.*

## Structure

`Nexo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_urls` | [`NotificationUrl`](../../doc/models/notification-url.md) | Optional | - |
| `encryption_key` | [`Key`](../../doc/models/key.md) | Optional | - |
| `event_urls` | [`EventUrl`](../../doc/models/event-url.md) | Optional | - |
| `nexo_event_urls` | `List[str]` | Optional | One or more URLs to send event messages to when using Terminal API. |
| `notification` | [`Notification`](../../doc/models/notification.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.category_1 import Category1
from adyen.models.event_url import EventUrl
from adyen.models.key import Key
from adyen.models.nexo_1 import Nexo1
from adyen.models.notification import Notification
from adyen.models.notification_url import NotificationUrl
from adyen.models.url import Url

nexo_1 = Nexo1(
    display_urls=NotificationUrl(
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
    ),
    encryption_key=Key(
        identifier='identifier6',
        passphrase='passphrase6',
        version=8,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    event_urls=EventUrl(
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
    ),
    nexo_event_urls=[
        'nexoEventUrls0'
    ],
    notification=Notification(
        category=Category1.SALEWAKEUP,
        details='details2',
        enabled=False,
        show_button=False,
        title='title2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

