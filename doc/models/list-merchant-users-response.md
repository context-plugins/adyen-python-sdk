
# List Merchant Users Response

## Structure

`ListMerchantUsersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[User]`](../../doc/models/user.md) | Optional | The list of users. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.links_1 import Links1
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_merchant_users_response import ListMerchantUsersResponse
from adyen.models.name import Name
from adyen.models.pagination_links_1 import PaginationLinks1
from adyen.models.user import User

list_merchant_users_response = ListMerchantUsersResponse(
    items_total=196,
    pages_total=158,
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
        User(
            email='email6',
            id='id0',
            roles=[
                'roles8'
            ],
            time_zone_code='timeZoneCode2',
            username='username0',
            links=Links1(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            account_groups=[
                'accountGroups7'
            ],
            active=False,
            apps=[
                'apps4',
                'apps5',
                'apps6'
            ],
            name=Name(
                first_name='firstName4',
                last_name='lastName4'
            )
        ),
        User(
            email='email6',
            id='id0',
            roles=[
                'roles8'
            ],
            time_zone_code='timeZoneCode2',
            username='username0',
            links=Links1(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            account_groups=[
                'accountGroups7'
            ],
            active=False,
            apps=[
                'apps4',
                'apps5',
                'apps6'
            ],
            name=Name(
                first_name='firstName4',
                last_name='lastName4'
            )
        ),
        User(
            email='email6',
            id='id0',
            roles=[
                'roles8'
            ],
            time_zone_code='timeZoneCode2',
            username='username0',
            links=Links1(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            account_groups=[
                'accountGroups7'
            ],
            active=False,
            apps=[
                'apps4',
                'apps5',
                'apps6'
            ],
            name=Name(
                first_name='firstName4',
                last_name='lastName4'
            )
        )
    ]
)
```

