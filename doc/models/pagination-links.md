
# Pagination Links

*This model accepts additional fields of type Any.*

## Structure

`PaginationLinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | [`First`](../../doc/models/first.md) | Required | - |
| `last` | [`Last`](../../doc/models/last.md) | Required | - |
| `next` | [`Next`](../../doc/models/next.md) | Optional | - |
| `prev` | [`Prev`](../../doc/models/prev.md) | Optional | - |
| `mself` | [`Self`](../../doc/models/self.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev

pagination_links = PaginationLinks(
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
    mself=Self(
        href='href0',
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

