
# Authentication Result Request

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationResultRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which the authentication was processed. |
| `psp_reference` | `str` | Required | The pspReference identifier for the transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_result_request import AuthenticationResultRequest

authentication_result_request = AuthenticationResultRequest(
    merchant_account='merchantAccount2',
    psp_reference='pspReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

