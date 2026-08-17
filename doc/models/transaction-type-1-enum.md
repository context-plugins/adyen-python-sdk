
# Transaction Type 1 Enum

Possible values:

* **Debit**
* **Credit**
* **ReverseDebit**
* **ReverseCredit**
* **OneTimeReservation**
* **CompletedDeffered**
* **FirstReservation**
* **UpdateReservation**
* **CompletedReservation**
* **CashAdvance**
* **IssuerInstalment**
* **Declined**
* **Failed**
* **Award**
* **ReverseAward**
* **Redemption**
* **ReverseRedemption**
* **Rebate**
* **ReverseRebate**

## Enumeration

`TransactionType1Enum`

## Fields

| Name |
|  --- |
| `DEBIT` |
| `CREDIT` |
| `REVERSEDEBIT` |
| `REVERSECREDIT` |
| `ONETIMERESERVATION` |
| `COMPLETEDDEFFERED` |
| `FIRSTRESERVATION` |
| `UPDATERESERVATION` |
| `COMPLETEDRESERVATION` |
| `CASHADVANCE` |
| `ISSUERINSTALMENT` |
| `DECLINED` |
| `FAILED` |
| `AWARD` |
| `REVERSEAWARD` |
| `REDEMPTION` |
| `REVERSEREDEMPTION` |
| `REBATE` |
| `REVERSEREBATE` |

## Example

```python
from adyen.models.transaction_type_1_enum import TransactionType1Enum

transaction_type_1 = TransactionType1Enum.REVERSEAWARD
```

