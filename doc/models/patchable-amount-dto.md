
# Patchable Amount DTO

Required if `type` is **business**, **assetSale**, **gamblingWinnings** or **inheritance**.

For `type` **business**, provide the annual turn over of the business. For `type` **assetSale**, **gamblingWinnings** or **inheritance**, provide the amount of the funds., The amount of the funds the financier provided., The maximum amount a card holder can withdraw per day.

## Structure

`PatchableAmountDTO`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `int` | Optional | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |

## Example

```python
from adyen.models.patchable_amount_dto import PatchableAmountDTO

patchable_amount_dto = PatchableAmountDTO(
    currency='currency0',
    value=6
)
```

