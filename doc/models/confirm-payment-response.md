
# Confirm Payment Response

## Structure

`ConfirmPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links11`](../../doc/models/links-11.md) | Required | Contains redirection URLs to guide the user to the appropriate page, after a successful payment or a cancellation. |

## Example

```python
from adyen.models.confirm_payment_response import ConfirmPaymentResponse
from adyen.models.href_1 import Href1
from adyen.models.href_6 import Href6
from adyen.models.links_11 import Links11

confirm_payment_response = ConfirmPaymentResponse(
    links=Links11(
        cancel=Href6(
            href='href4'
        ),
        success=Href1(
            href='href2'
        )
    )
)
```

