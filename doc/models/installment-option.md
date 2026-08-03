
# Installment Option

*This model accepts additional fields of type Any.*

## Structure

`InstallmentOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_value` | `int` | Optional | The maximum number of installments offered for this payment method. |
| `plans` | [`List[Plan1]`](../../doc/models/plan-1.md) | Optional | Defines the type of installment plan. If not set, defaults to **regular**.<br><br>Possible values:<br><br>* **regular**<br>* **revolving** |
| `preselected_value` | `int` | Optional | Preselected number of installments offered for this payment method. |
| `values` | `List[int]` | Optional | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with `maxValue`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.installment_option import InstallmentOption
from adyen.models.plan_1 import Plan1

installment_option = InstallmentOption(
    max_value=124,
    plans=[
        Plan1.INTEREST_BONUS,
        Plan1.NOINTERES_REFUND_PRCTG
    ],
    preselected_value=224,
    values=[
        158,
        157
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

