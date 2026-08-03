
# Sca Information

*This model accepts additional fields of type Any.*

## Structure

`ScaInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exemption` | [`ScaExemption`](../../doc/models/sca-exemption.md) | Optional | - |
| `status` | [`ScaStatus`](../../doc/models/sca-status.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sca_exemption import ScaExemption
from adyen.models.sca_information import ScaInformation
from adyen.models.sca_status import ScaStatus

sca_information = ScaInformation(
    status=ScaStatus.PERFORMED,
    exemption=ScaExemption.SETBYPLATFORM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

