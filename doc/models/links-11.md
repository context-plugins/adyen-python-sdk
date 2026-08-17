
# Links 11

Contains redirection URLs to guide the user to the appropriate page, after a successful payment or a cancellation.

## Structure

`Links11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cancel` | [`Href6`](../../doc/models/href-6.md) | Optional | The URL to where the user must be redirected after a payment has been canceled. |
| `success` | [`Href1`](../../doc/models/href-1.md) | Optional | The URL to where the user must be redirected after a successful payment. |

## Example

```python
from adyen.models.href_1 import Href1
from adyen.models.href_6 import Href6
from adyen.models.links_11 import Links11

links_11 = Links11(
    cancel=Href6(
        href='href4'
    ),
    success=Href1(
        href='href2'
    )
)
```

