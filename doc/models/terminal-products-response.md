
# Terminal Products Response

## Structure

`TerminalProductsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TerminalProduct]`](../../doc/models/terminal-product.md) | Optional | Terminal products that can be ordered. |

## Example

```python
from adyen.models.terminal_product import TerminalProduct
from adyen.models.terminal_product_price_2 import TerminalProductPrice2
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
            price=TerminalProductPrice2(
                currency='currency2',
                value=203.04
            )
        )
    ]
)
```

