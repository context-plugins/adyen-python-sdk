
# Swish Info

## Structure

`SwishInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_number` | `str` | Required | Swish number. Format: 10 digits without spaces. For example, **1231111111**.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |

## Example

```python
from adyen.models.swish_info import SwishInfo

swish_info = SwishInfo(
    swish_number='swishNumber4'
)
```

