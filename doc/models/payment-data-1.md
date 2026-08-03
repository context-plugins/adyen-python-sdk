
# Payment Data 1

Data related to the payment transaction.
If one data element is present.

*This model accepts additional fields of type Any.*

## Structure

`PaymentData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`PaymentType1`](../../doc/models/payment-type-1.md) | Optional | - |
| `split_payment_flag` | `bool` | Optional | Indicates if the payment of the Sale transaction is split. Allows the POI to decline payment means that cannot accept split payment.<br><br>**Default**: `False` |
| `requested_validity_date` | `date` | Optional | Requested validity date for the reservation. Allows a specific period for the reservation according to the need of the Merchant for the first reservation and the reservation updates as well. |
| `card_acquisition_reference` | [`CardAcquisitionReference`](../../doc/models/card-acquisition-reference.md) | Optional | - |
| `instalment` | [`Instalment`](../../doc/models/instalment.md) | Optional | - |
| `payment_instrument_data` | [`PaymentInstrumentData2`](../../doc/models/payment-instrument-data-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_acquisition_reference import CardAcquisitionReference
from adyen.models.instalment import Instalment
from adyen.models.instalment_type import InstalmentType
from adyen.models.payment_data_1 import PaymentData1
from adyen.models.payment_type_1 import PaymentType1
from adyen.models.period_unit_1 import PeriodUnit1

payment_data_1 = PaymentData1(
    payment_type=PaymentType1.ONETIMERESERVATION,
    split_payment_flag=False,
    requested_validity_date=dateutil.parser.parse('2016-03-13').date(),
    card_acquisition_reference=CardAcquisitionReference(
        transaction_id='TransactionID8',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    instalment=Instalment(
        instalment_type=InstalmentType.DEFERREDINSTALMENTS,
        sequence_number=106,
        plan_id='PlanID4',
        period=70,
        period_unit=PeriodUnit1.MONTHLY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

