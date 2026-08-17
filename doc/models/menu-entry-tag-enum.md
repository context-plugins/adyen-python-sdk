
# Menu Entry Tag Enum

Characteristics related to the selection of a menu entry.
Possible values:

* **Selectable**
* **NonSelectable**
* **SubMenu**
* **NonSelectableSubMenu**

## Enumeration

`MenuEntryTagEnum`

## Fields

| Name |
|  --- |
| `SELECTABLE` |
| `NONSELECTABLE` |
| `SUBMENU` |
| `NONSELECTABLESUBMENU` |

## Example

```python
from adyen.models.menu_entry_tag_enum import MenuEntryTagEnum

menu_entry_tag = MenuEntryTagEnum.SELECTABLE
```

