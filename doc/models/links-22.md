
# Links 22

Contains links to the next and previous page whenever applicable.

*This model accepts additional fields of type Any.*

## Structure

`Links22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | [`Next`](../../doc/models/next.md) | Optional | - |
| `prev` | [`Prev`](../../doc/models/prev.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.links_22 import Links22
from adyen.models.next import Next
from adyen.models.prev import Prev

links_22 = Links22(
    next=Next(
        href='href4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    prev=Prev(
        href='href8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

