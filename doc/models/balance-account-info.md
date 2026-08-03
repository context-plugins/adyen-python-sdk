
# Balance Account Info

*This model accepts additional fields of type Any.*

## Structure

`BalanceAccountInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
| `default_currency_code` | `str` | Optional | The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area.<br>The default value is **EUR**.<br><br>> After a balance account is created, you cannot change its default currency. |
| `description` | `str` | Optional | A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.<br><br>**Constraints**: *Maximum Length*: `300` |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `migrated_account_code` | `str` | Optional, Read-only | The unique identifier of the account of the migrated account holder in the classic integration. |
| `platform_payment_configuration` | [`PlatformPaymentConfiguration`](../../doc/models/platform-payment-configuration.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the balance account, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `time_zone` | `str` | Optional | The time zone of the balance account. For example, **Europe/Amsterdam**.<br>Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.balance_account_info import BalanceAccountInfo
from adyen.models.platform_payment_configuration import PlatformPaymentConfiguration

balance_account_info = BalanceAccountInfo(
    account_holder_id='accountHolderId6',
    default_currency_code='defaultCurrencyCode6',
    description='description4',
    metadata={
        'key0': 'metadata1',
        'key1': 'metadata0'
    },
    migrated_account_code='migratedAccountCode8',
    platform_payment_configuration=PlatformPaymentConfiguration(
        sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        settlement_delay_days=80,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

