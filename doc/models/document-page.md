
# Document Page

*This model accepts additional fields of type Any.*

## Structure

`DocumentPage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_name` | `str` | Optional | - |
| `page_number` | `int` | Optional | - |
| `mtype` | [`Type92`](../../doc/models/type-92.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.document_page import DocumentPage
from adyen.models.type_92 import Type92

document_page = DocumentPage(
    page_name='pageName2',
    page_number=84,
    mtype=Type92.BACK,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

