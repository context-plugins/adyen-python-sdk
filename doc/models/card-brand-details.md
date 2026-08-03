
# Card Brand Details

*This model accepts additional fields of type Any.*

## Structure

`CardBrandDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `healthcare` | `bool` | Optional | Indicates if the card supports FSA/HSA healthcare payments. |
| `supported` | `bool` | Optional | Indicates if you support the card brand. |
| `mtype` | `str` | Optional | The name of the card brand. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_brand_details import CardBrandDetails

card_brand_details = CardBrandDetails(
    healthcare=False,
    supported=False,
    mtype='type2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

