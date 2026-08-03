
# Loyalty Handling 2

Type of Loyalty processing requested by the Sale System. An way to specify what the POI has to handle concerning the loyalty.
Possible values:

* **Allowed**
* **Forbidden**
* **Processed**
* **Proposed**
* **Required**

## Enumeration

`LoyaltyHandling2`

## Fields

| Name |
|  --- |
| `FORBIDDEN` |
| `PROCESSED` |
| `ALLOWED` |
| `PROPOSED` |
| `REQUIRED` |

## Example

```python
from adyen.models.loyalty_handling_2 import LoyaltyHandling2

loyalty_handling_2 = LoyaltyHandling2.REQUIRED
```

