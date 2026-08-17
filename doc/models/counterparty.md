
# Counterparty

## Structure

`Counterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccount11`](../../doc/models/bank-account-11.md) | Optional | Contains information about the bank account. |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). |

## Example

```python
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_11 import BankAccount11
from adyen.models.counterparty import Counterparty

counterparty = Counterparty(
    bank_account=BankAccount11(
        account_identification=AULocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8'
        )
    ),
    transfer_instrument_id='transferInstrumentId4'
)
```

