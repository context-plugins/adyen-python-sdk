
# Loyalty Account Id 3

*This model accepts additional fields of type Any.*

## Structure

`LoyaltyAccountId3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entry_mode` | [`List[EntryMode]`](../../doc/models/entry-mode.md) | Required | Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.<br>Possible values:<br><br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **Mobile**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `identification_type` | [`IdentificationType11`](../../doc/models/identification-type-11.md) | Required | - |
| `identification_support` | [`IdentificationSupport1`](../../doc/models/identification-support-1.md) | Optional | - |
| `loyalty_id` | `str` | Required | Loyalty account identification conforming to the IdentificationType. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3

loyalty_account_id_3 = LoyaltyAccountId3(
    entry_mode=[
        EntryMode.MAGSTRIPE,
        EntryMode.SCANNED,
        EntryMode.FILE
    ],
    identification_type=IdentificationType11.ACCOUNTNUMBER,
    loyalty_id='LoyaltyID6',
    identification_support=IdentificationSupport1.NOCARD,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

