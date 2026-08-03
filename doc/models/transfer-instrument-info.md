
# Transfer Instrument Info

*This model accepts additional fields of type Any.*

## Structure

`TransferInstrumentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccountInfo`](../../doc/models/bank-account-info.md) | Required | - |
| `legal_entity_id` | `str` | Required | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. |
| `mtype` | [`Type222`](../../doc/models/type-222.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account_info import BankAccountInfo
from adyen.models.transfer_instrument_info import TransferInstrumentInfo
from adyen.models.type_222 import Type222
from adyen.models.type_413 import Type413

transfer_instrument_info = TransferInstrumentInfo(
    bank_account=BankAccountInfo(
        account_identification=AuLocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8',
            mtype=Type413.AULOCAL,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        account_type='accountType8',
        bank_name='bankName6',
        country_code='countryCode6',
        trusted_source=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    legal_entity_id='legalEntityId2',
    mtype=Type222.BANKACCOUNT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

