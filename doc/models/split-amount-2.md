
# Split Amount 2

The amount of the split item.

* Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).
* Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration.

*This model accepts additional fields of type Any.*

## Structure

`SplitAmount2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `int` | Required | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.split_amount_2 import SplitAmount2

split_amount_2 = SplitAmount2(
    value=218,
    currency='currency6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

