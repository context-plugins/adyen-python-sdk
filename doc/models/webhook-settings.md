
# Webhook Settings

*This model accepts additional fields of type Any.*

## Structure

`WebhookSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_settings` | [`List[WebhookSetting]`](../../doc/models/webhook-setting.md) | Optional | The list of webhook settings. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.target import Target
from adyen.models.type_18 import Type18
from adyen.models.webhook_setting import WebhookSetting
from adyen.models.webhook_settings import WebhookSettings

webhook_settings = WebhookSettings(
    webhook_settings=[
        WebhookSetting(
            currency='currency8',
            id='id2',
            status='status6',
            target=Target(
                id='id2',
                mtype=Type18.BALANCEACCOUNT,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            mtype='WebhookSetting',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        WebhookSetting(
            currency='currency8',
            id='id2',
            status='status6',
            target=Target(
                id='id2',
                mtype=Type18.BALANCEACCOUNT,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            mtype='WebhookSetting',
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

