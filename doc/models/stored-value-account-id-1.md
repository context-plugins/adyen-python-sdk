
# Stored Value Account Id 1

Identification of the stored value account or the stored value card.
If the identification of the Stored Value account or card has been made by the Sale System before the request.

*This model accepts additional fields of type Any.*

## Structure

`StoredValueAccountId1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_account_type` | [`StoredValueAccountType1`](../../doc/models/stored-value-account-type-1.md) | Required | - |
| `stored_value_provider` | `str` | Optional | Identification of the provider of the stored value account load/reload. When the ProductCode is not sufficient to identify the provider host which delivers the load or reload of the stored value account (for example if it contains the identification of the application.)<br><br>**Constraints**: *Pattern*: `^.+$` |
| `owner_name` | `str` | Optional | Name of the owner of a stored value account.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `expiry_date` | `int` | Optional | Date after which the card cannot be used. If EMV expiry date is present, it overrides Track2 information. Format is MMYY.<br><br>**Constraints**: `>= 4`, `<= 4` |
| `entry_mode` | [`List[EntryMode]`](../../doc/models/entry-mode.md) | Required | Entry mode of the payment instrument information. In the Payment, Loyalty, or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. (e.g. because the payment instrument information are a barcode read by the Cashier on a scanner device).<br>Possible values:<br><br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **Mobile**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `identification_type` | [`IdentificationType11`](../../doc/models/identification-type-11.md) | Required | - |
| `stored_value_id` | `str` | Required | Stored value account identification. The identification of the stored value account conforming to the IdentificationType.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.stored_value_account_id_1 import StoredValueAccountId1
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1

stored_value_account_id_1 = StoredValueAccountId1(
    stored_value_account_type=StoredValueAccountType1.PHONECARD,
    entry_mode=[
        EntryMode.FILE,
        EntryMode.SCANNED,
        EntryMode.MAGSTRIPE
    ],
    identification_type=IdentificationType11.ACCOUNTNUMBER,
    stored_value_id='StoredValueID4',
    stored_value_provider='StoredValueProvider2',
    owner_name='OwnerName6',
    expiry_date=4,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

