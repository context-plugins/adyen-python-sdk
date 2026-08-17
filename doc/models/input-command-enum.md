
# Input Command Enum

Possible values:

* **GetAnyKey**
* **GetConfirmation**
* **SiteManager**
* **TextString**
* **DigitString**
* **DecimalString**
* **GetFunctionKey**
* **GetMenuEntry**
* **Password**

## Enumeration

`InputCommandEnum`

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
from adyen.models.input_command_enum import InputCommandEnum

input_command = InputCommandEnum.DECIMALSTRING
```

