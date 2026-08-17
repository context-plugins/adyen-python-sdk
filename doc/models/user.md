
# User

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links1`](../../doc/models/links-1.md) | Optional | References to resources connected with this user. |
| `account_groups` | `List[str]` | Optional | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| `active` | `bool` | Optional | Indicates whether this user is active. |
| `apps` | `List[str]` | Optional | Set of apps available to this user |
| `email` | `str` | Required | The email address of the user. |
| `id` | `str` | Required | The unique identifier of the user. |
| `name` | [`Name`](../../doc/models/name.md) | Optional | The user's full name. |
| `roles` | `List[str]` | Required | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| `time_zone_code` | `str` | Required | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| `username` | `str` | Required | The username for this user.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |

## Example

```python
from adyen.models.links_1 import Links1
from adyen.models.links_element_6 import LinksElement6
from adyen.models.name import Name
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
    links=Links1(
        mself=LinksElement6(
            href='href0'
        )
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
    name=Name(
        first_name='firstName4',
        last_name='lastName4'
    )
)
```

