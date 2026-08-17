
# Donation Campaigns Request

## Structure

`DonationCampaignsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes/). |
| `locale` | `str` | Optional | Locale on the shopper interaction device. |
| `merchant_account` | `str` | Required | Your merchant account identifier. |
| `store` | `str` | Optional | Required for Adyen for Platforms integrations if you are a platform model. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/platforms)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. |

## Example

```python
from adyen.models.donation_campaigns_request import DonationCampaignsRequest

donation_campaigns_request = DonationCampaignsRequest(
    currency='currency4',
    merchant_account='merchantAccount6',
    locale='locale2',
    store='store4'
)
```

