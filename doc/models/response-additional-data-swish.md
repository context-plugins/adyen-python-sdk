
# Response Additional Data Swish

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataSwish`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_payer_alias` | `str` | Optional | A Swish shopper's telephone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_swish import ResponseAdditionalDataSwish

response_additional_data_swish = ResponseAdditionalDataSwish(
    swish_payer_alias='swish.payerAlias0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

