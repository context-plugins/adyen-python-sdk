
# Message Category

Possible values:

* **Abort**
* **Admin**
* **BalanceInquiry**
* **CardAcquisition**
* **Diagnosis**
* **Display**
* **EnableService**
* **Event**
* **GetTotals**
* **Input**
* **InputUpdate**
* **Login**
* **Logout**
* **Loyalty**
* **Payment**
* **Print**
* **Reconciliation**
* **Reversal**
* **StoredValue**
* **TransactionStatus**
* **None**

## Enumeration

`MessageCategory`

## Fields

| Name |
|  --- |
| `ABORT` |
| `ADMIN` |
| `BALANCEINQUIRY` |
| `CARDACQUISITION` |
| `DIAGNOSIS` |
| `DISPLAY` |
| `ENABLESERVICE` |
| `EVENT` |
| `GETTOTALS` |
| `INPUT` |
| `INPUTUPDATE` |
| `LOGIN` |
| `LOGOUT` |
| `LOYALTY` |
| `PAYMENT` |
| `PRINT` |
| `RECONCILIATION` |
| `REVERSAL` |
| `STOREDVALUE` |
| `TRANSACTIONSTATUS` |
| `ENUM_NONE` |

## Example

```python
from adyen.models.message_category import MessageCategory

message_category = MessageCategory.TRANSACTIONSTATUS
```

