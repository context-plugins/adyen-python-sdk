
# Document Page

## Structure

`DocumentPage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_name` | `str` | Optional | - |
| `page_number` | `int` | Optional | - |
| `mtype` | [`Type91Enum`](../../doc/models/type-91-enum.md) | Optional | - |

## Example

```python
from adyen.models.document_page import DocumentPage
from adyen.models.type_91_enum import Type91Enum

document_page = DocumentPage(
    page_name='pageName2',
    page_number=84,
    mtype=Type91Enum.BACK
)
```

