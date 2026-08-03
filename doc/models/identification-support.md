
# Identification Support

Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.
Possible values:

* **NoCard**
* **LoyaltyCard**
* **HybridCard**
* **LinkedCard**

## Enumeration

`IdentificationSupport`

## Fields

| Name |
|  --- |
| `NOCARD` |
| `LOYALTYCARD` |
| `HYBRIDCARD` |
| `LINKEDCARD` |

## Example

```python
from adyen.models.identification_support import IdentificationSupport

identification_support = IdentificationSupport.NOCARD
```

