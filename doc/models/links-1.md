
# Links 1

Contains redirection URLs to guide the user to the appropriate page, after a successful payment or a cancellation.

*This model accepts additional fields of type Any.*

## Structure

`Links1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cancel` | [`Href`](../../doc/models/href.md) | Optional | - |
| `success` | [`Href`](../../doc/models/href.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.href import Href
from adyen.models.links_1 import Links1

links_1 = Links1(
    cancel=Href(
        href='href4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    success=Href(
        href='href2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

