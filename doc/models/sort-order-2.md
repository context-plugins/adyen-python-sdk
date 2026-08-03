
# Sort Order 2

Determines the sort order of the returned transactions. The sort order is based on the creation date of the transaction.

Possible values:

- **asc**: Ascending order, from oldest to most recent.

- **desc**: Descending order, from most recent to oldest.

Default value: **asc**.

## Enumeration

`SortOrder2`

## Fields

| Name |
|  --- |
| `ASC` |
| `DESC` |

## Example

```python
from adyen.models.sort_order_2 import SortOrder2

sort_order_2 = SortOrder2.ASC
```

