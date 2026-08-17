
# Transaction Conditions

Conditions on which the transaction must be processed.

## Structure

`TransactionConditions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_payment_brand` | `List[str]` | Optional | Payment brands accepted for this transaction.<br>Card payment brands allowed by the Sale System for the payment transaction.<br>Restrict brand if data sent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_id` | `List[int]` | Optional | Identification of the Acquirer.<br>Restrict to these Acquirer if present. |
| `debit_preferred_flag` | `bool` | Optional | The preferred type of payment is a debit transaction rather than a credit transaction. |
| `allowed_loyalty_brand` | `List[str]` | Optional | Loyalty brands or programs allowed by the Sale System for the loyalty transaction.<br>Restrict brand if data sent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `loyalty_handling` | [`LoyaltyHandling1Enum`](../../doc/models/loyalty-handling-1-enum.md) | Optional | Type of Loyalty processing requested by the Sale System.<br>Possible values:<br><br>* **Allowed**<br>* **Forbidden**<br>* **Processed**<br>* **Proposed**<br>* **Required** |
| `customer_language` | `str` | Optional | The language used on the terminal screen or in text printed by the terminal.<br>Typical use case is setting the language on unattended terminals. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `force_online_flag` | `bool` | Optional | Indicates if the Cashier requires POI forces online access to the Acquirer.<br>Go online if data sent.<br><br>**Default**: `False` |
| `force_entry_mode` | [`List[ForceEntryModeEnum]`](../../doc/models/force-entry-mode-enum.md) | Optional | Payment instrument entry mode requested by the Sale System.<br>Restrict entry mode if sent.<br>Possible values:<br><br>* **CheckReader**<br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `merchant_category_code` | `str` | Optional | The code which identifies the category of the transaction (MCC).<br>The payment implies a specific MCC.<br><br>**Constraints**: *Pattern*: `^.{3,4}$` |

## Example

```python
from adyen.models.loyalty_handling_1_enum import LoyaltyHandling1Enum
from adyen.models.transaction_conditions import TransactionConditions

transaction_conditions = TransactionConditions(
    allowed_payment_brand=[
        'AllowedPaymentBrand6',
        'AllowedPaymentBrand7'
    ],
    acquirer_id=[
        98,
        97,
        96
    ],
    debit_preferred_flag=False,
    allowed_loyalty_brand=[
        'AllowedLoyaltyBrand4'
    ],
    loyalty_handling=LoyaltyHandling1Enum.PROCESSED,
    force_online_flag=False
)
```

