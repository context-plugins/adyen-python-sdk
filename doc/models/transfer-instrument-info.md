
# Transfer Instrument Info

## Structure

`TransferInstrumentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccountInfo1`](../../doc/models/bank-account-info-1.md) | Required | Contains information about the legal entity's bank account. |
| `legal_entity_id` | `str` | Required | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. |
| `mtype` | [`Type221Enum`](../../doc/models/type-221-enum.md) | Required | The type of transfer instrument.<br><br>Possible value: **bankAccount**. |

## Example

```python
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_info_1 import BankAccountInfo1
from adyen.models.transfer_instrument_info import TransferInstrumentInfo
from adyen.models.type_221_enum import Type221Enum

transfer_instrument_info = TransferInstrumentInfo(
    bank_account=BankAccountInfo1(
        account_identification=AULocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8'
        ),
        account_type='accountType8',
        bank_name='bankName6',
        country_code='countryCode6'
    ),
    legal_entity_id='legalEntityId2',
    mtype=Type221Enum.BANKACCOUNT
)
```

