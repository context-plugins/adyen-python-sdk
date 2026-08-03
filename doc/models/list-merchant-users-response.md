
# List Merchant Users Response

*This model accepts additional fields of type Any.*

## Structure

`ListMerchantUsersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `data` | [`List[User]`](../../doc/models/user.md) | Optional | The list of users. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.links_2 import Links2
from adyen.models.list_merchant_users_response import ListMerchantUsersResponse
from adyen.models.mself import Self
from adyen.models.name_5 import Name5
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev
from adyen.models.user import User

list_merchant_users_response = ListMerchantUsersResponse(
    items_total=196,
    pages_total=158,
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
        User(
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
            name=Name5(
                first_name='firstName4',
                last_name='lastName4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        User(
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
            name=Name5(
                first_name='firstName4',
                last_name='lastName4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        User(
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
            name=Name5(
                first_name='firstName4',
                last_name='lastName4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
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

