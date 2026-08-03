
# Store Filtration Mode

Specifies how payment methods should be filtered based on the 'store' parameter:

- 'exclusive': Only payment methods belonging to the specified 'store' are returned.
- 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned.

## Enumeration

`StoreFiltrationMode`

## Fields

| Name |
|  --- |
| `EXCLUSIVE` |
| `INCLUSIVE` |
| `SKIPFILTER` |

## Example

```python
from adyen.models.store_filtration_mode import StoreFiltrationMode

store_filtration_mode = StoreFiltrationMode.INCLUSIVE
```

