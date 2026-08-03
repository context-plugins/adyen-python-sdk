
# List Company Users Response

*This model accepts additional fields of type Any.*

## Structure

`ListCompanyUsersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `data` | [`List[CompanyUser]`](../../doc/models/company-user.md) | Optional | The list of users. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.company_user import CompanyUser
from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.links_2 import Links2
from adyen.models.list_company_users_response import ListCompanyUsersResponse
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev

list_company_users_response = ListCompanyUsersResponse(
    items_total=20,
    pages_total=238,
    links=PaginationLinks(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        prev=Prev(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
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
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
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
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CompanyUser(
            email='email6',
            id='id0',
            roles=[
                'roles8'
            ],
            time_zone_code='timeZoneCode2',
            username='username0',
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
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
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CompanyUser(
            email='email6',
            id='id0',
            roles=[
                'roles8'
            ],
            time_zone_code='timeZoneCode2',
            username='username0',
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
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
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

