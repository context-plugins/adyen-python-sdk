
# Balance Account Update Request

*This model accepts additional fields of type Any.*

## Structure

`BalanceAccountUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
| `description` | `str` | Optional | A human-readable description of the balance account. You can use this parameter to distinguish between multiple balance accounts under an account holder.<br><br>**Constraints**: *Maximum Length*: `300` |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `platform_payment_configuration` | [`PlatformPaymentConfiguration`](../../doc/models/platform-payment-configuration.md) | Optional | - |
| `reference` | `str` | Optional | Your reference to the balance account.<br><br>**Constraints**: *Maximum Length*: `150` |
| `status` | [`Status41`](../../doc/models/status-41.md) | Optional | - |
| `time_zone` | `str` | Optional | The time zone of the balance account. For example, **Europe/Amsterdam**.<br>Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.balance_account_update_request import BalanceAccountUpdateRequest
from adyen.models.platform_payment_configuration import PlatformPaymentConfiguration

balance_account_update_request = BalanceAccountUpdateRequest(
    account_holder_id='accountHolderId0',
    description='description8',
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4',
        'key2': 'metadata3'
    },
    platform_payment_configuration=PlatformPaymentConfiguration(
        sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        settlement_delay_days=80,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

