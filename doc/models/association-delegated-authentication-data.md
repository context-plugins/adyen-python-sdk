
# Association Delegated Authentication Data

*This model accepts additional fields of type Any.*

## Structure

`AssociationDelegatedAuthenticationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to authenticate the request. You obtain this information by using our authentication SDK.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association_delegated_authentication_data import AssociationDelegatedAuthenticationData

association_delegated_authentication_data = AssociationDelegatedAuthenticationData(
    sdk_output='sdkOutput4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

