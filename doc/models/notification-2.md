
# Notification 2

Configures sending event notifications by pressing a button on a terminal, for example used for pay-at-table.

## Structure

`Notification2`

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
from adyen.models.notification_2 import Notification2

notification_2 = Notification2(
    category=CategoryEnum.SALEWAKEUP,
    details='details4',
    enabled=False,
    show_button=False,
    title='title0'
)
```

