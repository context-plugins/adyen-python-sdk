
# Input 2

Data entered by the user, related to the input command.

## Structure

`Input2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `input_command` | [`InputCommand1Enum`](../../doc/models/input-command-1-enum.md) | Required | Type of requested input. Can be: **GetConfirmation**, **TextString**, **DigitString**, **DecimalString** or **GetMenuEntry**.<br>Possible values:<br><br>* **DecimalString**<br>* **DigitString**<br>* **GetAnyKey**<br>* **GetConfirmation**<br>* **GetFunctionKey**<br>* **GetMenuEntry**<br>* **Password**<br>* **SiteManager**<br>* **TextString** |
| `confirmed_flag` | `bool` | Optional | Indicates te response of the user from the `GetConfirmation` input command. |
| `function_key` | `int` | Optional | The number of the function key which is typed by the Customer on the POI or the Cashier on the Sale Terminal. |
| `text_input` | `str` | Optional | The text typed by the Customer on the POI or by the Cashier on the Sale Terminal. |
| `digit_input` | `int` | Optional | The digits typed by the Customer on the POI or by the Cashier on the Sale Terminal. |
| `password` | `str` | Optional | The text password typed by the Customer on the POI or by the Cashier on the Sale Terminal. |
| `menu_entry_number` | `List[int]` | Optional | The index of the menu item (from 1 to n) which is selected by the Cashier on the Sale Terminal. The value -1 indicates that the immediate upper level of the menu is requested. The value 0 indicates that the root of the menu is requested. |

## Example

```python
from adyen.models.input_2 import Input2
from adyen.models.input_command_1_enum import InputCommand1Enum

input_2 = Input2(
    input_command=InputCommand1Enum.GETMENUENTRY,
    confirmed_flag=False,
    function_key=152,
    text_input='TextInput0',
    digit_input=134,
    password='Password6'
)
```

