
# Split Configuration List

*This model accepts additional fields of type Any.*

## Structure

`SplitConfigurationList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[SplitConfiguration]`](../../doc/models/split-configuration.md) | Optional | List of split configurations applied to the stores under the merchant account. |
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
from adyen.models.split_configuration import SplitConfiguration
from adyen.models.split_configuration_list import SplitConfigurationList
from adyen.models.split_configuration_logic import SplitConfigurationLogic
from adyen.models.split_configuration_rule import SplitConfigurationRule

split_configuration_list = SplitConfigurationList(
    data=[
        SplitConfiguration(
            description='description0',
            rules=[
                SplitConfigurationRule(
                    currency='currency2',
                    funding_source=FundingSource1.PREPAID,
                    payment_method='paymentMethod4',
                    shopper_interaction=ShopperInteraction11.ANY,
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
                    card_region=CardRegion.INTERNATIONAL,
                    rule_id='ruleId2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                SplitConfigurationRule(
                    currency='currency2',
                    funding_source=FundingSource1.PREPAID,
                    payment_method='paymentMethod4',
                    shopper_interaction=ShopperInteraction11.ANY,
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
                    card_region=CardRegion.INTERNATIONAL,
                    rule_id='ruleId2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            split_configuration_id='splitConfigurationId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SplitConfiguration(
            description='description0',
            rules=[
                SplitConfigurationRule(
                    currency='currency2',
                    funding_source=FundingSource1.PREPAID,
                    payment_method='paymentMethod4',
                    shopper_interaction=ShopperInteraction11.ANY,
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
                    card_region=CardRegion.INTERNATIONAL,
                    rule_id='ruleId2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                SplitConfigurationRule(
                    currency='currency2',
                    funding_source=FundingSource1.PREPAID,
                    payment_method='paymentMethod4',
                    shopper_interaction=ShopperInteraction11.ANY,
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
                    card_region=CardRegion.INTERNATIONAL,
                    rule_id='ruleId2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            split_configuration_id='splitConfigurationId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

