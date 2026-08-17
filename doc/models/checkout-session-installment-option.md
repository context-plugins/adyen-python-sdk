
# Checkout Session Installment Option

## Structure

`CheckoutSessionInstallmentOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plans` | [`List[Plan1Enum]`](../../doc/models/plan-1-enum.md) | Optional | Defines the type of installment plan. If not set, defaults to **regular**.<br><br>Possible values:<br><br>* **regular**<br>* **revolving**<br>* **bonus**<br>* **with_interest**<br>* **buynow_paylater**<br>* **nointerest_bonus**<br>* **interest_bonus**<br>* **refund_prctg**<br>* **nointeres_refund_prctg**<br>* **interes_refund_prctg** |
| `preselected_value` | `int` | Optional | Preselected number of installments offered for this payment method. |
| `values` | `List[int]` | Optional | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with `maxValue`. |

## Example

```python
from adyen.models.checkout_session_installment_option import CheckoutSessionInstallmentOption
from adyen.models.plan_1_enum import Plan1Enum

checkout_session_installment_option = CheckoutSessionInstallmentOption(
    plans=[
        Plan1Enum.BUYNOW_PAYLATER,
        Plan1Enum.INTERES_REFUND_PRCTG,
        Plan1Enum.INTEREST_BONUS
    ],
    preselected_value=228,
    values=[
        162
    ]
)
```

