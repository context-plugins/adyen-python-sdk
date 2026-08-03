
# User

*This model accepts additional fields of type Any.*

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links2`](../../doc/models/links-2.md) | Optional | - |
| `account_groups` | `List[str]` | Optional | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| `active` | `bool` | Optional | Indicates whether this user is active. |
| `apps` | `List[str]` | Optional | Set of apps available to this user |
| `email` | `str` | Required | The email address of the user. |
| `id` | `str` | Required | The unique identifier of the user. |
| `name` | [`Name5`](../../doc/models/name-5.md) | Optional | - |
| `roles` | `List[str]` | Required | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| `time_zone_code` | `str` | Required | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| `username` | `str` | Required | The username for this user.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.links_2 import Links2
from adyen.models.mself import Self
from adyen.models.name_5 import Name5
from adyen.models.user import User

user = User(
    email='email6',
    id='id0',
    roles=[
        'roles6',
        'roles7'
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
        'accountGroups9',
        'accountGroups0'
    ],
    active=False,
    apps=[
        'apps4',
        'apps5'
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
```

