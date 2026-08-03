
# Response Additional Data Card

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_alt_id` | `str` | Optional | This is an ALT ID (alternate ID) mapped to the Card PAN.<br><br>> Returned only in case of Ecommerce Card Payment in India |
| `card_bin` | `str` | Optional | The first six digits of the card number.<br><br>This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin) for card numbers with a six-digit BIN.<br><br>Example: 521234 |
| `card_holder_name` | `str` | Optional | The cardholder name passed in the payment request. |
| `card_issuing_bank` | `str` | Optional | The bank or the financial institution granting lines of credit through card association branded payment cards. This information can be included when available. |
| `card_issuing_country` | `str` | Optional | The country where the card was issued.<br><br>Example: US |
| `card_issuing_currency` | `str` | Optional | The currency in which the card is issued, if this information is available. Provided as the currency code or currency number from the ISO-4217 standard.<br><br>Example: USD |
| `card_payment_method` | `str` | Optional | The card payment method used for the transaction.<br><br>Example: amex |
| `card_product_id` | `str` | Optional | The Card Product ID represents the type of card following card scheme product definitions and can be returned for Adyen Acquiring service level payments.<br><br>Example values Visa:<br><br>* **A** - Visa Traditional<br>* **B** - Visa Traditional Rewards<br>* **C** - Visa Signature<br>* **D** - Visa Signature Preferred<br>* **F** - Visa Classic<br><br>Example values Mastercard:<br><br>* **MCC** - Mastercard Card<br>* **MCE** - Mastercard Electronic Card<br>* **MCF** - Mastercard Corporate Fleet Card<br>* **MCG** - Gold Mastercard Card<br>* **MCH** - Mastercard Premium Charge<br>* **MCI** - Mastercard Select Debit |
| `card_summary` | `str` | Optional | The last four digits of a card number.<br><br>> Returned only in case of a card payment. |
| `issuer_bin` | `str` | Optional | The first eight digits of the card number. Only returned if the card number is 16 digits or more.<br><br>This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin) for card numbers with an eight-digit BIN.<br><br>Example: 52123423 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_card import ResponseAdditionalDataCard

response_additional_data_card = ResponseAdditionalDataCard(
    card_alt_id='cardAltID4',
    card_bin='cardBin6',
    card_holder_name='cardHolderName4',
    card_issuing_bank='cardIssuingBank6',
    card_issuing_country='cardIssuingCountry8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

