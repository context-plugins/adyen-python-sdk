
# Merchant Links 2

References to resources connected with this merchant.

## Structure

`MerchantLinks2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_credentials` | [`LinksElement`](../../doc/models/links-element.md) | Optional | - |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |
| `users` | [`LinksElement`](../../doc/models/links-element.md) | Optional | - |
| `webhooks` | [`LinksElement`](../../doc/models/links-element.md) | Optional | - |

## Example

```python
from adyen.models.links_element import LinksElement
from adyen.models.links_element_6 import LinksElement6
from adyen.models.merchant_links_2 import MerchantLinks2

merchant_links_2 = MerchantLinks2(
    mself=LinksElement6(
        href='href0'
    ),
    api_credentials=LinksElement(
        href='href8'
    ),
    users=LinksElement(
        href='href8'
    ),
    webhooks=LinksElement(
        href='href8'
    )
)
```

