
# Payment Type 1

Type of payment transaction. Elements requested by the Sale System that are related to the payment only.
Possible values:

* **CashAdvance**
* **CashDeposit**
* **Completion**
* **FirstReservation**
* **Instalment**
* **IssuerInstalment**
* **Normal**
* **OneTimeReservation**
* **PaidOut**
* **Recurring**
* **Refund**
* **UpdateReservation**

## Enumeration

`PaymentType1`

## Fields

| Name |
|  --- |
| `NORMAL` |
| `REFUND` |
| `ONETIMERESERVATION` |
| `FIRSTRESERVATION` |
| `UPDATERESERVATION` |
| `COMPLETION` |
| `CASHADVANCE` |
| `CASHDEPOSIT` |
| `RECURRING` |
| `INSTALMENT` |
| `ISSUERINSTALMENT` |
| `PAIDOUT` |

## Example

```python
from adyen.models.payment_type_1 import PaymentType1

payment_type_1 = PaymentType1.NORMAL
```

