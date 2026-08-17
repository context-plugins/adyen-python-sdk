
# Token Details

## Structure

`TokenDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token_data` | `Dict[str, str]` | Optional | - |
| `token_data_type` | `str` | Optional | - |

## Example

```python
from adyen.models.token_details import TokenDetails

token_details = TokenDetails(
    token_data={
        'key0': 'tokenData1',
        'key1': 'tokenData2'
    },
    token_data_type='tokenDataType6'
)
```

