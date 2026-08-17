
# List Company Response

## Structure

`ListCompanyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[Company2]`](../../doc/models/company-2.md) | Optional | The list of companies. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.company_2 import Company2
from adyen.models.company_links_2 import CompanyLinks2
from adyen.models.data_center import DataCenter
from adyen.models.links_element import LinksElement
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_company_response import ListCompanyResponse
from adyen.models.pagination_links_1 import PaginationLinks1

list_company_response = ListCompanyResponse(
    items_total=20,
    pages_total=18,
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
        Company2(
            links=CompanyLinks2(
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
            description='description0',
            id='id0',
            name='name0'
        ),
        Company2(
            links=CompanyLinks2(
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
            description='description0',
            id='id0',
            name='name0'
        ),
        Company2(
            links=CompanyLinks2(
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
            description='description0',
            id='id0',
            name='name0'
        )
    ]
)
```

