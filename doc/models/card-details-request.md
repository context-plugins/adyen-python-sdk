
# Card Details Request

## Structure

`CardDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number` | `str` | Optional | A minimum of the first six digits of the card number. The full card number gives the best result.<br><br>You must be [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide) to collect raw card data. Alternatively, you can use the `encryptedCardNumber` field. |
| `country_code` | `str` | Optional | The shopper country code.<br><br>Format: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)<br>Example: NL or DE |
| `encrypted_card_number` | `str` | Optional | The encrypted card number.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `supported_brands` | `List[str]` | Optional | The card brands you support. This is the [`brands`](https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentMethods#responses-200-paymentMethods-brands) array from your [`/paymentMethods`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods) response.<br><br>If not included, our API uses the ones configured for your merchant account and, if provided, the country code. |

## Example

```python
from adyen.models.card_details_request import CardDetailsRequest

card_details_request = CardDetailsRequest(
    merchant_account='merchantAccount2',
    card_number='cardNumber2',
    country_code='countryCode8',
    encrypted_card_number='encryptedCardNumber4',
    supported_brands=[
        'supportedBrands5',
        'supportedBrands4',
        'supportedBrands3'
    ]
)
```

