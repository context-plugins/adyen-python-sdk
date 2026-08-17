
# Type 64 Enum

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

`Type64Enum`

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
from adyen.models.type_64_enum import Type64Enum

type_64 = Type64Enum.ADYENCARD
```

