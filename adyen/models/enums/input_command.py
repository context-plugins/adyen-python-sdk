from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InputCommand(str, Enum):
    """Possible values:
    * **GetAnyKey**
    * **GetConfirmation**
    * **SiteManager**
    * **TextString**
    * **DigitString**
    * **DecimalString**
    * **GetFunctionKey**
    * **GetMenuEntry**
    * **Password**"""

    GET_ANY_KEY = "GetAnyKey"
    GET_CONFIRMATION = "GetConfirmation"
    SITE_MANAGER = "SiteManager"
    TEXT_STRING = "TextString"
    DIGIT_STRING = "DigitString"
    DECIMAL_STRING = "DecimalString"
    GET_FUNCTION_KEY = "GetFunctionKey"
    GET_MENU_ENTRY = "GetMenuEntry"
    PASSWORD = "Password"

    __str__ = str.__str__


InputCommandOrStr: TypeAlias = Annotated[InputCommand | str, open_enum_validator(InputCommand)]
