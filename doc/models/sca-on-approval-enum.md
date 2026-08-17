
# Sca on Approval Enum

Shows the status of the Strong Customer Authentication (SCA) process.

Possible values: **required**, **notApplicable**.

## Enumeration

`ScaOnApprovalEnum`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `NOTAPPLICABLE` |
| `REQUIRED` |

## Example

```python
from adyen.models.sca_on_approval_enum import ScaOnApprovalEnum

sca_on_approval = ScaOnApprovalEnum.REQUIRED
```

