
# Input Data 2

Information related to an Input request. It conveys the target input logical device, the type of input command, and possible minimum and maximum length of the input. In addition, if the requestor might require to receive an Event Notification if a card is inserted in a card reader, with the `NotifyCardInputFlag`.

## Structure

`InputData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device` | [`Device2Enum`](../../doc/models/device-2-enum.md) | Required | Logical device located on a Sale Terminal or a POI Terminal, regarding the class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.<br>Possible values:<br><br>* **CashierDisplay**<br>* **CashierInput**<br>* **CustomerDisplay**<br>* **CustomerInput** |
| `info_qualify` | [`InfoQualify2Enum`](../../doc/models/info-qualify-2-enum.md) | Required | Qualification of the information to send to an output logical device, to display or print to the Cashier or the Customer.<br>Possible values:<br><br>* **CustomerAssistance**<br>* **Display**<br>* **Document**<br>* **Error**<br>* **Input**<br>* **POIReplication**<br>* **Receipt**<br>* **Sound**<br>* **Status**<br>* **Voucher** |
| `input_command` | [`InputCommand1Enum`](../../doc/models/input-command-1-enum.md) | Required | Type of requested input. Can be: **GetConfirmation**, **TextString**, **DigitString**, **DecimalString** or **GetMenuEntry**.<br>Possible values:<br><br>* **DecimalString**<br>* **DigitString**<br>* **GetAnyKey**<br>* **GetConfirmation**<br>* **GetFunctionKey**<br>* **GetMenuEntry**<br>* **Password**<br>* **SiteManager**<br>* **TextString** |
| `notify_card_input_flag` | `bool` | Optional | Request Notification of the card entered in the POI card reader.<br><br>**Default**: `False` |
| `max_input_time` | `int` | Optional | Maximum input time in seconds. Limits the time to answer to an Input request message. |
| `immediate_response_flag` | `bool` | Optional | Indicates whether to request an Immediate response to the message without waiting for the completion of the command.<br><br>**Default**: `False` |
| `min_length` | `int` | Optional | Minimum length of an entered string, or minimum number of entries that can be selected in a menu. |
| `max_length` | `int` | Optional | Maximum length of an entered string, or maximum number of entries that can be selected in a menu. |
| `max_decimal_length` | `int` | Optional | Maximum input length of the decimal part (without decimal point). |
| `wait_user_validation_flag` | `bool` | Optional | Indicates that the user must confirm the entered characters, when the maximum allowed length is reached. During the processing of an Input command `TextString`, `DigitString` or `DecimalString` with `MaxLength` or `MaxDecimalLength` present in the request.<br><br>**Default**: `True` |
| `default_input_string` | `str` | Optional | Default string value for an input command. On the `TextString`, `DigitString` and `DecimalString` input commands: default string displayed on the input field before entering the string. In `GetConfirmation` input command: **Y** for yes, **N** for no.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `default_layout_string` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `string_mask` | `str` | Optional | String mask to get information requiring a specific format. For the processing of an Input command `TextString`, `DigitString` or `DecimalString`. Some information as date or plate number required to be entered with a certain format.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `from_right_to_left_flag` | `bool` | Optional | Indicates if the entered character has to be displayed from the right to the left of the display field.<br><br>**Default**: `False` |
| `mask_characters_flag` | `bool` | Optional | Indicates to mask the characters entered by the user (i.e. replacing in the display of the input, the entered character by a standard character as *).<br><br>**Default**: `False` |
| `beep_key_flag` | `bool` | Optional | Indicates, when the user press a key, if a beep has to be generated (value True).<br><br>**Default**: `False` |
| `global_correction_flag` | `bool` | Optional | Indicates, when the user presses the Correct function key in an input entry, if all the entered characters are removed (value True) or only the last entered character if any (value False).<br><br>**Default**: `False` |
| `disable_cancel_flag` | `bool` | Optional | Indicates if the Cancel function key has to be deactivated (value True).<br><br>**Default**: `False` |
| `disable_correct_flag` | `bool` | Optional | Indicates if the Correct function key has to be deactivated (value True). During the processing of an Input command `GetConfirmation`, `SiteManager`, or `GetMenuEntry`.<br><br>**Default**: `False` |
| `disable_valid_flag` | `bool` | Optional | Indicates if the Valid function key has to be deactivated (value True). During the processing of an Input command `GetConfirmation`, `SiteManager`, or `GetMenuEntry`.<br><br>**Default**: `False` |
| `menu_back_flag` | `bool` | Optional | If it has the value True, it indicates that the Back function key (respectively Home function key) may be used to go back to the immediate upper level of the menu. If it has the value False, it indicates that the current menu level has no parent menu.<br><br>**Default**: `False` |

## Example

```python
from adyen.models.device_2_enum import Device2Enum
from adyen.models.info_qualify_2_enum import InfoQualify2Enum
from adyen.models.input_command_1_enum import InputCommand1Enum
from adyen.models.input_data_2 import InputData2

input_data_2 = InputData2(
    device=Device2Enum.CASHIERDISPLAY,
    info_qualify=InfoQualify2Enum.DOCUMENT,
    input_command=InputCommand1Enum.DIGITSTRING,
    notify_card_input_flag=False,
    max_input_time=226,
    immediate_response_flag=False,
    min_length=58,
    max_length=82,
    wait_user_validation_flag=True,
    from_right_to_left_flag=False,
    mask_characters_flag=False,
    beep_key_flag=False,
    global_correction_flag=False,
    disable_cancel_flag=False,
    disable_correct_flag=False,
    disable_valid_flag=False,
    menu_back_flag=False
)
```

