
# Status Reason 2 Enum

The reason for updating the status of the payment instrument.

Possible values: **lost**, **stolen**, **damaged**, **suspectedFraud**, **expired**, **endOfLife**, **accountClosure**, **other**.
If the reason is **other**, you must also send the `statusComment` parameter describing the status change.

## Enumeration

`StatusReason2Enum`

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
from adyen.models.status_reason_2_enum import StatusReason2Enum

status_reason_2 = StatusReason2Enum.ACCOUNTCLOSURE
```

