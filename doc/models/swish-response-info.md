
# Swish Response Info

## Structure

`SwishResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_number` | `str` | Optional | Swish number. Format: 10 digits without spaces. For example, **1231111111**.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |

## Example

```python
from adyen.models.swish_response_info import SwishResponseInfo

swish_response_info = SwishResponseInfo(
    swish_number='swishNumber6'
)
```

