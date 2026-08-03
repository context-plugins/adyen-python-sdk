
# Association Initiate Response

*This model accepts additional fields of type Any.*

## Structure

`AssociationInitiateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the association process.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association_initiate_response import AssociationInitiateResponse

association_initiate_response = AssociationInitiateResponse(
    sdk_input='sdkInput2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

