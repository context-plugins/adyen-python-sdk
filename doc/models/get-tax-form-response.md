
# Get Tax Form Response

*This model accepts additional fields of type Any.*

## Structure

`GetTaxFormResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | The content of the tax form in the Base64 binary format. |
| `content_type` | `str` | Optional | The content type of the tax form. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2
from adyen.models.get_tax_form_response import GetTaxFormResponse

get_tax_form_response = GetTaxFormResponse(
    content='content0',
    content_type='contentType2',
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    psp_reference='pspReference2',
    result_code='resultCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

