
# List Nonprofits Response

## Structure

`ListNonprofitsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `items_total` | `int` | Required | Total number of items. |
| `nonprofits` | [`List[Nonprofit]`](../../doc/models/nonprofit.md) | Optional | The supported nonprofit organizations. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_nonprofits_response import ListNonprofitsResponse
from adyen.models.nonprofit import Nonprofit
from adyen.models.nonprofit_cause import NonprofitCause
from adyen.models.pagination_links_1 import PaginationLinks1

list_nonprofits_response = ListNonprofitsResponse(
    items_total=8,
    pages_total=226,
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
    nonprofits=[
        Nonprofit(
            causes=[
                NonprofitCause(
                    banner_url='bannerUrl6',
                    description='description6',
                    locales=[
                        'locales6',
                        'locales7'
                    ],
                    name='name6',
                    id='id6'
                )
            ],
            description='description8',
            goals=[
                'goals3',
                'goals4',
                'goals5'
            ],
            locales=[
                'locales8',
                'locales9'
            ],
            logo_url='logoUrl8',
            name='name8',
            regions=[
                'regions3',
                'regions4'
            ],
            terms_and_conditions_url='termsAndConditionsUrl6',
            website='website4',
            id='id8'
        )
    ]
)
```

