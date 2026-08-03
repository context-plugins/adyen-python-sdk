
# Href 51

The link to the list page you are currently viewing.

*This model accepts additional fields of type Any.*

## Structure

`Href51`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href_51 import Href51

href_51 = Href51(
    href='href6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

