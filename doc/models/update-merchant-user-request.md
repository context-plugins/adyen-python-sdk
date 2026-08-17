
# Update Merchant User Request

## Structure

`UpdateMerchantUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_groups` | `List[str]` | Optional | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| `active` | `bool` | Optional | Sets the status of the user to active (**true**) or inactive (**false**). |
| `email` | `str` | Optional | The email address of the user. |
| `login_method` | `str` | Optional | The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before creating the user.<br><br>Possible values: **Email** or **SSO** |
| `name` | [`Name22`](../../doc/models/name-22.md) | Optional | The user's full name. |
| `roles` | `List[str]` | Optional | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| `time_zone_code` | `str` | Optional | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |

## Example

```python
from adyen.models.name_22 import Name22
from adyen.models.update_merchant_user_request import UpdateMerchantUserRequest

update_merchant_user_request = UpdateMerchantUserRequest(
    account_groups=[
        'accountGroups9',
        'accountGroups0'
    ],
    active=False,
    email='email6',
    login_method='loginMethod2',
    name=Name22(
        first_name='firstName4',
        last_name='lastName4'
    )
)
```

