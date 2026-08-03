
# Create Company User Request

*This model accepts additional fields of type Any.*

## Structure

`CreateCompanyUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_groups` | `List[str]` | Optional | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| `associated_merchant_accounts` | `List[str]` | Optional | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) associated with this user. |
| `email` | `str` | Required | The email address of the user. |
| `login_method` | `str` | Optional | The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before creating the user.<br><br>Possible values: **Email** or **SSO** |
| `name` | [`Name5`](../../doc/models/name-5.md) | Required | - |
| `roles` | `List[str]` | Optional | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| `time_zone_code` | `str` | Optional | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| `username` | `str` | Required | The user's email address that will be their username. Must be the same as the one in the `email` field.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_company_user_request import CreateCompanyUserRequest
from adyen.models.name_5 import Name5

create_company_user_request = CreateCompanyUserRequest(
    email='email2',
    name=Name5(
        first_name='firstName4',
        last_name='lastName4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    username='username6',
    account_groups=[
        'accountGroups5',
        'accountGroups4',
        'accountGroups3'
    ],
    associated_merchant_accounts=[
        'associatedMerchantAccounts4'
    ],
    login_method='loginMethod6',
    roles=[
        'roles2',
        'roles3',
        'roles4'
    ],
    time_zone_code='timeZoneCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

