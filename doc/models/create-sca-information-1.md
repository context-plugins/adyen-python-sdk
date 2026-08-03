
# Create Sca Information 1

Information for the Strong Customer Authentication (SCA)

*This model accepts additional fields of type Any.*

## Structure

`CreateScaInformation1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exemption` | [`ScaExemption`](../../doc/models/sca-exemption.md) | Optional | - |
| `sca_on_approval` | `bool` | Optional | Indicates whether to initiate Strong Customer Authentication (SCA) later, during approval, or immediately after you submit this request. Possible values:<br><br>* **true**: you can initiate SCA later, during approval, for all pending transfer limits.<br>* **false** (default): you initiate SCA immediately after submitting the transfer limit request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_sca_information_1 import CreateScaInformation1
from adyen.models.sca_exemption import ScaExemption

create_sca_information_1 = CreateScaInformation1(
    exemption=ScaExemption.INITIALLIMIT,
    sca_on_approval=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

