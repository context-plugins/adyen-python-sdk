
# Type 72 Enum

The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set to **push**.

Possible values:

* **push**: _push out funds_ to a destination balance account or transfer instrument.

* **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account.

## Enumeration

`Type72Enum`

## Fields

| Name |
|  --- |
| `PULL` |
| `PUSH` |

## Example

```python
from adyen.models.type_72_enum import Type72Enum

type_72 = Type72Enum.PULL
```

