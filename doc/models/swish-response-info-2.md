
# Swish Response Info 2

**swish** or its variant details

## Structure

`SwishResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_number` | `str` | Optional | Swish number. Format: 10 digits without spaces. For example, **1231111111**.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |

## Example

```python
from adyen.models.swish_response_info_2 import SwishResponseInfo2

swish_response_info_2 = SwishResponseInfo2(
    swish_number='swishNumber2'
)
```

