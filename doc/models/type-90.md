
# Type 90

The type of tracking event.

Possible values:

- **internalReview**: the transfer was flagged because it does not comply with Adyen's risk policy.

## Enumeration

`Type90`

## Fields

| Name |
|  --- |
| `INTERNALREVIEW` |

## Example

```python
from adyen.models.type_90 import Type90

type_90 = Type90.INTERNALREVIEW
```

