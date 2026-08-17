
# Mandate 1

## Structure

`Mandate1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account linked to the payment instrument. |
| `counterparty` | [`MandateBankAccount2`](../../doc/models/mandate-bank-account-2.md) | Optional | Contains information to identify the counterparty. |
| `created_at` | `datetime` | Optional | The date when the mandate was created. |
| `id` | `str` | Optional | The unique identifier of the mandate. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument linked to the mandate. |
| `status` | [`MandateStatus2Enum`](../../doc/models/mandate-status-2-enum.md) | Optional | The status of the mandate.<br><br>Possible values: **pending**, **approved**, **cancelled**. |
| `mtype` | [`MandateType2Enum`](../../doc/models/mandate-type-2-enum.md) | Optional | The type of mandate. Possible value: **bacs**. |
| `updated_at` | `datetime` | Optional | The date when the mandate was updated. |

## Example

```python
import dateutil.parser

from adyen.models.mandate_1 import Mandate1
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account_2 import MandateBankAccount2
from adyen.models.mandate_party_identification_2 import MandatePartyIdentification2

mandate_1 = Mandate1(
    balance_account_id='balanceAccountId4',
    counterparty=MandateBankAccount2(
        account_holder=MandatePartyIdentification2(
            full_name='fullName0'
        ),
        account_identification=MandateAccountIdentification2(
            mtype='MandateAccountIdentification2'
        )
    ),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id4',
    payment_instrument_id='paymentInstrumentId6'
)
```

