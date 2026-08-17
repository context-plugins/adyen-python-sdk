
# Loyalty Handling 1 Enum

Type of Loyalty processing requested by the Sale System.
Possible values:

* **Allowed**
* **Forbidden**
* **Processed**
* **Proposed**
* **Required**

## Enumeration

`LoyaltyHandling1Enum`

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
from adyen.models.loyalty_handling_1_enum import LoyaltyHandling1Enum

loyalty_handling_1 = LoyaltyHandling1Enum.FORBIDDEN
```

