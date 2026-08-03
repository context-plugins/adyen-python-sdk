
# Utility Response

*This model accepts additional fields of type Any.*

## Structure

`UtilityResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `origin_keys` | `Dict[str, str]` | Optional | The list of origin keys for all requested domains. For each list item, the key is the domain and the value is the origin key. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.utility_response import UtilityResponse

utility_response = UtilityResponse(
    origin_keys={
        'key0': 'originKeys4',
        'key1': 'originKeys5',
        'key2': 'originKeys6'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

