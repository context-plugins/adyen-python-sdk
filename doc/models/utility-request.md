
# Utility Request

*This model accepts additional fields of type Any.*

## Structure

`UtilityRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `origin_domains` | `List[str]` | Required | The list of origin domains, for which origin keys are requested. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.utility_request import UtilityRequest

utility_request = UtilityRequest(
    origin_domains=[
        'originDomains6',
        'originDomains7',
        'originDomains8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

