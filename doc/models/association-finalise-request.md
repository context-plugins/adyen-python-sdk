
# Association Finalise Request

*This model accepts additional fields of type Any.*

## Structure

`AssociationFinaliseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Required | The list of unique identifiers of the resources that you are associating with the SCA device.<br><br>Maximum: 5 strings. |
| `strong_customer_authentication` | [`AssociationDelegatedAuthenticationData`](../../doc/models/association-delegated-authentication-data.md) | Required | - |
| `mtype` | [`Type103`](../../doc/models/type-103.md) | Required | The type of resource that you are associating with the SCA device.<br><br>Possible value: **PaymentInstrument** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association_delegated_authentication_data import AssociationDelegatedAuthenticationData
from adyen.models.association_finalise_request import AssociationFinaliseRequest
from adyen.models.type_103 import Type103

association_finalise_request = AssociationFinaliseRequest(
    ids=[
        'ids3'
    ],
    strong_customer_authentication=AssociationDelegatedAuthenticationData(
        sdk_output='sdkOutput4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mtype=Type103.PAYMENTINSTRUMENT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

