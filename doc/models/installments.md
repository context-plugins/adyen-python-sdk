
# Installments

Contains installment settings. For more information, refer to [Installments](https://docs.adyen.com/payment-methods/cards/credit-card-installments).

## Structure

`Installments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extra` | `int` | Optional | Defines the bonus percentage, refund percentage or if the transaction is Buy now Pay later.<br>Used for [card installments in Mexico](https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico) |
| `plan` | [`PlanEnum`](../../doc/models/plan-enum.md) | Optional | The installment plan, used for [card installments in Japan](https://docs.adyen.com/payment-methods/cards/credit-card-installments#make-a-payment-japan).<br>and [Mexico](https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico).<br>By default, this is set to **regular**. |
| `value` | `int` | Required | Defines the number of installments.<br>Usually, the maximum allowed number of installments is capped. For example, it may not be possible to split a payment in more than 24 installments. The acquirer sets this upper limit, so its value may vary.<br>This value can be zero for Installments processed in Mexico. |

## Example

```python
from adyen.models.installments import Installments
from adyen.models.plan_enum import PlanEnum

installments = Installments(
    value=58,
    extra=50,
    plan=PlanEnum.REFUND_PRCTG
)
```

