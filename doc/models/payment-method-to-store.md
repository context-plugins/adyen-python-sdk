
# Payment Method to Store

## Structure

`PaymentMethodToStore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | Secondary brand of the card. For example: **plastix**, **hmclub**. |
| `cvc` | `str` | Optional | The card verification code. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `encrypted_card` | `str` | Optional | The encrypted card.<br><br>**Constraints**: *Maximum Length*: `40000` |
| `encrypted_card_number` | `str` | Optional | The encrypted card number.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_expiry_month` | `str` | Optional | The encrypted card expiry month.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_expiry_year` | `str` | Optional | The encrypted card expiry year.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `encrypted_security_code` | `str` | Optional | The encrypted card verification code.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `expiry_month` | `str` | Optional | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `expiry_year` | `str` | Optional | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `holder_name` | `str` | Optional | The name of the card holder. |
| `number` | `str` | Optional | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `mtype` | `str` | Optional | Set to **scheme**. |

## Example

```python
from adyen.models.payment_method_to_store import PaymentMethodToStore

payment_method_to_store = PaymentMethodToStore(
    brand='brand0',
    cvc='cvc0',
    encrypted_card='encryptedCard8',
    encrypted_card_number='encryptedCardNumber4',
    encrypted_expiry_month='encryptedExpiryMonth8'
)
```

