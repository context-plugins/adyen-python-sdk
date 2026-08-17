
# Status Reason Enum

The reason for the status of the payment instrument.

Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**, **suspectedFraud**, **transactionRule**, **other**.
If the reason is **other**, you must also send the `statusComment` parameter describing the status change.

## Enumeration

`StatusReasonEnum`

## Fields

| Name |
|  --- |
| `ACCOUNTCLOSURE` |
| `DAMAGED` |
| `ENDOFLIFE` |
| `EXPIRED` |
| `LOST` |
| `OTHER` |
| `STOLEN` |
| `SUSPECTEDFRAUD` |
| `TRANSACTIONRULE` |

## Example

```python
from adyen.models.status_reason_enum import StatusReasonEnum

status_reason = StatusReasonEnum.ACCOUNTCLOSURE
```

