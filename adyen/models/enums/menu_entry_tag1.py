from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MenuEntryTag1(str, Enum):
    """Characteristics related to the selection of a menu entry. Possible values:
    * **NonSelectable**
    * **NonSelectableSubMenu**
    * **Selectable**
    * **SubMenu**"""

    SELECTABLE = "Selectable"
    NON_SELECTABLE = "NonSelectable"
    SUB_MENU = "SubMenu"
    NON_SELECTABLE_SUB_MENU = "NonSelectableSubMenu"

    __str__ = str.__str__


MenuEntryTag1OrStr: TypeAlias = Annotated[MenuEntryTag1 | str, open_enum_validator(MenuEntryTag1)]
