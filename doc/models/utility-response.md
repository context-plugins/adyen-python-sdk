
# Utility Response

## Structure

`UtilityResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `origin_keys` | `Dict[str, str]` | Optional | The list of origin keys for all requested domains. For each list item, the key is the domain and the value is the origin key. |

## Example

```python
from adyen.models.utility_response import UtilityResponse

utility_response = UtilityResponse(
    origin_keys={
        'key0': 'originKeys4',
        'key1': 'originKeys5',
        'key2': 'originKeys6'
    }
)
```

