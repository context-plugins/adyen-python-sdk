
# Card Data

Information related to the payment card used for the transaction.
Allows acquisition of the card data by the Sale System before the Payment, CardAcquisition, or BalanceInquiry request to the POI. It can also be sent in the CardAcquisition response, to be processed by the Sale System.

## Structure

`CardData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_brand` | `str` | Optional | Type of payment card.<br>If card PAN is readable.<br>Indicates the card used to pay in the PaymentResponse. Sent in the CardAcquisitionResponse, to leave the Cashier to choose between several applications in a smartcard, or several brand in a co-branded card. In this case, the CardAcquisitionRequest.ForceCustomerSelectionFlag must contain the value False. Brands are part of the POI and Sale Systems configurations.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `masked_pan` | `str` | Optional | Masked Primary Account Number<br>Part of the PAN is replaced by a string of * characters, to identify a customer account or relationship. Presence of this data element, which replace the PAN when SensitiveCardData is protected and replaced by ProtectedCardData. Alternatively the MaskedPAN can be used as a token to identify a customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `payment_account_ref` | `str` | Optional | Reference of the PAN, which identifies the PAN or the card uniquely, named also PAR (Payment Account Reference). This reference may be defined by the card issuer or by a token service provider under the control of the card issuer, and cannot be used for a payment transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `entry_mode` | [`List[EntryModeEnum]`](../../doc/models/entry-mode-enum.md) | Optional | Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment instrument.<br>Possible values:<br><br>* **Contactless**<br>* **File**<br>* **ICC**<br>* **Keyed**<br>* **MagStripe**<br>* **Manual**<br>* **Mobile**<br>* **RFID**<br>* **Scanned**<br>* **SynchronousICC**<br>* **Tapped** |
| `card_country_code` | `int` | Optional | Country Code attached to the card (3 numerics).<br>If available in the card.<br><br>**Constraints**: `>= 3`, `<= 3` |
| `protected_card_data` | `str` | Optional | Sensitive information related to the payment card, protected by CMS.<br>SensitiveCardData protected by CMS EnvelopedData. |
| `sensitive_card_data` | [`SensitiveCardData1`](../../doc/models/sensitive-card-data-1.md) | Optional | Sensitive information related to the payment card, entered or read by the Sale System.<br>If structure non empty and unprotected. |
| `payment_token` | [`PaymentToken1`](../../doc/models/payment-token-1.md) | Optional | Surrogate of the PAN (Primary Account Number) of the payment card to identify the payment mean of the customer. It allows, for a merchant, to identify the customer.<br>Restriction of product payable by a card. |

## Example

```python
from adyen.models.card_data import CardData
from adyen.models.entry_mode_enum import EntryModeEnum

card_data = CardData(
    payment_brand='PaymentBrand0',
    masked_pan='MaskedPan0',
    payment_account_ref='PaymentAccountRef8',
    entry_mode=[
        EntryModeEnum.KEYED
    ],
    card_country_code=3
)
```

