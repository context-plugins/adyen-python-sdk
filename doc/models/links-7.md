
# Links 7

Reference to resources connected with the store.

*This model accepts additional fields of type Any.*

## Structure

`Links7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mself` | [`Self`](../../doc/models/self.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.links_7 import Links7
from adyen.models.mself import Self

links_7 = Links7(
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

