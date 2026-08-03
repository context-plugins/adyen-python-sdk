
# Disable Permit Request

*This model accepts additional fields of type Any.*

## Structure

`DisablePermitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `token` | `str` | Required | The permit token to disable. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disable_permit_request import DisablePermitRequest

disable_permit_request = DisablePermitRequest(
    merchant_account='merchantAccount8',
    token='token0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

