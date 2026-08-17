
# Webhook Settings

## Structure

`WebhookSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_settings` | [`List[WebhookSetting]`](../../doc/models/webhook-setting.md) | Optional | The list of webhook settings. |

## Example

```python
from adyen.models.target_3 import Target3
from adyen.models.type_181_enum import Type181Enum
from adyen.models.webhook_setting import WebhookSetting
from adyen.models.webhook_settings import WebhookSettings

webhook_settings = WebhookSettings(
    webhook_settings=[
        WebhookSetting(
            currency='currency8',
            id='id2',
            status='status6',
            target=Target3(
                id='id2',
                mtype=Type181Enum.BALANCEACCOUNT
            ),
            mtype='WebhookSetting'
        ),
        WebhookSetting(
            currency='currency8',
            id='id2',
            status='status6',
            target=Target3(
                id='id2',
                mtype=Type181Enum.BALANCEACCOUNT
            ),
            mtype='WebhookSetting'
        )
    ]
)
```

