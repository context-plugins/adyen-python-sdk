
# Sca Information 1

Information for the Strong Customer Authentication (SCA)

*This model accepts additional fields of type Any.*

## Structure

`ScaInformation1`

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
from adyen.models.sca_information_1 import ScaInformation1
from adyen.models.sca_status import ScaStatus

sca_information_1 = ScaInformation1(
    status=ScaStatus.PERFORMED,
    exemption=ScaExemption.INITIALLIMIT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

