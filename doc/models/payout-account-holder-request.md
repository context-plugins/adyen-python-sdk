
# Payout Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`PayoutAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account from which the payout is to be made. |
| `account_holder_code` | `str` | Required | The code of the Account Holder who owns the account from which the payout is to be made.<br>The Account Holder is the party to which the payout will be made. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `bank_account_uuid` | `str` | Optional | The unique ID of the Bank Account held by the Account Holder to which the payout is to be made.<br>If left blank, a bank account is automatically selected. |
| `description` | `str` | Optional | A description of the payout. Maximum 200 characters.<br>Allowed: **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,'+ ";**<br><br>**Constraints**: *Maximum Length*: `200` |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `payout_method_code` | `str` | Optional | The unique ID of the payout method held by the Account Holder to which the payout is to be made.<br>If left blank, a payout instrument is automatically selected. |
| `payout_speed` | [`PayoutSpeed`](../../doc/models/payout-speed.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.payout_account_holder_request import PayoutAccountHolderRequest

payout_account_holder_request = PayoutAccountHolderRequest(
    account_code='accountCode6',
    account_holder_code='accountHolderCode8',
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bank_account_uuid='bankAccountUUID2',
    description='description6',
    merchant_reference='merchantReference0',
    payout_method_code='payoutMethodCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

