
# Loyalty Data

In the Payment, Loyalty or Balance Inquiry Request message, it allows the Sale Terminal to send the identification of the loyalty account or an awarded amount or an amount to redeem to the loyalty account.
Data related to a Loyalty program or account.

*This model accepts additional fields of type Any.*

## Structure

`LoyaltyData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_acquisition_reference` | [`CardAcquisitionReference`](../../doc/models/card-acquisition-reference.md) | Optional | - |
| `loyalty_account_id` | [`LoyaltyAccountId3`](../../doc/models/loyalty-account-id-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_acquisition_reference import CardAcquisitionReference
from adyen.models.entry_mode import EntryMode
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_data import LoyaltyData

loyalty_data = LoyaltyData(
    card_acquisition_reference=CardAcquisitionReference(
        transaction_id='TransactionID8',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    loyalty_account_id=LoyaltyAccountId3(
        entry_mode=[
            EntryMode.FILE
        ],
        identification_type=IdentificationType11.ISOTRACK2,
        loyalty_id='LoyaltyID4',
        identification_support=IdentificationSupport1.HYBRIDCARD,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

