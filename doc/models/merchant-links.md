
# Merchant Links

## Structure

`MerchantLinks`

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
from adyen.models.merchant_links import MerchantLinks

merchant_links = MerchantLinks(
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

