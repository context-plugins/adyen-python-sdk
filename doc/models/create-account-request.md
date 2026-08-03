
# Create Account Request

*This model accepts additional fields of type Any.*

## Structure

`CreateAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of Account Holder under which to create the account. |
| `bank_account_uuid` | `str` | Optional | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |
| `description` | `str` | Optional | A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use by the merchant.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `payout_method_code` | `str` | Optional | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |
| `payout_schedule` | [`PayoutSchedule`](../../doc/models/payout-schedule.md) | Optional | - |
| `payout_schedule_reason` | `str` | Optional | The reason for the payout schedule choice.<br><br>> This field is required when the `payoutSchedule` parameter is set to `HOLD`. |
| `payout_speed` | [`PayoutSpeed1`](../../doc/models/payout-speed-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_account_request import CreateAccountRequest
from adyen.models.payout_schedule import PayoutSchedule

create_account_request = CreateAccountRequest(
    account_holder_code='accountHolderCode0',
    bank_account_uuid='bankAccountUUID0',
    description='description6',
    metadata={
        'key0': 'metadata9'
    },
    payout_method_code='payoutMethodCode6',
    payout_schedule=PayoutSchedule.WEEKLY_SUN_TO_THU_AU,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

