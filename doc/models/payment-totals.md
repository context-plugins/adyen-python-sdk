
# Payment Totals

Totals of the payment transaction during the reconciliation period.

## Structure

`PaymentTotals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`TransactionType11Enum`](../../doc/models/transaction-type-11-enum.md) | Required | Type of transaction for which totals are grouped.<br>Debit, Credit, ReverseDebit, ReverseCredit, OneTimeReservation, CompletedDeffered, FirstReservation, UpdateReservation, CompletedReservation, CashAdvance.<br>Possible values:<br><br>* **Award**<br>* **CashAdvance**<br>* **CompletedDeffered**<br>* **CompletedReservation**<br>* **Credit**<br>* **Debit**<br>* **Declined**<br>* **Failed**<br>* **FirstReservation**<br>* **IssuerInstalment**<br>* **OneTimeReservation**<br>* **Rebate**<br>* **Redemption**<br>* **ReverseAward**<br>* **ReverseCredit**<br>* **ReverseDebit**<br>* **ReverseRebate**<br>* **ReverseRedemption**<br>* **UpdateReservation** |
| `transaction_count` | `int` | Required | Number of processed transaction during the period. |
| `transaction_amount` | `float` | Required | Sum of amount of processed transaction during the period.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |

## Example

```python
from adyen.models.payment_totals import PaymentTotals
from adyen.models.transaction_type_11_enum import TransactionType11Enum

payment_totals = PaymentTotals(
    transaction_type=TransactionType11Enum.UPDATERESERVATION,
    transaction_count=220,
    transaction_amount=21.08
)
```

