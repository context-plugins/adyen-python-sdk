
# Patchable Top Up Amount 2

The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount or a target amount.

## Structure

`PatchableTopUpAmount2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| None | Optional | This is a container for one-of cases. |
| `target` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.patchable_top_up_amount_2 import PatchableTopUpAmount2

patchable_top_up_amount_2 = PatchableTopUpAmount2(
    fixed=PatchableAmountDTO(
        currency='currency2',
        value=164
    ),
    target=PatchableAmountDTO(
        currency='currency2',
        value=164
    )
)
```

