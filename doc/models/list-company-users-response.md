
# List Company Users Response

## Structure

`ListCompanyUsersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[CompanyUser]`](../../doc/models/company-user.md) | Optional | The list of users. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.company_user import CompanyUser
from adyen.models.links_1 import Links1
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_company_users_response import ListCompanyUsersResponse
from adyen.models.pagination_links_1 import PaginationLinks1

list_company_users_response = ListCompanyUsersResponse(
    items_total=20,
    pages_total=238,
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
        CompanyUser(
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
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ]
        ),
        CompanyUser(
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
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ]
        ),
        CompanyUser(
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
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ]
        )
    ]
)
```

