
# Three Ds 2 Result Request

*This model accepts additional fields of type Any.*

## Structure

`ThreeDs2ResultRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `psp_reference` | `str` | Required | The pspReference returned in the /authorise call. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_ds_2_result_request import ThreeDs2ResultRequest

three_ds_2_result_request = ThreeDs2ResultRequest(
    merchant_account='merchantAccount8',
    psp_reference='pspReference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

