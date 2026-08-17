
# Account

## Structure

`Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account. |
| `bank_account_uuid` | `str` | Optional | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |
| `beneficiary_account` | `str` | Optional | The beneficiary of the account. |
| `beneficiary_merchant_reference` | `str` | Optional | The reason that a beneficiary has been set up for this account. This may have been supplied during the setup of a beneficiary at the discretion of the executing user. |
| `description` | `str` | Optional | A description of the account. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use by the merchant.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `payout_method_code` | `str` | Optional | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |
| `payout_schedule` | [`PayoutScheduleResponse4`](../../doc/models/payout-schedule-response-4.md) | Optional | The account's payout schedule. |
| `payout_speed` | [`PayoutSpeedEnum`](../../doc/models/payout-speed-enum.md) | Optional | Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`. |
| `status` | `str` | Optional | The status of the account. Possible values: `Active`, `Inactive`, `Suspended`, `Closed`. |

## Example

```python
from adyen.models.account import Account

account = Account(
    account_code='accountCode0',
    bank_account_uuid='bankAccountUUID6',
    beneficiary_account='beneficiaryAccount2',
    beneficiary_merchant_reference='beneficiaryMerchantReference2',
    description='description0'
)
```

