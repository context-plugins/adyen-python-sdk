
# Transaction Type 1

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

`TransactionType1`

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
from adyen.models.transaction_type_1 import TransactionType1

transaction_type_1 = TransactionType1.REVERSEAWARD
```

