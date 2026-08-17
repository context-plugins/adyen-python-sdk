
# Split Amount

The amount of the split item.

* Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).

* Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration., The amount of the split item.

* Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).

* Required if `type` is **BalanceAccount**, **Commission**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration.

## Structure

`SplitAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `int` | Required | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |

## Example

```python
from adyen.models.split_amount import SplitAmount

split_amount = SplitAmount(
    value=188,
    currency='currency8'
)
```

