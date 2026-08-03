
# Identification Support 1

Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:

* **HybridCard**
* **LinkedCard**
* **LoyaltyCard**
* **NoCard**

## Enumeration

`IdentificationSupport1`

## Fields

| Name |
|  --- |
| `NOCARD` |
| `LOYALTYCARD` |
| `HYBRIDCARD` |
| `LINKEDCARD` |

## Example

```python
from adyen.models.identification_support_1 import IdentificationSupport1

identification_support_1 = IdentificationSupport1.HYBRIDCARD
```

