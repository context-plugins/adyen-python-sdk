
# Transaction Rule

*This model accepts additional fields of type Any.*

## Structure

`TransactionRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregation_level` | `str` | Optional | The level at which data must be accumulated, used in rules with `type` **velocity** or **maxUsage**. The level must be the [same or lower in hierarchy](https://docs.adyen.com/issuing/transaction-rules#accumulate-data) than the `entityKey`.<br><br>If not provided, by default, the rule will accumulate data at the **paymentInstrument** level.<br><br>Possible values: **paymentInstrument**, **paymentInstrumentGroup**, **balanceAccount**, **accountHolder**, **balancePlatform**. |
| `description` | `str` | Required | Your description for the transaction rule.<br><br>**Constraints**: *Maximum Length*: `300` |
| `end_date` | `str` | Optional | The date when the rule will stop being evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.<br><br>If not provided, the rule will be evaluated until the rule status is set to **inactive**. |
| `entity_key` | [`TransactionRuleEntityKey`](../../doc/models/transaction-rule-entity-key.md) | Required | - |
| `id` | `str` | Optional | The unique identifier of the transaction rule. |
| `interval` | [`TransactionRuleInterval`](../../doc/models/transaction-rule-interval.md) | Required | - |
| `outcome_type` | [`OutcomeType`](../../doc/models/outcome-type.md) | Optional | - |
| `overrides_rule` | `str` | Optional | The `id` of the transaction rule you want to override or skip for the specified `entityKey`. |
| `purpose` | [`Purpose`](../../doc/models/purpose.md) | Optional | - |
| `reference` | `str` | Required | Your reference for the transaction rule.<br><br>**Constraints**: *Maximum Length*: `150` |
| `request_type` | [`RequestType`](../../doc/models/request-type.md) | Optional | - |
| `rule_restrictions` | [`TransactionRuleRestrictions`](../../doc/models/transaction-rule-restrictions.md) | Required | - |
| `score` | `int` | Optional | A positive or negative score applied to the transaction if it meets the conditions of the rule. Required when `outcomeType` is **scoreBased**.  The value must be between **-100** and **100**. |
| `start_date` | `str` | Optional | The date when the rule will start to be evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.<br><br>If not provided when creating a transaction rule, the `startDate` is set to the date when the rule status is set to **active**. |
| `status` | [`Status14`](../../doc/models/status-14.md) | Optional | - |
| `mtype` | [`Type14`](../../doc/models/type-14.md) | Required | - |
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
from adyen.models.transaction_rule_restrictions import TransactionRuleRestrictions
from adyen.models.type_13 import Type13
from adyen.models.type_14 import Type14
from adyen.models.unit import Unit
from adyen.models.value import Value

transaction_rule = TransactionRule(
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
    reference='reference8',
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
    mtype=Type14.BYPASS,
    aggregation_level='aggregationLevel4',
    end_date='endDate4',
    id='id2',
    outcome_type=OutcomeType.SCOREBASED,
    overrides_rule='overridesRule8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

