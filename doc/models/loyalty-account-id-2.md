
# Loyalty Account ID 2

Identification of a Loyalty account.

## Structure

`LoyaltyAccountID2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entry_mode` | [`List[EntryModeEnum]`](../../doc/models/entry-mode-enum.md) | Required | Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.<br>Possible values:<br><br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **Mobile**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `identification_type` | [`IdentificationType11Enum`](../../doc/models/identification-type-11-enum.md) | Required | Type of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.<br>Possible values:<br><br>* **AccountNumber**<br>* **BarCode**<br>* **ISOTrack2**<br>* **PAN**<br>* **PhoneNumber** |
| `identification_support` | [`IdentificationSupport1Enum`](../../doc/models/identification-support-1-enum.md) | Optional | Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account identification.<br>Possible values:<br><br>* **HybridCard**<br>* **LinkedCard**<br>* **LoyaltyCard**<br>* **NoCard** |
| `loyalty_id` | `str` | Required | Loyalty account identification conforming to the IdentificationType. |

## Example

```python
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2

loyalty_account_id_2 = LoyaltyAccountID2(
    entry_mode=[
        EntryModeEnum.MOBILE,
        EntryModeEnum.RFID
    ],
    identification_type=IdentificationType11Enum.ISOTRACK2,
    loyalty_id='LoyaltyID4',
    identification_support=IdentificationSupport1Enum.HYBRIDCARD
)
```

