
# Installment Option

## Structure

`InstallmentOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_value` | `int` | Optional | The maximum number of installments offered for this payment method. |
| `plans` | [`List[Plan1Enum]`](../../doc/models/plan-1-enum.md) | Optional | Defines the type of installment plan. If not set, defaults to **regular**.<br><br>Possible values:<br><br>* **regular**<br>* **revolving** |
| `preselected_value` | `int` | Optional | Preselected number of installments offered for this payment method. |
| `values` | `List[int]` | Optional | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with `maxValue`. |

## Example

```python
from adyen.models.installment_option import InstallmentOption
from adyen.models.plan_1_enum import Plan1Enum

installment_option = InstallmentOption(
    max_value=124,
    plans=[
        Plan1Enum.INTEREST_BONUS,
        Plan1Enum.NOINTERES_REFUND_PRCTG
    ],
    preselected_value=224,
    values=[
        158,
        157
    ]
)
```

