
# Input Command 1

Type of requested input. Can be: **GetConfirmation**, **TextString**, **DigitString**, **DecimalString** or **GetMenuEntry**.
Possible values:

* **DecimalString**
* **DigitString**
* **GetAnyKey**
* **GetConfirmation**
* **GetFunctionKey**
* **GetMenuEntry**
* **Password**
* **SiteManager**
* **TextString**

## Enumeration

`InputCommand1`

## Fields

| Name |
|  --- |
| `GETANYKEY` |
| `GETCONFIRMATION` |
| `SITEMANAGER` |
| `TEXTSTRING` |
| `DIGITSTRING` |
| `DECIMALSTRING` |
| `GETFUNCTIONKEY` |
| `GETMENUENTRY` |
| `PASSWORD` |

## Example

```python
from adyen.models.input_command_1 import InputCommand1

input_command_1 = InputCommand1.DECIMALSTRING
```

