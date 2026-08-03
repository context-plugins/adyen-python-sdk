
# Card 6

*This model accepts additional fields of type Any.*

## Structure

`Card6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cvc` | `str` | Optional | The [card verification code](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid) (1-20 characters). Depending on the card brand, it is known also as:<br><br>* CVV2/CVC2 – length: 3 digits<br>* CID – length: 4 digits<br><br>> If you are using [Client-Side Encryption](https://docs.adyen.com/classic-integration/cse-integration-ecommerce), the CVC code is present in the encrypted data. You must never post the card details to the server.<br>> This field must be always present in a [one-click payment request](https://docs.adyen.com/classic-integration/recurring-payments).<br>> When this value is returned in a response, it is always empty because it is not stored.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `20` |
| `expiry_month` | `str` | Optional | The card expiry month.<br>Format: 2 digits, zero-padded for single digits. For example:<br><br>* 03 = March<br>* 11 = November<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2` |
| `expiry_year` | `str` | Optional | The card expiry year.<br>Format: 4 digits. For example: 2020<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `holder_name` | `str` | Optional | The name of the cardholder, as printed on the card.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `issue_number` | `str` | Optional | The issue number of the card (for some UK debit cards only).<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2` |
| `number` | `str` | Optional | The card number (4-19 characters). Do not use any separators.<br>When this value is returned in a response, only the last 4 digits of the card number are returned.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `start_month` | `str` | Optional | The month component of the start date (for some UK debit cards only).<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2` |
| `start_year` | `str` | Optional | The year component of the start date (for some UK debit cards only).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_6 import Card6

card_6 = Card6(
    cvc='cvc6',
    expiry_month='expiryMonth6',
    expiry_year='expiryYear4',
    holder_name='holderName8',
    issue_number='issueNumber6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

