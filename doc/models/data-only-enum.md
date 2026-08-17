
# Data Only Enum

Required to trigger the [data-only flow](https://docs.adyen.com/online-payments/3d-secure/data-only/). When set to **true**, forces the 3D Secure 2 data-only flow for all transactions where it is possible.

## Enumeration

`DataOnlyEnum`

## Fields

| Name |
|  --- |
| `FALSE` |
| `TRUE` |

## Example

```python
from adyen.models.data_only_enum import DataOnlyEnum

data_only = DataOnlyEnum.FALSE
```

