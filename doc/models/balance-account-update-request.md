
# Balance Account Update Request

## Structure

`BalanceAccountUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
| `description` | `str` | Optional | A human-readable description of the balance account. You can use this parameter to distinguish between multiple balance accounts under an account holder.<br><br>**Constraints**: *Maximum Length*: `300` |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `platform_payment_configuration` | [`PlatformPaymentConfiguration1`](../../doc/models/platform-payment-configuration-1.md) | Optional | Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account. |
| `reference` | `str` | Optional | Your reference to the balance account.<br><br>**Constraints**: *Maximum Length*: `150` |
| `status` | [`Status43Enum`](../../doc/models/status-43-enum.md) | Optional | The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status is **active**.<br><br>Possible values: **active**, **closed**, **suspended**. |
| `time_zone` | `str` | Optional | The time zone of the balance account. For example, **Europe/Amsterdam**.<br>Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |

## Example

```python
import dateutil.parser

from adyen.models.balance_account_update_request import BalanceAccountUpdateRequest
from adyen.models.platform_payment_configuration_1 import PlatformPaymentConfiguration1

balance_account_update_request = BalanceAccountUpdateRequest(
    account_holder_id='accountHolderId0',
    description='description8',
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4',
        'key2': 'metadata3'
    },
    platform_payment_configuration=PlatformPaymentConfiguration1(
        sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        settlement_delay_days=80
    ),
    reference='reference6'
)
```

