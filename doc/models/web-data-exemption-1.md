
# Web Data Exemption 1

The reason why the web data is not provided.

*This model accepts additional fields of type Any.*

## Structure

`WebDataExemption1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason1`](../../doc/models/reason-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.reason_1 import Reason1
from adyen.models.web_data_exemption_1 import WebDataExemption1

web_data_exemption_1 = WebDataExemption1(
    reason=Reason1.NOONLINEPRESENCE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

