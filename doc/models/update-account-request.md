
# Update Account Request

## Structure

`UpdateAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account to update. |
| `bank_account_uuid` | `str` | Optional | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |
| `description` | `str` | Optional | A description of the account, maximum 256 characters.You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use by the merchant.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `payout_method_code` | `str` | Optional | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |
| `payout_schedule` | [`UpdatePayoutScheduleRequest2`](../../doc/models/update-payout-schedule-request-2.md) | Optional | The details of the payout schedule to which the account must be updated. |
| `payout_speed` | [`PayoutSpeed1Enum`](../../doc/models/payout-speed-1-enum.md) | Optional | Speed at which payouts for this account are processed.<br><br>Possible values: `STANDARD` (default), `SAME_DAY`. |

## Example

```python
from adyen.models.action_enum import ActionEnum
from adyen.models.schedule_1_enum import Schedule1Enum
from adyen.models.update_account_request import UpdateAccountRequest
from adyen.models.update_payout_schedule_request_2 import UpdatePayoutScheduleRequest2

update_account_request = UpdateAccountRequest(
    account_code='accountCode0',
    bank_account_uuid='bankAccountUUID6',
    description='description0',
    metadata={
        'key0': 'metadata3'
    },
    payout_method_code='payoutMethodCode0',
    payout_schedule=UpdatePayoutScheduleRequest2(
        schedule=Schedule1Enum.WEEKLY_ON_TUE_FRI_MIDNIGHT,
        action=ActionEnum.NOTHING,
        reason='reason0'
    )
)
```

