
# Surcharge 2

The [surcharge](https://docs.adyen.com/online-payments/surcharge/) amount to apply to the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). When you apply surcharge, include the surcharge in the `amount.value` field.

Review our [Surcharge compliance guide](https://docs.adyen.com/development-resources/surcharge-compliance/) to learn about how to comply with regulatory requirements when applying surcharge.

*This model accepts additional fields of type Any.*

## Structure

`Surcharge2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `int` | Required | The [surcharge](https://docs.adyen.com/online-payments/surcharge/) amount to apply to the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). When you apply surcharge, include the surcharge in the `amount.value` field.<br><br>Review our [Surcharge compliance guide](https://docs.adyen.com/development-resources/surcharge-compliance/) to learn about how to comply with regulatory requirements when applying surcharge. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.surcharge_2 import Surcharge2

surcharge_2 = Surcharge2(
    value=106,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

