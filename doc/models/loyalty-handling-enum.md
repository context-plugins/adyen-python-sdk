
# Loyalty Handling Enum

Possible values:

* **Forbidden**
* **Processed**
* **Allowed**
* **Proposed**
* **Required**

## Enumeration

`LoyaltyHandlingEnum`

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
from adyen.models.loyalty_handling_enum import LoyaltyHandlingEnum

loyalty_handling = LoyaltyHandlingEnum.REQUIRED
```

