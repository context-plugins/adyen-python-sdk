
# Transaction Conditions 1

*This model accepts additional fields of type Any.*

## Structure

`TransactionConditions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_payment_brand` | `List[str]` | Optional | Payment brands accepted for this transaction.<br>Card payment brands allowed by the Sale System for the payment transaction.<br>Restrict brand if data sent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Restrict to these Acquirer if present. |
| `debit_preferred_flag` | `bool` | Optional | The preferred type of payment is a debit transaction rather than a credit transaction. |
| `allowed_loyalty_brand` | `List[str]` | Optional | Loyalty brands or programs allowed by the Sale System for the loyalty transaction.<br>Restrict brand if data sent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `loyalty_handling` | [`LoyaltyHandling1`](../../doc/models/loyalty-handling-1.md) | Optional | - |
| `customer_language` | `str` | Optional | The language used on the terminal screen or in text printed by the terminal.<br>Typical use case is setting the language on unattended terminals. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `force_online_flag` | `bool` | Optional | Indicates if the Cashier requires POI forces online access to the Acquirer.<br>Go online if data sent.<br><br>**Default**: `False` |
| `force_entry_mode` | [`List[ForceEntryMode]`](../../doc/models/force-entry-mode.md) | Optional | Payment instrument entry mode requested by the Sale System.<br>Restrict entry mode if sent.<br>Possible values:<br><br>* **CheckReader**<br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `merchant_category_code` | `str` | Optional | The code which identifies the category of the transaction (MCC).<br>The payment implies a specific MCC.<br><br>**Constraints**: *Pattern*: `^.{3,4}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.loyalty_handling_1 import LoyaltyHandling1
from adyen.models.transaction_conditions_1 import TransactionConditions1

transaction_conditions_1 = TransactionConditions1(
    allowed_payment_brand=[
        'AllowedPaymentBrand6'
    ],
    acquirer_id=[
        100
    ],
    debit_preferred_flag=False,
    allowed_loyalty_brand=[
        'AllowedLoyaltyBrand4',
        'AllowedLoyaltyBrand5',
        'AllowedLoyaltyBrand6'
    ],
    loyalty_handling=LoyaltyHandling1.PROCESSED,
    force_online_flag=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

