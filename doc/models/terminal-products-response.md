
# Terminal Products Response

*This model accepts additional fields of type Any.*

## Structure

`TerminalProductsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TerminalProduct]`](../../doc/models/terminal-product.md) | Optional | Terminal products that can be ordered. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_product import TerminalProduct
from adyen.models.terminal_product_price import TerminalProductPrice
from adyen.models.terminal_products_response import TerminalProductsResponse

terminal_products_response = TerminalProductsResponse(
    data=[
        TerminalProduct(
            description='description0',
            id='id0',
            items_included=[
                'itemsIncluded3',
                'itemsIncluded4',
                'itemsIncluded5'
            ],
            name='name0',
            price=TerminalProductPrice(
                currency='currency2',
                value=203.04,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

