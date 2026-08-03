
# Cost Estimate Request

*This model accepts additional fields of type Any.*

## Structure

`CostEstimateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `assumptions` | [`CostEstimateAssumptions`](../../doc/models/cost-estimate-assumptions.md) | Optional | - |
| `card_number` | `str` | Optional | The card number (4-19 characters) for PCI compliant use cases. Do not use any separators.<br><br>> Either the `cardNumber` or `encryptedCardNumber` field must be provided in a payment request.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `encrypted_card_number` | `str` | Optional | Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created with the Checkout Card Component or Secured Fields Component, and must contain the `encryptedCardNumber` field.<br><br>> Either the `cardNumber` or `encryptedCardNumber` field must be provided in a payment request. |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the (transaction) request with. |
| `merchant_details` | [`MerchantDetails`](../../doc/models/merchant-details.md) | Optional | - |
| `recurring` | [`Recurring3`](../../doc/models/recurring-3.md) | Optional | - |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this cost estimate. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `shopper_interaction` | [`ShopperInteraction1`](../../doc/models/shopper-interaction-1.md) | Optional | - |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.contract import Contract
from adyen.models.cost_estimate_assumptions import CostEstimateAssumptions
from adyen.models.cost_estimate_request import CostEstimateRequest
from adyen.models.merchant_details import MerchantDetails
from adyen.models.recurring_3 import Recurring3
from adyen.models.token_service import TokenService

cost_estimate_request = CostEstimateRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount8',
    assumptions=CostEstimateAssumptions(
        assume_3_d_secure_authenticated=False,
        assume_level_3_data=False,
        installments=20,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_number='cardNumber6',
    encrypted_card_number='encryptedCardNumber8',
    merchant_details=MerchantDetails(
        country_code='countryCode8',
        enrolled_in_3_d_secure=False,
        mcc='mcc6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    recurring=Recurring3(
        contract=Contract.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenService.VISATOKENSERVICE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

