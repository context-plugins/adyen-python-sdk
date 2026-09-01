from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MenuEntryTag(str, Enum):
    """Characteristics related to the selection of a menu entry. Possible values:
    * **Selectable**
    * **NonSelectable**
    * **SubMenu**
    * **NonSelectableSubMenu**"""

    SELECTABLE = "Selectable"
    NON_SELECTABLE = "NonSelectable"
    SUB_MENU = "SubMenu"
    NON_SELECTABLE_SUB_MENU = "NonSelectableSubMenu"

    __str__ = str.__str__


MenuEntryTagOrStr: TypeAlias = Annotated[MenuEntryTag | str, open_enum_validator(MenuEntryTag)]
