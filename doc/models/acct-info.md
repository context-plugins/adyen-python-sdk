
# Acct Info

Additional information about the cardholder’s account provided by the 3DS Requestor.

*This model accepts additional fields of type Any.*

## Structure

`AcctInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ch_acc_age_ind` | [`ChAccAgeInd`](../../doc/models/ch-acc-age-ind.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `ch_acc_change` | `str` | Optional | Date that the cardholder’s account with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.<br>Format: **YYYYMMDD** |
| `ch_acc_change_ind` | [`ChAccChangeInd`](../../doc/models/ch-acc-change-ind.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `ch_acc_pw_change` | `str` | Optional | Date that cardholder’s account with the 3DS Requestor had a password change or account reset.<br>Format: **YYYYMMDD** |
| `ch_acc_pw_change_ind` | [`ChAccPwChangeInd`](../../doc/models/ch-acc-pw-change-ind.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `ch_acc_string` | `str` | Optional | Date that the cardholder opened the account with the 3DS Requestor.<br>Format: **YYYYMMDD** |
| `nb_purchase_account` | `str` | Optional | Number of purchases with this cardholder account during the previous six months. Max length: 4 characters. |
| `payment_acc_age` | `str` | Optional | String that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.<br>Format: **YYYYMMDD** |
| `payment_acc_ind` | [`PaymentAccInd`](../../doc/models/payment-acc-ind.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `provision_attempts_day` | `str` | Optional | Number of Add Card attempts in the last 24 hours. Max length: 3 characters. |
| `ship_address_usage` | `str` | Optional | String when the shipping address used for this transaction was first used with the 3DS Requestor.<br>Format: **YYYYMMDD** |
| `ship_address_usage_ind` | [`ShipAddressUsageInd`](../../doc/models/ship-address-usage-ind.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `ship_name_indicator` | [`ShipNameIndicator`](../../doc/models/ship-name-indicator.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `suspicious_acc_activity` | [`SuspiciousAccActivity`](../../doc/models/suspicious-acc-activity.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `txn_activity_day` | `str` | Optional | Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous 24 hours. Max length: 3 characters.<br><br>**Constraints**: *Maximum Length*: `3` |
| `txn_activity_year` | `str` | Optional | Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous year. Max length: 3 characters.<br><br>**Constraints**: *Maximum Length*: `3` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.acct_info import AcctInfo
from adyen.models.ch_acc_age_ind import ChAccAgeInd
from adyen.models.ch_acc_change_ind import ChAccChangeInd
from adyen.models.ch_acc_pw_change_ind import ChAccPwChangeInd

acct_info = AcctInfo(
    ch_acc_age_ind=ChAccAgeInd.ENUM_05,
    ch_acc_change='chAccChange8',
    ch_acc_change_ind=ChAccChangeInd.ENUM_01,
    ch_acc_pw_change='chAccPwChange2',
    ch_acc_pw_change_ind=ChAccPwChangeInd.ENUM_04,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

