
# Payment Acc Ind

Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.
Allowed values:

* **01** — No account (guest checkout)
* **02** — During this transaction
* **03** — Less than 30 days
* **04** — 30–60 days
* **05** — More than 60 days

## Enumeration

`PaymentAccInd`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |
| `ENUM_05` |

## Example

```python
from adyen.models.payment_acc_ind import PaymentAccInd

payment_acc_ind = PaymentAccInd.ENUM_04
```

