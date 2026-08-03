
# Ship Address Usage Ind

Indicates when the shipping address used for this transaction was first used with the 3DS Requestor.
Allowed values:

* **01** — This transaction
* **02** — Less than 30 days
* **03** — 30–60 days
* **04** — More than 60 days

## Enumeration

`ShipAddressUsageInd`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |

## Example

```python
from adyen.models.ship_address_usage_ind import ShipAddressUsageInd

ship_address_usage_ind = ShipAddressUsageInd.ENUM_01
```

