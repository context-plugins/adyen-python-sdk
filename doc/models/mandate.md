
# Mandate

*This model accepts additional fields of type Any.*

## Structure

`Mandate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account linked to the payment instrument. |
| `counterparty` | [`MandateBankAccount`](../../doc/models/mandate-bank-account.md) | Optional | - |
| `created_at` | `datetime` | Optional | The date when the mandate was created. |
| `id` | `str` | Optional | The unique identifier of the mandate. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument linked to the mandate. |
| `status` | [`MandateStatus2`](../../doc/models/mandate-status-2.md) | Optional | - |
| `mtype` | [`MandateType2`](../../doc/models/mandate-type-2.md) | Optional | - |
| `updated_at` | `datetime` | Optional | The date when the mandate was updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.mandate import Mandate
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account import MandateBankAccount
from adyen.models.mandate_party_identification import MandatePartyIdentification

mandate = Mandate(
    balance_account_id='balanceAccountId2',
    counterparty=MandateBankAccount(
        account_holder=MandatePartyIdentification(
            full_name='fullName0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        account_identification=MandateAccountIdentification2(
            mtype='MandateAccountIdentification2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id6',
    payment_instrument_id='paymentInstrumentId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

