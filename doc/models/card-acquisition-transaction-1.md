
# Card Acquisition Transaction 1

Data related to the payment and loyalty card acquisition.

## Structure

`CardAcquisitionTransaction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_payment_brand` | `List[str]` | Optional | Card payment brands allowed by the Sale System for the payment transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `allowed_loyalty_brand` | `List[str]` | Optional | Loyalty brands or programs allowed by the Sale System for the loyalty transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `loyalty_handling` | [`LoyaltyHandling2Enum`](../../doc/models/loyalty-handling-2-enum.md) | Optional | Type of Loyalty processing requested by the Sale System. An way to specify what the POI has to handle concerning the loyalty.<br>Possible values:<br><br>* **Allowed**<br>* **Forbidden**<br>* **Processed**<br>* **Proposed**<br>* **Required** |
| `customer_language` | `str` | Optional | The language used on the terminal screen or in text printed by the terminal.<br>Typical use case is setting the language on unattended terminals. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `force_entry_mode` | [`List[ForceEntryModeEnum]`](../../doc/models/force-entry-mode-enum.md) | Optional | Payment instrument entry mode requested by the Sale System. Avoid retry on an out of order card reading device, when the sale system knows that some card entry modes on the POI do not work.<br>Possible values:<br><br>* **CheckReader**<br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `force_customer_selection_flag` | `bool` | Optional | Indicates if the Customer realises the selection of the card application. |
| `total_amount` | `float` | Optional | Amount of a transaction. In the Card Acquisition Request message, it allows the processing of a contactless card.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `payment_type` | [`PaymentType1Enum`](../../doc/models/payment-type-1-enum.md) | Optional | Type of payment transaction. Elements requested by the Sale System that are related to the payment only.<br>Possible values:<br><br>* **CashAdvance**<br>* **CashDeposit**<br>* **Completion**<br>* **FirstReservation**<br>* **Instalment**<br>* **IssuerInstalment**<br>* **Normal**<br>* **OneTimeReservation**<br>* **PaidOut**<br>* **Recurring**<br>* **Refund**<br>* **UpdateReservation** |
| `cash_back_flag` | `bool` | Optional | Cash back has been requested with the payment transaction. Allows choice of the Customer language when the POI displays messages or print text to Merchant interface. |

## Example

```python
from adyen.models.card_acquisition_transaction_1 import CardAcquisitionTransaction1
from adyen.models.force_entry_mode_enum import ForceEntryModeEnum
from adyen.models.loyalty_handling_2_enum import LoyaltyHandling2Enum

card_acquisition_transaction_1 = CardAcquisitionTransaction1(
    allowed_payment_brand=[
        'AllowedPaymentBrand4',
        'AllowedPaymentBrand5',
        'AllowedPaymentBrand6'
    ],
    allowed_loyalty_brand=[
        'AllowedLoyaltyBrand2',
        'AllowedLoyaltyBrand3'
    ],
    loyalty_handling=LoyaltyHandling2Enum.REQUIRED,
    customer_language='CustomerLanguage6',
    force_entry_mode=[
        ForceEntryModeEnum.SCANNED,
        ForceEntryModeEnum.MAGSTRIPE
    ]
)
```

