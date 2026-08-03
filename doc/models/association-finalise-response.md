
# Association Finalise Response

*This model accepts additional fields of type Any.*

## Structure

`AssociationFinaliseResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | The unique identifier of the SCA device you associated with a resource. |
| `ids` | `List[str]` | Optional | The list of unique identifiers of the resources that you associated with the SCA device. |
| `mtype` | [`Type123`](../../doc/models/type-123.md) | Required | The type of resource that you associated with the SCA device. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association_finalise_response import AssociationFinaliseResponse
from adyen.models.type_123 import Type123

association_finalise_response = AssociationFinaliseResponse(
    mtype=Type123.PAYMENT_INSTRUMENT,
    device_id='deviceId2',
    ids=[
        'ids3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

