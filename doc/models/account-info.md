
# Account Info

Shopper account information for 3D Secure 2.

> For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.

## Structure

`AccountInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_age_indicator` | [`AccountAgeIndicatorEnum`](../../doc/models/account-age-indicator-enum.md) | Optional | Indicator for the length of time since this shopper account was created in the merchant's environment.<br>Allowed values:<br><br>* notApplicable<br>* thisTransaction<br>* lessThan30Days<br>* from30To60Days<br>* moreThan60Days |
| `account_change_date` | `datetime` | Optional | Date when the shopper's account was last changed. |
| `account_change_indicator` | [`AccountChangeIndicatorEnum`](../../doc/models/account-change-indicator-enum.md) | Optional | Indicator for the length of time since the shopper's account was last updated.<br>Allowed values:<br><br>* thisTransaction<br>* lessThan30Days<br>* from30To60Days<br>* moreThan60Days |
| `account_creation_date` | `datetime` | Optional | Date when the shopper's account was created. |
| `account_type` | [`AccountTypeEnum`](../../doc/models/account-type-enum.md) | Optional | Indicates the type of account. For example, for a multi-account card product.<br>Allowed values:<br><br>* notApplicable<br>* credit<br>* debit |
| `add_card_attempts_day` | `int` | Optional | Number of attempts the shopper tried to add a card to their account in the last day. |
| `delivery_address_usage_date` | `datetime` | Optional | Date the selected delivery address was first used. |
| `delivery_address_usage_indicator` | [`DeliveryAddressUsageIndicatorEnum`](../../doc/models/delivery-address-usage-indicator-enum.md) | Optional | Indicator for the length of time since this delivery address was first used.<br>Allowed values:<br><br>* thisTransaction<br>* lessThan30Days<br>* from30To60Days<br>* moreThan60Days |
| `home_phone` | `str` | Optional | Shopper's home phone number (including the country code). |
| `mobile_phone` | `str` | Optional | Shopper's mobile phone number (including the country code). |
| `password_change_date` | `datetime` | Optional | Date when the shopper last changed their password. |
| `password_change_indicator` | [`PasswordChangeIndicatorEnum`](../../doc/models/password-change-indicator-enum.md) | Optional | Indicator when the shopper has changed their password.<br>Allowed values:<br><br>* notApplicable<br>* thisTransaction<br>* lessThan30Days<br>* from30To60Days<br>* moreThan60Days |
| `past_transactions_day` | `int` | Optional | Number of all transactions (successful and abandoned) from this shopper in the past 24 hours. |
| `past_transactions_year` | `int` | Optional | Number of all transactions (successful and abandoned) from this shopper in the past year. |
| `payment_account_age` | `datetime` | Optional | Date this payment method was added to the shopper's account. |
| `payment_account_indicator` | [`PaymentAccountIndicatorEnum`](../../doc/models/payment-account-indicator-enum.md) | Optional | Indicator for the length of time since this payment method was added to this shopper's account.<br>Allowed values:<br><br>* notApplicable<br>* thisTransaction<br>* lessThan30Days<br>* from30To60Days<br>* moreThan60Days |
| `purchases_last_6_months` | `int` | Optional | Number of successful purchases in the last six months. |
| `suspicious_activity` | `bool` | Optional | Whether suspicious activity was recorded on this account. |
| `work_phone` | `str` | Optional | Shopper's work phone number (including the country code). |

## Example

```python
import dateutil.parser

from adyen.models.account_age_indicator_enum import AccountAgeIndicatorEnum
from adyen.models.account_change_indicator_enum import AccountChangeIndicatorEnum
from adyen.models.account_info import AccountInfo
from adyen.models.account_type_enum import AccountTypeEnum

account_info = AccountInfo(
    account_age_indicator=AccountAgeIndicatorEnum.FROM30TO60DAYS,
    account_change_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account_change_indicator=AccountChangeIndicatorEnum.THISTRANSACTION,
    account_creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    account_type=AccountTypeEnum.CREDIT
)
```

