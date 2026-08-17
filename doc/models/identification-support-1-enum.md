
# Identification Support 1 Enum

Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:

* **HybridCard**
* **LinkedCard**
* **LoyaltyCard**
* **NoCard**

## Enumeration

`IdentificationSupport1Enum`

## Fields

| Name |
|  --- |
| `NOCARD` |
| `LOYALTYCARD` |
| `HYBRIDCARD` |
| `LINKEDCARD` |

## Example

```python
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum

identification_support_1 = IdentificationSupport1Enum.HYBRIDCARD
```

