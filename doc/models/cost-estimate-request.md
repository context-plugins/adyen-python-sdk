
# Cost Estimate Request

## Structure

`CostEstimateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The transaction amount used as a base for the cost estimation. |
| `assumptions` | [`CostEstimateAssumptions1`](../../doc/models/cost-estimate-assumptions-1.md) | Optional | Assumptions made for the expected characteristics of the transaction, for which the charges are being estimated. |
| `card_number` | `str` | Optional | The card number (4-19 characters) for PCI compliant use cases. Do not use any separators.<br><br>> Either the `cardNumber` or `encryptedCardNumber` field must be provided in a payment request.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `encrypted_card_number` | `str` | Optional | Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created with the Checkout Card Component or Secured Fields Component, and must contain the `encryptedCardNumber` field.<br><br>> Either the `cardNumber` or `encryptedCardNumber` field must be provided in a payment request. |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the (transaction) request with. |
| `merchant_details` | [`MerchantDetails2`](../../doc/models/merchant-details-2.md) | Optional | Additional data for merchants who don't use Adyen as the payment authorisation gateway. |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Optional | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/online-payments/tokenization). |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this cost estimate. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the card holder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.contract_enum import ContractEnum
from adyen.models.cost_estimate_assumptions_1 import CostEstimateAssumptions1
from adyen.models.cost_estimate_request import CostEstimateRequest
from adyen.models.merchant_details_2 import MerchantDetails2
from adyen.models.recurring import Recurring
from adyen.models.token_service_enum import TokenServiceEnum

cost_estimate_request = CostEstimateRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount8',
    assumptions=CostEstimateAssumptions1(
        assume_3_d_secure_authenticated=False,
        assume_level_3_data=False,
        installments=20
    ),
    card_number='cardNumber6',
    encrypted_card_number='encryptedCardNumber8',
    merchant_details=MerchantDetails2(
        country_code='countryCode8',
        enrolled_in_3_d_secure=False,
        mcc='mcc6'
    ),
    recurring=Recurring(
        contract=ContractEnum.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenServiceEnum.VISATOKENSERVICE
    )
)
```

