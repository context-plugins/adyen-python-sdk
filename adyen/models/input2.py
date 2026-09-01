from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.input_command1 import InputCommand1OrStr


class Input2(SdkBaseModel):
    """Data entered by the user, related to the input command."""

    input_command: InputCommand1OrStr = Field(alias="InputCommand")
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

    confirmed_flag: Optional[bool] = Field(default=UNSET, alias="ConfirmedFlag")
    """Indicates te response of the user from the ``GetConfirmation`` input command."""

    function_key: Optional[int] = Field(default=UNSET, alias="FunctionKey")
    """The number of the function key which is typed by the Customer on the POI or the Cashier on the Sale Terminal."""

    text_input: Optional[str] = Field(default=UNSET, alias="TextInput")
    """The text typed by the Customer on the POI or by the Cashier on the Sale Terminal."""

    digit_input: Optional[int] = Field(default=UNSET, alias="DigitInput")
    """The digits typed by the Customer on the POI or by the Cashier on the Sale Terminal."""

    password: Optional[str] = Field(default=UNSET, alias="Password")
    """The text password typed by the Customer on the POI or by the Cashier on the Sale Terminal."""

    menu_entry_number: Optional[list[int]] = Field(default=UNSET, alias="MenuEntryNumber")
    """The index of the menu item (from 1 to n) which is selected by the Cashier on the Sale Terminal. The value -1
    indicates that the immediate upper level of the menu is requested. The value 0 indicates that the root of the menu
    is requested."""


class Input2Dict(TypedDict):
    input_command: InputCommand1OrStr
    confirmed_flag: NotRequired[bool]
    function_key: NotRequired[int]
    text_input: NotRequired[str]
    digit_input: NotRequired[int]
    password: NotRequired[str]
    menu_entry_number: NotRequired[list[int]]
