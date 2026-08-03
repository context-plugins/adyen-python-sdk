
# Patchable Amount Dto

Required if `type` is **business**, **assetSale**, **gamblingWinnings** or **inheritance**.

For `type` **business**, provide the annual turn over of the business. For `type` **assetSale**, **gamblingWinnings** or **inheritance**, provide the amount of the funds.

*This model accepts additional fields of type Any.*

## Structure

`PatchableAmountDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `int` | Optional | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_amount_dto import PatchableAmountDto

patchable_amount_dto = PatchableAmountDto(
    currency='currency0',
    value=6,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

