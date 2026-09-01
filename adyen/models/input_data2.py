from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.device2 import Device2OrStr
from .enums.info_qualify2 import InfoQualify2OrStr
from .enums.input_command1 import InputCommand1OrStr


class InputData2(SdkBaseModel):
    """Information related to an Input request. It conveys the target input logical device, the type of input command,
    and possible minimum and maximum length of the input. In addition, if the requestor might require to receive an
    Event Notification if a card is inserted in a card reader, with the ``NotifyCardInputFlag``."""

    device: Device2OrStr = Field(alias="Device")
    """Logical device located on a Sale Terminal or a POI Terminal, regarding the class of information to output
    (display, print or store), or input (keyboard) for the Cashier or the Customer. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    info_qualify: InfoQualify2OrStr = Field(alias="InfoQualify")
    """Qualification of the information to send to an output logical device, to display or print to the Cashier or the
    Customer. Possible values:
    * **CustomerAssistance**
    * **Display**
    * **Document**
    * **Error**
    * **Input**
    * **POIReplication**
    * **Receipt**
    * **Sound**
    * **Status**
    * **Voucher**"""

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

    notify_card_input_flag: Optional[bool] = Field(default=UNSET, alias="NotifyCardInputFlag")
    """Request Notification of the card entered in the POI card reader."""

    max_input_time: Optional[int] = Field(default=UNSET, alias="MaxInputTime")
    """Maximum input time in seconds. Limits the time to answer to an Input request message."""

    immediate_response_flag: Optional[bool] = Field(default=UNSET, alias="ImmediateResponseFlag")
    """Indicates whether to request an Immediate response to the message without waiting for the completion of the
    command."""

    min_length: Optional[int] = Field(default=UNSET, alias="MinLength")
    """Minimum length of an entered string, or minimum number of entries that can be selected in a menu."""

    max_length: Optional[int] = Field(default=UNSET, alias="MaxLength")
    """Maximum length of an entered string, or maximum number of entries that can be selected in a menu."""

    max_decimal_length: Optional[int] = Field(default=UNSET, alias="MaxDecimalLength")
    """Maximum input length of the decimal part (without decimal point)."""

    wait_user_validation_flag: Optional[bool] = Field(default=UNSET, alias="WaitUserValidationFlag")
    """Indicates that the user must confirm the entered characters, when the maximum allowed length is reached. During
    the processing of an Input command ``TextString``, ``DigitString`` or ``DecimalString`` with ``MaxLength`` or
    ``MaxDecimalLength`` present in the request."""

    default_input_string: Optional[str] = Field(default=UNSET, alias="DefaultInputString")
    """Default string value for an input command. On the ``TextString``, ``DigitString`` and ``DecimalString`` input
    commands: default string displayed on the input field before entering the string. In ``GetConfirmation`` input
    command: **Y** for yes, **N** for no."""

    default_layout_string: Optional[str] = Field(default=UNSET, alias="DefaultLayoutString")
    string_mask: Optional[str] = Field(default=UNSET, alias="StringMask")
    """String mask to get information requiring a specific format. For the processing of an Input command
    ``TextString``, ``DigitString`` or ``DecimalString``. Some information as date or plate number required to be
    entered with a certain format."""

    from_right_to_left_flag: Optional[bool] = Field(default=UNSET, alias="FromRightToLeftFlag")
    """Indicates if the entered character has to be displayed from the right to the left of the display field."""

    mask_characters_flag: Optional[bool] = Field(default=UNSET, alias="MaskCharactersFlag")
    """Indicates to mask the characters entered by the user (i.e. replacing in the display of the input, the entered
    character by a standard character as *)."""

    beep_key_flag: Optional[bool] = Field(default=UNSET, alias="BeepKeyFlag")
    """Indicates, when the user press a key, if a beep has to be generated (value True)."""

    global_correction_flag: Optional[bool] = Field(default=UNSET, alias="GlobalCorrectionFlag")
    """Indicates, when the user presses the Correct function key in an input entry, if all the entered characters are
    removed (value True) or only the last entered character if any (value False)."""

    disable_cancel_flag: Optional[bool] = Field(default=UNSET, alias="DisableCancelFlag")
    """Indicates if the Cancel function key has to be deactivated (value True)."""

    disable_correct_flag: Optional[bool] = Field(default=UNSET, alias="DisableCorrectFlag")
    """Indicates if the Correct function key has to be deactivated (value True). During the processing of an Input
    command ``GetConfirmation``, ``SiteManager``, or ``GetMenuEntry``."""

    disable_valid_flag: Optional[bool] = Field(default=UNSET, alias="DisableValidFlag")
    """Indicates if the Valid function key has to be deactivated (value True). During the processing of an Input command
    ``GetConfirmation``, ``SiteManager``, or ``GetMenuEntry``."""

    menu_back_flag: Optional[bool] = Field(default=UNSET, alias="MenuBackFlag")
    """If it has the value True, it indicates that the Back function key (respectively Home function key) may be used to
    go back to the immediate upper level of the menu. If it has the value False, it indicates that the current menu
    level has no parent menu."""


class InputData2Dict(TypedDict):
    device: Device2OrStr
    info_qualify: InfoQualify2OrStr
    input_command: InputCommand1OrStr
    notify_card_input_flag: NotRequired[bool]
    max_input_time: NotRequired[int]
    immediate_response_flag: NotRequired[bool]
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    max_decimal_length: NotRequired[int]
    wait_user_validation_flag: NotRequired[bool]
    default_input_string: NotRequired[str]
    default_layout_string: NotRequired[str]
    string_mask: NotRequired[str]
    from_right_to_left_flag: NotRequired[bool]
    mask_characters_flag: NotRequired[bool]
    beep_key_flag: NotRequired[bool]
    global_correction_flag: NotRequired[bool]
    disable_cancel_flag: NotRequired[bool]
    disable_correct_flag: NotRequired[bool]
    disable_valid_flag: NotRequired[bool]
    menu_back_flag: NotRequired[bool]
