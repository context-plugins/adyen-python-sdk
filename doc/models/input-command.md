
# Input Command

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

`InputCommand`

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
from adyen.models.input_command import InputCommand

input_command = InputCommand.DECIMALSTRING
```

