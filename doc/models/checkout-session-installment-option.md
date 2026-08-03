
# Checkout Session Installment Option

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSessionInstallmentOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plans` | [`List[Plan1]`](../../doc/models/plan-1.md) | Optional | Defines the type of installment plan. If not set, defaults to **regular**.<br><br>Possible values:<br><br>* **regular**<br>* **revolving**<br>* **bonus**<br>* **with_interest**<br>* **buynow_paylater**<br>* **nointerest_bonus**<br>* **interest_bonus**<br>* **refund_prctg**<br>* **nointeres_refund_prctg**<br>* **interes_refund_prctg** |
| `preselected_value` | `int` | Optional | Preselected number of installments offered for this payment method. |
| `values` | `List[int]` | Optional | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with `maxValue`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_session_installment_option import CheckoutSessionInstallmentOption
from adyen.models.plan_1 import Plan1

checkout_session_installment_option = CheckoutSessionInstallmentOption(
    plans=[
        Plan1.BUYNOW_PAYLATER,
        Plan1.INTERES_REFUND_PRCTG,
        Plan1.INTEREST_BONUS
    ],
    preselected_value=228,
    values=[
        162
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

