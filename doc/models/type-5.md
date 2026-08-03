
# Type 5

The type of additional bank identification, depending on the country.

Possible values:

* **auBsbCode**: The 6-digit [Australian Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or spaces.
* **caRoutingNumber**: The 9-digit [Canadian routing number](https://en.wikipedia.org/wiki/Routing_number_(Canada)), in EFT format, without separators or spaces.
* **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spaces
* **usRoutingNumber**: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or spaces.

## Enumeration

`Type5`

## Fields

| Name |
|  --- |
| `AUBSBCODE` |
| `CAROUTINGNUMBER` |
| `GBSORTCODE` |
| `USROUTINGNUMBER` |

## Example

```python
from adyen.models.type_5 import Type5

type_5 = Type5.AUBSBCODE
```

