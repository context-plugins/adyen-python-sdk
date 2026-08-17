
# Web Data Exemption

## Structure

`WebDataExemption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason3Enum`](../../doc/models/reason-3-enum.md) | Optional | The reason why the web data was not provided. Possible value: **noOnlinePresence**. |

## Example

```python
from adyen.models.reason_3_enum import Reason3Enum
from adyen.models.web_data_exemption import WebDataExemption

web_data_exemption = WebDataExemption(
    reason=Reason3Enum.NOONLINEPRESENCE
)
```

