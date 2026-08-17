
# List Stores Response

## Structure

`ListStoresResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[Store]`](../../doc/models/store.md) | Optional | List of stores |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.links_7 import Links7
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_stores_response import ListStoresResponse
from adyen.models.pagination_links_1 import PaginationLinks1
from adyen.models.store import Store
from adyen.models.store_location_1 import StoreLocation1

list_stores_response = ListStoresResponse(
    items_total=112,
    pages_total=182,
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
        Store(
            links=Links7(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            address=StoreLocation1(
                country='country0',
                city='city6',
                line_1='line18',
                line_2='line20',
                line_3='line38',
                postal_code='postalCode8'
            ),
            business_line_ids=[
                'businessLineIds4'
            ],
            description='description0',
            external_reference_id='externalReferenceId8'
        )
    ]
)
```

