
# Debit Account Holder Request

## Structure

`DebitAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount to be debited from the account holder's bank account. |
| `bank_account_uuid` | `str` | Required | The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account. |
| `description` | `str` | Optional | A description of the direct debit. Maximum length: 35 characters.<br><br>Allowed characters: **a-z**, **A-Z**, **0-9**, and special characters **/?:().,'+ ";**.<br><br>**Constraints**: *Maximum Length*: `35` |
| `merchant_account` | `str` | Required | Your merchant account. |
| `splits` | [`List[Split1]`](../../doc/models/split-1.md) | Required | Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.debit_account_holder_request import DebitAccountHolderRequest
from adyen.models.split_1 import Split1
from adyen.models.split_amount import SplitAmount
from adyen.models.type_60_enum import Type60Enum

debit_account_holder_request = DebitAccountHolderRequest(
    account_holder_code='accountHolderCode2',
    amount=Amount(
        currency='currency2',
        value=110
    ),
    bank_account_uuid='bankAccountUUID2',
    merchant_account='merchantAccount8',
    splits=[
        Split1(
            mtype=Type60Enum.TIP,
            account='account2',
            amount=SplitAmount(
                value=110,
                currency='currency2'
            ),
            description='description2',
            reference='reference2'
        )
    ],
    description='description6'
)
```

