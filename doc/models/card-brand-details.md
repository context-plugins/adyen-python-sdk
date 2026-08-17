
# Card Brand Details

## Structure

`CardBrandDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `healthcare` | `bool` | Optional | Indicates if the card supports FSA/HSA healthcare payments. |
| `supported` | `bool` | Optional | Indicates if you support the card brand. |
| `mtype` | `str` | Optional | The name of the card brand. |

## Example

```python
from adyen.models.card_brand_details import CardBrandDetails

card_brand_details = CardBrandDetails(
    healthcare=False,
    supported=False,
    mtype='type2'
)
```

