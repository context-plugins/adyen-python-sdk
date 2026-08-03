
# Transaction Rule Response

*This model accepts additional fields of type Any.*

## Structure

`TransactionRuleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_rule` | [`TransactionRule`](../../doc/models/transaction-rule.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.active_network_tokens_restriction import ActiveNetworkTokensRestriction
from adyen.models.bank_identification import BankIdentification
from adyen.models.brand_variants_restriction import BrandVariantsRestriction
from adyen.models.counterparty_bank_restriction import CounterpartyBankRestriction
from adyen.models.counterparty_types_restriction import CounterpartyTypesRestriction
from adyen.models.countries_restriction import CountriesRestriction
from adyen.models.day_of_week import DayOfWeek
from adyen.models.duration import Duration
from adyen.models.identification_type import IdentificationType
from adyen.models.outcome_type import OutcomeType
from adyen.models.transaction_rule import TransactionRule
from adyen.models.transaction_rule_entity_key import TransactionRuleEntityKey
from adyen.models.transaction_rule_interval import TransactionRuleInterval
from adyen.models.transaction_rule_response import TransactionRuleResponse
from adyen.models.transaction_rule_restrictions import TransactionRuleRestrictions
from adyen.models.type_13 import Type13
from adyen.models.type_14 import Type14
from adyen.models.unit import Unit
from adyen.models.value import Value

transaction_rule_response = TransactionRuleResponse(
    transaction_rule=TransactionRule(
        description='description2',
        entity_key=TransactionRuleEntityKey(
            entity_reference='entityReference2',
            entity_type='entityType0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        interval=TransactionRuleInterval(
            mtype=Type13.MONTHLY,
            day_of_month=178,
            day_of_week=DayOfWeek.SATURDAY,
            duration=Duration(
                unit=Unit.WEEKS,
                value=176,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            time_of_day='timeOfDay2',
            time_zone='timeZone4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        reference='reference2',
        rule_restrictions=TransactionRuleRestrictions(
            active_network_tokens=ActiveNetworkTokensRestriction(
                operation='operation0',
                value=202,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            brand_variants=BrandVariantsRestriction(
                operation='operation4',
                value=[
                    'value8',
                    'value9'
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            counterparty_bank=CounterpartyBankRestriction(
                operation='operation2',
                value=[
                    BankIdentification(
                        country='country6',
                        identification='identification0',
                        identification_type=IdentificationType.BIC,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    BankIdentification(
                        country='country6',
                        identification='identification0',
                        identification_type=IdentificationType.BIC,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            counterparty_types=CounterpartyTypesRestriction(
                operation='operation8',
                value=[
                    Value.BALANCEACCOUNT
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            countries=CountriesRestriction(
                operation='operation0',
                value=[
                    'value4'
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mtype=Type14.MAXUSAGE,
        aggregation_level='aggregationLevel4',
        end_date='endDate4',
        id='id2',
        outcome_type=OutcomeType.ENFORCESCA,
        overrides_rule='overridesRule8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

