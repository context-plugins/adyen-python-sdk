
# Links 3

*This model accepts additional fields of type Any.*

## Structure

`Links3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | [`Next`](../../doc/models/next.md) | Optional | - |
| `prev` | [`Prev`](../../doc/models/prev.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.links_3 import Links3
from adyen.models.next import Next
from adyen.models.prev import Prev

links_3 = Links3(
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

