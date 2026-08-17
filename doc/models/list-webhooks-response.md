
# List Webhooks Response

## Structure

`ListWebhooksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `account_reference` | `str` | Optional | Reference to the account. |
| `data` | [`List[Webhook]`](../../doc/models/webhook.md) | Optional | The list of webhooks configured for this account. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.communication_format_enum import CommunicationFormatEnum
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_15 import LinksElement15
from adyen.models.links_element_16 import LinksElement16
from adyen.models.links_element_17 import LinksElement17
from adyen.models.links_element_19 import LinksElement19
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_webhooks_response import ListWebhooksResponse
from adyen.models.pagination_links_1 import PaginationLinks1
from adyen.models.webhook import Webhook
from adyen.models.webhook_links_2 import WebhookLinks2

list_webhooks_response = ListWebhooksResponse(
    items_total=198,
    pages_total=160,
    links=PaginationLinks1(
        first=LinksElement9(
            href='href2'
        ),
        last=LinksElement10(
            href='href2'
        ),
        mself=LinksElement13(
            href='href0'
        ),
        next=LinksElement11(
            href='href4'
        ),
        prev=LinksElement12(
            href='href8'
        )
    ),
    account_reference='accountReference6',
    data=[
        Webhook(
            active=False,
            communication_format=CommunicationFormatEnum.JSON,
            mtype='type0',
            url='url4',
            links=WebhookLinks2(
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
            ),
            accepts_expired_certificate=False,
            accepts_self_signed_certificate=False,
            accepts_untrusted_root_certificate=False,
            account_reference='accountReference2'
        ),
        Webhook(
            active=False,
            communication_format=CommunicationFormatEnum.JSON,
            mtype='type0',
            url='url4',
            links=WebhookLinks2(
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
            ),
            accepts_expired_certificate=False,
            accepts_self_signed_certificate=False,
            accepts_untrusted_root_certificate=False,
            account_reference='accountReference2'
        )
    ]
)
```

