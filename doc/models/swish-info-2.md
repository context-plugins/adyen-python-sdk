
# Swish Info 2

Details to provide if `type` is **swish**.

- This field is required only if you have a contract with Swish. Swish handles settlement directly with you (not through Adyen).
- If not specified then it's assumed that you are using Adyen's contract with Swish.You don't have a direct relationship with Swish.

## Structure

`SwishInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_number` | `str` | Required | Swish number. Format: 10 digits without spaces. For example, **1231111111**.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |

## Example

```python
from adyen.models.swish_info_2 import SwishInfo2

swish_info_2 = SwishInfo2(
    swish_number='swishNumber6'
)
```

