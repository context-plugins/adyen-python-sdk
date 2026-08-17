
# List Merchant Response

## Structure

`ListMerchantResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[Merchant]`](../../doc/models/merchant.md) | Optional | The list of merchant accounts. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.data_center import DataCenter
from adyen.models.links_element import LinksElement
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_merchant_response import ListMerchantResponse
from adyen.models.merchant import Merchant
from adyen.models.merchant_links_2 import MerchantLinks2
from adyen.models.pagination_links_1 import PaginationLinks1

list_merchant_response = ListMerchantResponse(
    items_total=8,
    pages_total=30,
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
    data=[
        Merchant(
            links=MerchantLinks2(
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
            ),
            capture_delay='captureDelay6',
            company_id='companyId0',
            data_centers=[
                DataCenter(
                    live_prefix='livePrefix4',
                    name='name6'
                ),
                DataCenter(
                    live_prefix='livePrefix4',
                    name='name6'
                ),
                DataCenter(
                    live_prefix='livePrefix4',
                    name='name6'
                )
            ],
            default_shopper_interaction='defaultShopperInteraction8'
        )
    ]
)
```

