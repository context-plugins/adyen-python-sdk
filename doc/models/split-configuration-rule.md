
# Split Configuration Rule

*This model accepts additional fields of type Any.*

## Structure

`SplitConfigurationRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_region` | [`CardRegion`](../../doc/models/card-region.md) | Optional | - |
| `currency` | `str` | Required | The currency condition that defines whether the split logic applies.<br>Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
| `funding_source` | [`FundingSource1`](../../doc/models/funding-source-1.md) | Required | - |
| `payment_method` | `str` | Required | The payment method condition that defines whether the split logic applies.<br><br>Possible values:<br><br>* [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method.<br>* **ANY**: Apply the split logic for all available payment methods. |
| `rule_id` | `str` | Optional, Read-only | The unique identifier of the split configuration rule. |
| `shopper_interaction` | [`ShopperInteraction11`](../../doc/models/shopper-interaction-11.md) | Required | - |
| `split_logic` | [`SplitConfigurationLogic`](../../doc/models/split-configuration-logic.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.acquiring_fees import AcquiringFees
from adyen.models.additional_commission import AdditionalCommission
from adyen.models.adyen_commission import AdyenCommission
from adyen.models.adyen_fees import AdyenFees
from adyen.models.adyen_markup import AdyenMarkup
from adyen.models.card_region import CardRegion
from adyen.models.commission import Commission
from adyen.models.funding_source_1 import FundingSource1
from adyen.models.shopper_interaction_11 import ShopperInteraction11
from adyen.models.split_configuration_logic import SplitConfigurationLogic
from adyen.models.split_configuration_rule import SplitConfigurationRule

split_configuration_rule = SplitConfigurationRule(
    currency='currency0',
    funding_source=FundingSource1.CHARGED,
    payment_method='paymentMethod8',
    shopper_interaction=ShopperInteraction11.CONTAUTH,
    split_logic=SplitConfigurationLogic(
        commission=Commission(
            fixed_amount=112,
            variable_percentage=52,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        acquiring_fees=AcquiringFees.DEDUCTFROMLIABLEACCOUNT,
        additional_commission=AdditionalCommission(
            balance_account_id='balanceAccountId0',
            fixed_amount=100,
            variable_percentage=64,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        adyen_commission=AdyenCommission.DEDUCTFROMLIABLEACCOUNT,
        adyen_fees=AdyenFees.DEDUCTFROMLIABLEACCOUNT,
        adyen_markup=AdyenMarkup.DEDUCTFROMLIABLEACCOUNT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_region=CardRegion.DOMESTIC,
    rule_id='ruleId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

