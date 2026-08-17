
# Message Category 1 Enum

Category of message.
Possible values:

* **Abort**
* **Admin**
* **BalanceInquiry**
* **Batch**
* **CardAcquisition**
* **CardReaderInit**
* **CardReaderPowerOff**
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
* **None**
* **PIN**
* **Payment**
* **Print**
* **Reconciliation**
* **Reversal**
* **Sound**
* **StoredValue**
* **TransactionStatus**
* **Transmit**

## Enumeration

`MessageCategory1Enum`

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
from adyen.models.message_category_1_enum import MessageCategory1Enum

message_category_1 = MessageCategory1Enum.EVENT
```

