
# Association Initiate Request

*This model accepts additional fields of type Any.*

## Structure

`AssociationInitiateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Required | The list of unique identifiers of the resources that you are associating with the SCA device.<br><br>Maximum: 5 strings. |
| `mtype` | [`Type103`](../../doc/models/type-103.md) | Required | The type of resource that you are associating with the SCA device.<br><br>Possible value: **PaymentInstrument** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association_initiate_request import AssociationInitiateRequest
from adyen.models.type_103 import Type103

association_initiate_request = AssociationInitiateRequest(
    ids=[
        'ids3'
    ],
    mtype=Type103.PAYMENTINSTRUMENT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

