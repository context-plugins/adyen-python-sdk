
# Notification

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`CategoryEnum`](../../doc/models/category-enum.md) | Optional | The type of event notification sent when you select the notification button. |
| `details` | `str` | Optional | The text shown in the prompt which opens when you select the notification button. For example, the description of the input box for pay-at-table. |
| `enabled` | `bool` | Optional | Enables sending event notifications either by pressing the Confirm key on terminals with a keypad or by tapping the event notification button on the terminal screen. |
| `show_button` | `bool` | Optional | Shows or hides the event notification button on the screen of terminal models that have a keypad. |
| `title` | `str` | Optional | The name of the notification button on the terminal screen. |

## Example

```python
from adyen.models.category_enum import CategoryEnum
from adyen.models.notification import Notification

notification = Notification(
    category=CategoryEnum.SALEWAKEUP,
    details='details2',
    enabled=False,
    show_button=False,
    title='title2'
)
```

