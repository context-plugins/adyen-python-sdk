
# Link 3

A list of hyperlinks to resources related to this response.

*This model accepts additional fields of type Any.*

## Structure

`Link3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | [`First`](../../doc/models/first.md) | Optional | - |
| `last` | [`Last`](../../doc/models/last.md) | Optional | - |
| `next` | [`Next`](../../doc/models/next.md) | Optional | - |
| `previous` | [`Previous`](../../doc/models/previous.md) | Optional | - |
| `mself` | [`Self`](../../doc/models/self.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.link_3 import Link3
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous

link_3 = Link3(
    first=First(
        href='href2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    last=Last(
        href='href2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    next=Next(
        href='href4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    previous=Previous(
        href='href0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mself=Self(
        href='href0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

