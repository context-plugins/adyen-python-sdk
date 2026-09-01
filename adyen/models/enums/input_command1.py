from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InputCommand1(str, Enum):
    """Type of requested input. Can be: **GetConfirmation**, **TextString**, **DigitString**, **DecimalString** or
    **GetMenuEntry**. Possible values:
    * **DecimalString**
    * **DigitString**
    * **GetAnyKey**
    * **GetConfirmation**
    * **GetFunctionKey**
    * **GetMenuEntry**
    * **Password**
    * **SiteManager**
    * **TextString**"""

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


InputCommand1OrStr: TypeAlias = Annotated[InputCommand1 | str, open_enum_validator(InputCommand1)]
