
# Debit Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`DebitAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `bank_account_uuid` | `str` | Required | The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account. |
| `description` | `str` | Optional | A description of the direct debit. Maximum length: 35 characters.<br><br>Allowed characters: **a-z**, **A-Z**, **0-9**, and special characters **/?:().,'+ ";**.<br><br>**Constraints**: *Maximum Length*: `35` |
| `merchant_account` | `str` | Required | Your merchant account. |
| `splits` | [`List[Split1]`](../../doc/models/split-1.md) | Required | Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.amount_31 import Amount31
from adyen.models.debit_account_holder_request import DebitAccountHolderRequest
from adyen.models.split_1 import Split1
from adyen.models.type_15 import Type15

debit_account_holder_request = DebitAccountHolderRequest(
    account_holder_code='accountHolderCode2',
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bank_account_uuid='bankAccountUUID2',
    merchant_account='merchantAccount8',
    splits=[
        Split1(
            mtype=Type15.TIP,
            account='account2',
            amount=Amount31(
                value=110,
                currency='currency2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description2',
            reference='reference2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    description='description6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

