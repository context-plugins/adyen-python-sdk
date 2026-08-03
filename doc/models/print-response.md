
# Print Response

It conveys the result of the print, parallel to the message request, except if response not required and absent.
Content of the Print Response message.

*This model accepts additional fields of type Any.*

## Structure

`PrintResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier2`](../../doc/models/document-qualifier-2.md) | Required | - |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.document_qualifier_2 import DocumentQualifier2
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.print_response import PrintResponse
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

print_response = PrintResponse(
    document_qualifier=DocumentQualifier2.VOUCHER,
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

