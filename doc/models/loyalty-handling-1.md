
# Loyalty Handling 1

Type of Loyalty processing requested by the Sale System.
Possible values:

* **Allowed**
* **Forbidden**
* **Processed**
* **Proposed**
* **Required**

## Enumeration

`LoyaltyHandling1`

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
from adyen.models.loyalty_handling_1 import LoyaltyHandling1

loyalty_handling_1 = LoyaltyHandling1.FORBIDDEN
```

