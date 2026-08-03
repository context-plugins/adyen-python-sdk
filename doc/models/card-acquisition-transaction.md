
# Card Acquisition Transaction

*This model accepts additional fields of type Any.*

## Structure

`CardAcquisitionTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_payment_brand` | `List[str]` | Optional | Card payment brands allowed by the Sale System for the payment transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `allowed_loyalty_brand` | `List[str]` | Optional | Loyalty brands or programs allowed by the Sale System for the loyalty transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `loyalty_handling` | [`LoyaltyHandling2`](../../doc/models/loyalty-handling-2.md) | Optional | - |
| `customer_language` | `str` | Optional | The language used on the terminal screen or in text printed by the terminal.<br>Typical use case is setting the language on unattended terminals. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `force_entry_mode` | [`List[ForceEntryMode]`](../../doc/models/force-entry-mode.md) | Optional | Payment instrument entry mode requested by the Sale System. Avoid retry on an out of order card reading device, when the sale system knows that some card entry modes on the POI do not work.<br>Possible values:<br><br>* **CheckReader**<br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `force_customer_selection_flag` | `bool` | Optional | Indicates if the Customer realises the selection of the card application. |
| `total_amount` | `float` | Optional | Amount of a transaction. In the Card Acquisition Request message, it allows the processing of a contactless card.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `payment_type` | [`PaymentType1`](../../doc/models/payment-type-1.md) | Optional | - |
| `cash_back_flag` | `bool` | Optional | Cash back has been requested with the payment transaction. Allows choice of the Customer language when the POI displays messages or print text to Merchant interface. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_acquisition_transaction import CardAcquisitionTransaction
from adyen.models.force_entry_mode import ForceEntryMode
from adyen.models.loyalty_handling_2 import LoyaltyHandling2

card_acquisition_transaction = CardAcquisitionTransaction(
    allowed_payment_brand=[
        'AllowedPaymentBrand0',
        'AllowedPaymentBrand1'
    ],
    allowed_loyalty_brand=[
        'AllowedLoyaltyBrand8'
    ],
    loyalty_handling=LoyaltyHandling2.FORBIDDEN,
    customer_language='CustomerLanguage2',
    force_entry_mode=[
        ForceEntryMode.CONTACTLESS
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

