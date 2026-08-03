
# Counterparty 11

The recipient of the funds transfer. A bank account or a transfer instrument.

*This model accepts additional fields of type Any.*

## Structure

`Counterparty11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | - |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account import BankAccount
from adyen.models.counterparty_11 import Counterparty11
from adyen.models.type_413 import Type413

counterparty_11 = Counterparty11(
    bank_account=BankAccount(
        account_identification=AuLocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8',
            mtype=Type413.AULOCAL,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    transfer_instrument_id='transferInstrumentId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

