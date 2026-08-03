
# Token Details

*This model accepts additional fields of type Any.*

## Structure

`TokenDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_data` | `Dict[str, str]` | Optional | - |
| `token_data_type` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.token_details import TokenDetails

token_details = TokenDetails(
    token_data={
        'key0': 'tokenData1',
        'key1': 'tokenData2'
    },
    token_data_type='tokenDataType6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

