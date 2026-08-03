
# Status Reason

The reason for the status of the payment instrument.

Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**, **suspectedFraud**, **transactionRule**, **other**.
If the reason is **other**, you must also send the `statusComment` parameter describing the status change.

## Enumeration

`StatusReason`

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
from adyen.models.status_reason import StatusReason

status_reason = StatusReason.ACCOUNTCLOSURE
```

