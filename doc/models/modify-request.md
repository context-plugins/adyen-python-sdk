
# Modify Request

*This model accepts additional fields of type Any.*

## Structure

`ModifyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular payout request. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `original_reference` | `str` | Required | The PSP reference received in the `/submitThirdParty` response. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.modify_request import ModifyRequest

modify_request = ModifyRequest(
    merchant_account='merchantAccount2',
    original_reference='originalReference6',
    additional_data={
        'key0': 'additionalData0'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

