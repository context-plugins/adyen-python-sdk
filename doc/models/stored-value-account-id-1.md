
# Stored Value Account ID 1

Identification of the stored value account or the stored value card.
If the identification of the Stored Value account or card has been made by the Sale System before the request.

## Structure

`StoredValueAccountID1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_account_type` | [`StoredValueAccountType1Enum`](../../doc/models/stored-value-account-type-1-enum.md) | Required | Type of stored value account. Allows the distinction of the stored value instrument to access the stored value account.<br>Possible values:<br><br>* **GiftCard**<br>* **Other**<br>* **PhoneCard** |
| `stored_value_provider` | `str` | Optional | Identification of the provider of the stored value account load/reload. When the ProductCode is not sufficient to identify the provider host which delivers the load or reload of the stored value account (for example if it contains the identification of the application.)<br><br>**Constraints**: *Pattern*: `^.+$` |
| `owner_name` | `str` | Optional | Name of the owner of a stored value account.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `expiry_date` | `int` | Optional | Date after which the card cannot be used. If EMV expiry date is present, it overrides Track2 information. Format is MMYY.<br><br>**Constraints**: `>= 4`, `<= 4` |
| `entry_mode` | [`List[EntryModeEnum]`](../../doc/models/entry-mode-enum.md) | Required | Entry mode of the payment instrument information. In the Payment, Loyalty, or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. (e.g. because the payment instrument information are a barcode read by the Cashier on a scanner device).<br>Possible values:<br><br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **Mobile**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `identification_type` | [`IdentificationType11Enum`](../../doc/models/identification-type-11-enum.md) | Required | Type of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.<br>Possible values:<br><br>* **AccountNumber**<br>* **BarCode**<br>* **ISOTrack2**<br>* **PAN**<br>* **PhoneNumber** |
| `stored_value_id` | `str` | Required | Stored value account identification. The identification of the stored value account conforming to the IdentificationType.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.stored_value_account_id_1 import StoredValueAccountID1
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum

stored_value_account_id_1 = StoredValueAccountID1(
    stored_value_account_type=StoredValueAccountType1Enum.PHONECARD,
    entry_mode=[
        EntryModeEnum.FILE,
        EntryModeEnum.SCANNED,
        EntryModeEnum.MAGSTRIPE
    ],
    identification_type=IdentificationType11Enum.ACCOUNTNUMBER,
    stored_value_id='StoredValueID4',
    stored_value_provider='StoredValueProvider2',
    owner_name='OwnerName6',
    expiry_date=4
)
```

