
# Modification Result

*This model accepts additional fields of type Any.*

## Structure

`ModificationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular modification response. |
| `psp_reference` | `str` | Required | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `response` | [`Response`](../../doc/models/response.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.modification_result import ModificationResult
from adyen.models.response import Response

modification_result = ModificationResult(
    psp_reference='pspReference0',
    response=Response.ERROR,
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

