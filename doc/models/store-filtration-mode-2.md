
# Store Filtration Mode 2

Specifies how payment methods should be filtered based on the `store` parameter:

- **exclusive**: Only payment methods belonging to the specified `store` are returned.
- **inclusive**: Payment methods from the `store` and those not associated with any other store are returned.

## Enumeration

`StoreFiltrationMode2`

## Fields

| Name |
|  --- |
| `EXCLUSIVE` |
| `INCLUSIVE` |
| `SKIPFILTER` |

## Example

```python
from adyen.models.store_filtration_mode_2 import StoreFiltrationMode2

store_filtration_mode_2 = StoreFiltrationMode2.SKIPFILTER
```

