
# Plan

The installment plan, used for [card installments in Japan](https://docs.adyen.com/payment-methods/cards/credit-card-installments#make-a-payment-japan).
and [Mexico](https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico).
By default, this is set to **regular**.

## Enumeration

`Plan`

## Fields

| Name |
|  --- |
| `BONUS` |
| `BUYNOW_PAYLATER` |
| `INTERES_REFUND_PRCTG` |
| `INTEREST_BONUS` |
| `NOINTERES_REFUND_PRCTG` |
| `NOINTEREST_BONUS` |
| `REFUND_PRCTG` |
| `REGULAR` |
| `REVOLVING` |
| `WITH_INTEREST` |

## Example

```python
from adyen.models.plan import Plan

plan = Plan.NOINTERES_REFUND_PRCTG
```

