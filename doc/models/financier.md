
# Financier

## Structure

`Financier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`PatchableAmountDTO`](../../doc/models/patchable-amount-dto.md) | Required | The amount of the funds the financier provided. |
| `first_name` | `str` | Required | The financier's first name. |
| `last_name` | `str` | Required | The financier's last name. |
| `location` | `str` | Required | The city and country/region where the financier is currently located. For example: Chicago, USA |

## Example

```python
from adyen.models.financier import Financier
from adyen.models.patchable_amount_dto import PatchableAmountDTO

financier = Financier(
    amount=PatchableAmountDTO(
        currency='currency2',
        value=110
    ),
    first_name='firstName0',
    last_name='lastName8',
    location='location8'
)
```

