
# Type 25

The type of Terms of Service.

Possible values:

* **adyenForPlatformsManage**
* **adyenIssuing**
* **adyenForPlatformsAdvanced**
* **adyenCapital**
* **adyenAccount**
* **adyenCard**
* **adyenFranchisee**
* **adyenPccr**
* **adyenChargeCard**
* **kycOnInvite**

## Enumeration

`Type25`

## Fields

| Name |
|  --- |
| `ADYENACCOUNT` |
| `ADYENCAPITAL` |
| `ADYENCARD` |
| `ADYENCHARGECARD` |
| `ADYENFORPLATFORMSADVANCED` |
| `ADYENFORPLATFORMSMANAGE` |
| `ADYENFRANCHISEE` |
| `ADYENISSUING` |
| `ADYENPCCR` |
| `KYCONINVITE` |

## Example

```python
from adyen.models.type_25 import Type25

type_25 = Type25.ADYENCARD
```

