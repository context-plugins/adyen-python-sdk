
# Identification Support Enum

Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:

* **NoCard**
* **LoyaltyCard**
* **HybridCard**
* **LinkedCard**

## Enumeration

`IdentificationSupportEnum`

## Fields

| Name |
|  --- |
| `NOCARD` |
| `LOYALTYCARD` |
| `HYBRIDCARD` |
| `LINKEDCARD` |

## Example

```python
from adyen.models.identification_support_enum import IdentificationSupportEnum

identification_support = IdentificationSupportEnum.NOCARD
```

