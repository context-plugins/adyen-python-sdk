
# Webhook Setting

## Structure

`WebhookSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance.<br><br>**Constraints**: *Minimum Length*: `1` |
| `id` | `str` | Required | The unique identifier of the webhook setting. |
| `status` | `str` | Required | The status of the webhook setting. Possible values:<br><br>* **active**: You receive a balance webhook if any of the conditions in this setting are met.<br>* **inactive**: You do not receive a balance webhook even if the conditions in this settings are met. |
| `target` | [`Target3`](../../doc/models/target-3.md) | Required | The resource about whose balance change you want to get notified. |
| `mtype` | `str` | Optional | - |

## Example

```python
from adyen.models.target_3 import Target3
from adyen.models.type_181_enum import Type181Enum
from adyen.models.webhook_setting import WebhookSetting

webhook_setting = WebhookSetting(
    currency='currency4',
    id='id4',
    status='status6',
    target=Target3(
        id='id2',
        mtype=Type181Enum.BALANCEACCOUNT
    ),
    mtype='WebhookSetting'
)
```

