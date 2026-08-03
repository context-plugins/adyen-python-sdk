
# Loyalty Account

This data structure conveys the identification of the account and the associated loyalty brand.
Data related to a loyalty account processed in the transaction.

*This model accepts additional fields of type Any.*

## Structure

`LoyaltyAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account_id` | [`LoyaltyAccountId3`](../../doc/models/loyalty-account-id-3.md) | Required | - |
| `loyalty_brand` | `str` | Optional | Identification of a Loyalty brand.<br>If a card is analysed.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3

loyalty_account = LoyaltyAccount(
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
    loyalty_brand='LoyaltyBrand2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

