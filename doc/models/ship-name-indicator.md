
# Ship Name Indicator

Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction.
Allowed values:

* **01** — Account Name identical to shipping Name
* **02** — Account Name different to shipping Name

## Enumeration

`ShipNameIndicator`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |

## Example

```python
from adyen.models.ship_name_indicator import ShipNameIndicator

ship_name_indicator = ShipNameIndicator.ENUM_01
```

