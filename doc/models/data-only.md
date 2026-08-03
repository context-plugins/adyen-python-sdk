
# Data Only

Required to trigger the [data-only flow](https://docs.adyen.com/online-payments/3d-secure/data-only/). When set to **true**, forces the 3D Secure 2 data-only flow for all transactions where it is possible.

## Enumeration

`DataOnly`

## Fields

| Name |
|  --- |
| `FALSE` |
| `TRUE` |

## Example

```python
from adyen.models.data_only import DataOnly

data_only = DataOnly.FALSE
```

