
# Webhook Links 2

References to resources connected with this webhook.

## Structure

`WebhookLinks2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | [`LinksElement15`](../../doc/models/links-element-15.md) | Optional | The company account that the webhook is configured for. Only present for company-level webhooks. |
| `generate_hmac` | [`LinksElement16`](../../doc/models/links-element-16.md) | Required | Generate an HMAC key. |
| `merchant` | [`LinksElement17`](../../doc/models/links-element-17.md) | Optional | The merchant account that the webhook is configured for. Only present for merchant-level webhooks. |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |
| `test_webhook` | [`LinksElement19`](../../doc/models/links-element-19.md) | Required | Test the webhook setup. |

## Example

```python
from adyen.models.links_element_15 import LinksElement15
from adyen.models.links_element_16 import LinksElement16
from adyen.models.links_element_17 import LinksElement17
from adyen.models.links_element_19 import LinksElement19
from adyen.models.links_element_6 import LinksElement6
from adyen.models.webhook_links_2 import WebhookLinks2

webhook_links_2 = WebhookLinks2(
    generate_hmac=LinksElement16(
        href='href6'
    ),
    mself=LinksElement6(
        href='href0'
    ),
    test_webhook=LinksElement19(
        href='href6'
    ),
    company=LinksElement15(
        href='href2'
    ),
    merchant=LinksElement17(
        href='href6'
    )
)
```

