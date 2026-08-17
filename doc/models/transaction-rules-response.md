
# Transaction Rules Response

## Structure

`TransactionRulesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_rules` | [`List[TransactionRule]`](../../doc/models/transaction-rule.md) | Optional | List of transaction rules. |

## Example

```python
from adyen.models.active_network_tokens_restriction_1 import ActiveNetworkTokensRestriction1
from adyen.models.bank_identification import BankIdentification
from adyen.models.brand_variants_restriction_1 import BrandVariantsRestriction1
from adyen.models.counterparty_bank_restriction_1 import CounterpartyBankRestriction1
from adyen.models.counterparty_types_restriction_1 import CounterpartyTypesRestriction1
from adyen.models.countries_restriction_1 import CountriesRestriction1
from adyen.models.day_of_week_enum import DayOfWeekEnum
from adyen.models.duration_1 import Duration1
from adyen.models.identification_type_enum import IdentificationTypeEnum
from adyen.models.outcome_type_enum import OutcomeTypeEnum
from adyen.models.transaction_rule import TransactionRule
from adyen.models.transaction_rule_entity_key_2 import TransactionRuleEntityKey2
from adyen.models.transaction_rule_interval_1 import TransactionRuleInterval1
from adyen.models.transaction_rule_restrictions_1 import TransactionRuleRestrictions1
from adyen.models.transaction_rules_response import TransactionRulesResponse
from adyen.models.type_131_enum import Type131Enum
from adyen.models.type_141_enum import Type141Enum
from adyen.models.unit_enum import UnitEnum
from adyen.models.value_enum import ValueEnum

transaction_rules_response = TransactionRulesResponse(
    transaction_rules=[
        TransactionRule(
            description='description8',
            entity_key=TransactionRuleEntityKey2(
                entity_reference='entityReference2',
                entity_type='entityType0'
            ),
            interval=TransactionRuleInterval1(
                mtype=Type131Enum.MONTHLY,
                day_of_month=178,
                day_of_week=DayOfWeekEnum.SATURDAY,
                duration=Duration1(
                    unit=UnitEnum.WEEKS,
                    value=176
                ),
                time_of_day='timeOfDay2',
                time_zone='timeZone4'
            ),
            reference='reference4',
            rule_restrictions=TransactionRuleRestrictions1(
                active_network_tokens=ActiveNetworkTokensRestriction1(
                    operation='operation0',
                    value=202
                ),
                brand_variants=BrandVariantsRestriction1(
                    operation='operation4',
                    value=[
                        'value8',
                        'value9'
                    ]
                ),
                counterparty_bank=CounterpartyBankRestriction1(
                    operation='operation2',
                    value=[
                        BankIdentification(
                            country='country6',
                            identification='identification0',
                            identification_type=IdentificationTypeEnum.BIC
                        ),
                        BankIdentification(
                            country='country6',
                            identification='identification0',
                            identification_type=IdentificationTypeEnum.BIC
                        )
                    ]
                ),
                counterparty_types=CounterpartyTypesRestriction1(
                    operation='operation8',
                    value=[
                        ValueEnum.BALANCEACCOUNT
                    ]
                ),
                countries=CountriesRestriction1(
                    operation='operation0',
                    value=[
                        'value4'
                    ]
                )
            ),
            mtype=Type141Enum.MAXUSAGE,
            aggregation_level='aggregationLevel0',
            end_date='endDate0',
            id='id8',
            outcome_type=OutcomeTypeEnum.SCOREBASED,
            overrides_rule='overridesRule4'
        )
    ]
)
```

