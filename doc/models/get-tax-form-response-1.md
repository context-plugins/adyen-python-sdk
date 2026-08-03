
# Get Tax Form Response 1

*This model accepts additional fields of type Any.*

## Structure

`GetTaxFormResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Required | The content of the tax form in Base64 format. |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.content_type import ContentType
from adyen.models.get_tax_form_response_1 import GetTaxFormResponse1

get_tax_form_response_1 = GetTaxFormResponse1(
    content='content8',
    content_type=ContentType.ENUM_APPLICATIONPDF,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

