
# Modification Result

## Structure

`ModificationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular modification response. |
| `psp_reference` | `str` | Required | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `response` | [`ResponseEnum`](../../doc/models/response-enum.md) | Required | Indicates if the modification request has been received for processing. |

## Example

```python
from adyen.models.modification_result import ModificationResult
from adyen.models.response_enum import ResponseEnum

modification_result = ModificationResult(
    psp_reference='pspReference0',
    response=ResponseEnum.ERROR,
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    }
)
```

