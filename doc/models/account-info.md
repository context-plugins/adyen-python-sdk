
# Account Info

*This model accepts additional fields of type Any.*

## Structure

`AccountInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_age_indicator` | [`AccountAgeIndicator`](../../doc/models/account-age-indicator.md) | Optional | - |
| `account_change_date` | `datetime` | Optional | Date when the shopper's account was last changed. |
| `account_change_indicator` | [`AccountChangeIndicator`](../../doc/models/account-change-indicator.md) | Optional | - |
| `account_creation_date` | `datetime` | Optional | Date when the shopper's account was created. |
| `account_type` | [`AccountType1`](../../doc/models/account-type-1.md) | Optional | - |
| `add_card_attempts_day` | `int` | Optional | Number of attempts the shopper tried to add a card to their account in the last day. |
| `delivery_address_usage_date` | `datetime` | Optional | Date the selected delivery address was first used. |
| `delivery_address_usage_indicator` | [`DeliveryAddressUsageIndicator`](../../doc/models/delivery-address-usage-indicator.md) | Optional | - |
| `home_phone` | `str` | Optional | Shopper's home phone number (including the country code). |
| `mobile_phone` | `str` | Optional | Shopper's mobile phone number (including the country code). |
| `password_change_date` | `datetime` | Optional | Date when the shopper last changed their password. |
| `password_change_indicator` | [`PasswordChangeIndicator`](../../doc/models/password-change-indicator.md) | Optional | - |
| `past_transactions_day` | `int` | Optional | Number of all transactions (successful and abandoned) from this shopper in the past 24 hours. |
| `past_transactions_year` | `int` | Optional | Number of all transactions (successful and abandoned) from this shopper in the past year. |
| `payment_account_age` | `datetime` | Optional | Date this payment method was added to the shopper's account. |
| `payment_account_indicator` | [`PaymentAccountIndicator`](../../doc/models/payment-account-indicator.md) | Optional | - |
| `purchases_last_6_months` | `int` | Optional | Number of successful purchases in the last six months. |
| `suspicious_activity` | `bool` | Optional | Whether suspicious activity was recorded on this account. |
| `work_phone` | `str` | Optional | Shopper's work phone number (including the country code). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_age_indicator import AccountAgeIndicator
from adyen.models.account_change_indicator import AccountChangeIndicator
from adyen.models.account_info import AccountInfo
from adyen.models.account_type_1 import AccountType1

account_info = AccountInfo(
    account_age_indicator=AccountAgeIndicator.FROM30TO60DAYS,
    account_change_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account_change_indicator=AccountChangeIndicator.THISTRANSACTION,
    account_creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account_type=AccountType1.CREDIT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

