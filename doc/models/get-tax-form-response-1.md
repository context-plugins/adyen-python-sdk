
# Get Tax Form Response 1

## Structure

`GetTaxFormResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Required | The content of the tax form in Base64 format. |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Optional | The content type of the tax form.<br><br>Possible values:<br><br>* **application/pdf** |

## Example

```python
from adyen.models.content_type_enum import ContentTypeEnum
from adyen.models.get_tax_form_response_1 import GetTaxFormResponse1

get_tax_form_response_1 = GetTaxFormResponse1(
    content='content8',
    content_type=ContentTypeEnum.ENUM_APPLICATIONPDF
)
```

