
# Checkout Forward Request Card 2

The card details.

## Structure

`CheckoutForwardRequestCard2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cvc` | `str` | Optional | The [card verification code](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid) (1-20 characters). Depending on the card brand, it is also known as:<br><br>* CVV2/CVC2 – length: 3 digits<br>* CID – length: 4 digits |
| `encrypted_card_number` | `str` | Optional | The encrypted card number. |
| `encrypted_expiry_month` | `str` | Optional | The encrypted expiryMonth |
| `encrypted_expiry_year` | `str` | Optional | The encrypted card expiry year. |
| `encrypted_security_code` | `str` | Optional | The encrypted security code. |
| `expiry_month` | `str` | Optional | The card expiry month.<br>Format: 2 digits, zero-padded for single digits. For example:<br><br>* 03 = March<br>* 11 = November |
| `expiry_year` | `str` | Optional | The card expiry year. |
| `holder_name` | `str` | Optional | The name of the cardholder. |
| `number` | `str` | Optional | The card number. Only collect raw card data if you are fully [PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide).<br>Format: Do not use separators. |
| `mtype` | [`Type18Enum`](../../doc/models/type-18-enum.md) | Optional | Default payment method details. Common for scheme payment methods, and for simple payment method details.<br><br>**Default**: `"scheme"` |

## Example

```python
from adyen.models.checkout_forward_request_card_2 import CheckoutForwardRequestCard2
from adyen.models.type_18_enum import Type18Enum

checkout_forward_request_card_2 = CheckoutForwardRequestCard2(
    cvc='cvc0',
    encrypted_card_number='encryptedCardNumber4',
    encrypted_expiry_month='encryptedExpiryMonth8',
    encrypted_expiry_year='encryptedExpiryYear6',
    encrypted_security_code='encryptedSecurityCode2',
    mtype=Type18Enum.SCHEME
)
```

