
# Loyalty Handling

Possible values:

* **Forbidden**
* **Processed**
* **Allowed**
* **Proposed**
* **Required**

## Enumeration

`LoyaltyHandling`

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
from adyen.models.loyalty_handling import LoyaltyHandling

loyalty_handling = LoyaltyHandling.REQUIRED
```

