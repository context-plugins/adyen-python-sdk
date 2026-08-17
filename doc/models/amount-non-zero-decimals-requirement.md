
# Amount Non Zero Decimals Requirement

## Structure

`AmountNonZeroDecimalsRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies for which routes the amount in a transfer request must have no non-zero decimal places, so the transfer can only be processed if the amount consists of round numbers. |
| `mtype` | `str` | Required, Constant | **amountNonZeroDecimalsRequirement**<br><br>**Value**: `"amountNonZeroDecimalsRequirement"` |

## Example

```python
from adyen.models.amount_non_zero_decimals_requirement import AmountNonZeroDecimalsRequirement

amount_non_zero_decimals_requirement = AmountNonZeroDecimalsRequirement(
    description='description8'
)
```

