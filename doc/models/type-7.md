
# Type 7

The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set to **push**.

Possible values:

* **push**: _push out funds_ to a destination balance account or transfer instrument.

* **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account.

## Enumeration

`Type7`

## Fields

| Name |
|  --- |
| `PULL` |
| `PUSH` |

## Example

```python
from adyen.models.type_7 import Type7

type_7 = Type7.PULL
```

