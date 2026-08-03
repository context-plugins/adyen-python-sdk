
# Update Company User Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateCompanyUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_groups` | `List[str]` | Optional | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| `active` | `bool` | Optional | Indicates whether this user is active. |
| `associated_merchant_accounts` | `List[str]` | Optional | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) to associate the user with. |
| `email` | `str` | Optional | The email address of the user. |
| `login_method` | `str` | Optional | The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before creating the user.<br><br>Possible values: **Email** or **SSO** |
| `name` | [`Name22`](../../doc/models/name-22.md) | Optional | - |
| `roles` | `List[str]` | Optional | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| `time_zone_code` | `str` | Optional | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.update_company_user_request import UpdateCompanyUserRequest

update_company_user_request = UpdateCompanyUserRequest(
    account_groups=[
        'accountGroups9'
    ],
    active=False,
    associated_merchant_accounts=[
        'associatedMerchantAccounts8',
        'associatedMerchantAccounts9',
        'associatedMerchantAccounts0'
    ],
    email='email8',
    login_method='loginMethod0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

