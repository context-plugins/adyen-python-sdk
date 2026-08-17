
# Payout Account Holder Request

## Structure

`PayoutAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account from which the payout is to be made. |
| `account_holder_code` | `str` | Required | The code of the Account Holder who owns the account from which the payout is to be made.<br>The Account Holder is the party to which the payout will be made. |
| `amount` | [`Amount`](../../doc/models/amount.md) | Optional | An object containing the currency and value of the payout.<br>If the account has multiple currencies, specify the currency to be used.<br>If the `bankAccountUUID` is provided in the request, the currency supported by the bank is used.<br>If the `payoutMethodCode` is provided in the request, the specified payout method is selected. |
| `bank_account_uuid` | `str` | Optional | The unique ID of the Bank Account held by the Account Holder to which the payout is to be made.<br>If left blank, a bank account is automatically selected. |
| `description` | `str` | Optional | A description of the payout. Maximum 200 characters.<br>Allowed: **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,'+ ";**<br><br>**Constraints**: *Maximum Length*: `200` |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `payout_method_code` | `str` | Optional | The unique ID of the payout method held by the Account Holder to which the payout is to be made.<br>If left blank, a payout instrument is automatically selected. |
| `payout_speed` | [`PayoutSpeedEnum`](../../doc/models/payout-speed-enum.md) | Optional | Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.<br><br>**Default**: `"STANDARD"` |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.payout_account_holder_request import PayoutAccountHolderRequest
from adyen.models.payout_speed_enum import PayoutSpeedEnum

payout_account_holder_request = PayoutAccountHolderRequest(
    account_code='accountCode6',
    account_holder_code='accountHolderCode8',
    amount=Amount(
        currency='currency2',
        value=110
    ),
    bank_account_uuid='bankAccountUUID2',
    description='description6',
    merchant_reference='merchantReference0',
    payout_method_code='payoutMethodCode4',
    payout_speed=PayoutSpeedEnum.STANDARD
)
```

