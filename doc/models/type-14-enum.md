
# Type 14 Enum

Default payment method details. Common for scheme payment methods, and for simple payment method details.

## Enumeration

`Type14Enum`

## Fields

| Name |
|  --- |
| `BCMC` |
| `SCHEME` |
| `NETWORKTOKEN` |
| `GIFTCARD` |
| `CARD` |
| `CLICKTOPAY` |

## Example

```python
from adyen.models.type_14_enum import Type14Enum

type_14 = Type14Enum.BCMC
```

