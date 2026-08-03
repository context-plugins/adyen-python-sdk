
# Sca on Approval

Shows the status of the Strong Customer Authentication (SCA) process.

Possible values: **required**, **notApplicable**.

## Enumeration

`ScaOnApproval`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `NOTAPPLICABLE` |
| `REQUIRED` |

## Example

```python
from adyen.models.sca_on_approval import ScaOnApproval

sca_on_approval = ScaOnApproval.REQUIRED
```

