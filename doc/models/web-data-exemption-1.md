
# Web Data Exemption 1

The reason why the web data is not provided.

## Structure

`WebDataExemption1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason3Enum`](../../doc/models/reason-3-enum.md) | Optional | The reason why the web data was not provided. Possible value: **noOnlinePresence**. |

## Example

```python
from adyen.models.reason_3_enum import Reason3Enum
from adyen.models.web_data_exemption_1 import WebDataExemption1

web_data_exemption_1 = WebDataExemption1(
    reason=Reason3Enum.NOONLINEPRESENCE
)
```

