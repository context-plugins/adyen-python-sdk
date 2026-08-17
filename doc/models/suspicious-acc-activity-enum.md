
# Suspicious Acc Activity Enum

Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the cardholder account.
Allowed values:

* **01** — No suspicious activity has been observed
* **02** — Suspicious activity has been observed

## Enumeration

`SuspiciousAccActivityEnum`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |

## Example

```python
from adyen.models.suspicious_acc_activity_enum import SuspiciousAccActivityEnum

suspicious_acc_activity = SuspiciousAccActivityEnum.ENUM_01
```

