
# Split Dcc 2

Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).

> This field is in pilot phase, and not yet available for all platforms.

## Structure

`SplitDcc2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_percentage` | `int` | Optional | - |

## Example

```python
from adyen.models.split_dcc_2 import SplitDcc2

split_dcc_2 = SplitDcc2(
    account_holder_percentage=134
)
```

