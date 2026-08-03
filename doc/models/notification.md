
# Notification

*This model accepts additional fields of type Any.*

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category1`](../../doc/models/category-1.md) | Optional | - |
| `details` | `str` | Optional | The text shown in the prompt which opens when you select the notification button. For example, the description of the input box for pay-at-table. |
| `enabled` | `bool` | Optional | Enables sending event notifications either by pressing the Confirm key on terminals with a keypad or by tapping the event notification button on the terminal screen. |
| `show_button` | `bool` | Optional | Shows or hides the event notification button on the screen of terminal models that have a keypad. |
| `title` | `str` | Optional | The name of the notification button on the terminal screen. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.category_1 import Category1
from adyen.models.notification import Notification

notification = Notification(
    category=Category1.SALEWAKEUP,
    details='details2',
    enabled=False,
    show_button=False,
    title='title2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

