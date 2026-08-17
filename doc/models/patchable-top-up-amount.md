
# Patchable Top Up Amount

## Structure

`PatchableTopUpAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| None | Optional | This is a container for one-of cases. |
| `target` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.patchable_top_up_amount import PatchableTopUpAmount

patchable_top_up_amount = PatchableTopUpAmount(
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

