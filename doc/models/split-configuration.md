
# Split Configuration

## Structure

`SplitConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Your description for the split configuration.<br><br>**Constraints**: *Maximum Length*: `300` |
| `rules` | [`List[SplitConfigurationRule]`](../../doc/models/split-configuration-rule.md) | Required | Array of rules that define the split configuration behavior. |
| `split_configuration_id` | `str` | Optional, Read-only | Unique identifier of the split configuration. |

## Example

```python
from adyen.models.acquiring_fees_enum import AcquiringFeesEnum
from adyen.models.additional_commission_1 import AdditionalCommission1
from adyen.models.adyen_commission_enum import AdyenCommissionEnum
from adyen.models.adyen_fees_enum import AdyenFeesEnum
from adyen.models.adyen_markup_enum import AdyenMarkupEnum
from adyen.models.card_region_enum import CardRegionEnum
from adyen.models.commission_1 import Commission1
from adyen.models.funding_source_1_enum import FundingSource1Enum
from adyen.models.shopper_interaction_11_enum import ShopperInteraction11Enum
from adyen.models.split_configuration import SplitConfiguration
from adyen.models.split_configuration_logic_2 import SplitConfigurationLogic2
from adyen.models.split_configuration_rule import SplitConfigurationRule

split_configuration = SplitConfiguration(
    description='description8',
    rules=[
        SplitConfigurationRule(
            currency='currency2',
            funding_source=FundingSource1Enum.PREPAID,
            payment_method='paymentMethod4',
            shopper_interaction=ShopperInteraction11Enum.ANY,
            split_logic=SplitConfigurationLogic2(
                commission=Commission1(
                    fixed_amount=112,
                    variable_percentage=52
                ),
                acquiring_fees=AcquiringFeesEnum.DEDUCTFROMLIABLEACCOUNT,
                additional_commission=AdditionalCommission1(
                    balance_account_id='balanceAccountId0',
                    fixed_amount=100,
                    variable_percentage=64
                ),
                adyen_commission=AdyenCommissionEnum.DEDUCTFROMLIABLEACCOUNT,
                adyen_fees=AdyenFeesEnum.DEDUCTFROMLIABLEACCOUNT,
                adyen_markup=AdyenMarkupEnum.DEDUCTFROMLIABLEACCOUNT
            ),
            card_region=CardRegionEnum.INTERNATIONAL
        )
    ]
)
```

