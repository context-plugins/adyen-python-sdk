
# Webhook Setting

*This model accepts additional fields of type Any.*

## Structure

`WebhookSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance.<br><br>**Constraints**: *Minimum Length*: `1` |
| `id` | `str` | Required | The unique identifier of the webhook setting. |
| `status` | `str` | Required | The status of the webhook setting. Possible values:<br><br>* **active**: You receive a balance webhook if any of the conditions in this setting are met.<br>* **inactive**: You do not receive a balance webhook even if the conditions in this settings are met. |
| `target` | [`Target`](../../doc/models/target.md) | Required | - |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.target import Target
from adyen.models.type_18 import Type18
from adyen.models.webhook_setting import WebhookSetting

webhook_setting = WebhookSetting(
    currency='currency4',
    id='id4',
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
```

