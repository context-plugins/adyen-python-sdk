
# Message Category 2 Enum

Category of message.
CardAcquisition, Display, Input, Loyalty, Payment, Print, CardReaderInit, CardReaderPowerOff.
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

`MessageCategory2Enum`

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
from adyen.models.message_category_2_enum import MessageCategory2Enum

message_category_2 = MessageCategory2Enum.ENUM_NONE
```

