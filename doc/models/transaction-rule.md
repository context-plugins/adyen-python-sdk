
# Transaction Rule

## Structure

`TransactionRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregation_level` | `str` | Optional | The level at which data must be accumulated, used in rules with `type` **velocity** or **maxUsage**. The level must be the [same or lower in hierarchy](https://docs.adyen.com/issuing/transaction-rules#accumulate-data) than the `entityKey`.<br><br>If not provided, by default, the rule will accumulate data at the **paymentInstrument** level.<br><br>Possible values: **paymentInstrument**, **paymentInstrumentGroup**, **balanceAccount**, **accountHolder**, **balancePlatform**. |
| `description` | `str` | Required | Your description for the transaction rule.<br><br>**Constraints**: *Maximum Length*: `300` |
| `end_date` | `str` | Optional | The date when the rule will stop being evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.<br><br>If not provided, the rule will be evaluated until the rule status is set to **inactive**. |
| `entity_key` | [`TransactionRuleEntityKey2`](../../doc/models/transaction-rule-entity-key-2.md) | Required | The type and unique identifier of the resource to which the rule applies. |
| `id` | `str` | Optional | The unique identifier of the transaction rule. |
| `interval` | [`TransactionRuleInterval1`](../../doc/models/transaction-rule-interval-1.md) | Required | The [time interval](https://docs.adyen.com/issuing/transaction-rules#time-intervals) when the rule conditions apply. |
| `outcome_type` | [`OutcomeTypeEnum`](../../doc/models/outcome-type-enum.md) | Optional | The [outcome](https://docs.adyen.com/issuing/transaction-rules#outcome) that will be applied when a transaction meets the conditions of the rule.<br><br>Possible values:<br><br>* **hardBlock** (default): the transaction is declined.<br><br>* **scoreBased**: the transaction is assigned the `score` you specified. Adyen calculates the total score and if it exceeds 100, the transaction is declined. This value is not allowed when `requestType` is **bankTransfer**.<br><br>* **enforceSCA**: your user is prompted to verify their identity using [3D Secure authentication](https://docs.adyen.com/issuing/3d-secure/). If the authentication fails or times out, the transaction is declined. This value is only allowed when `requestType` is **authentication**. |
| `overrides_rule` | `str` | Optional | The `id` of the transaction rule you want to override or skip for the specified `entityKey`. |
| `purpose` | [`PurposeEnum`](../../doc/models/purpose-enum.md) | Optional | Specifies the reason for creating the rule.<br><br>Possible values:<br><br>* **fraud**: the rule is created to regulate fraudulent activity.<br>* **policy**: the rule is created to ensure that the transaction adheres to your business' policies. For example, if your business has policies about the Merchant Category Codes (MCCs) allowed on a transaction, you can create a rule to block transactions that have specific MCCs. |
| `reference` | `str` | Required | Your reference for the transaction rule.<br><br>**Constraints**: *Maximum Length*: `150` |
| `request_type` | [`RequestTypeEnum`](../../doc/models/request-type-enum.md) | Optional | Indicates the type of request to which the rule applies. If not provided, by default, this is set to **authorization**.<br><br>Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**. |
| `rule_restrictions` | [`TransactionRuleRestrictions1`](../../doc/models/transaction-rule-restrictions-1.md) | Required | Contains one or more objects that define the [rule conditions](https://docs.adyen.com/issuing/transaction-rules#conditions). Each object must have a value and an operation which determines how the values must be evaluated.<br><br>For example, a `countries` object can have a list of country codes **["US", "CA"]** in the `value` field and **anyMatch** in the `operation` field. |
| `score` | `int` | Optional | A positive or negative score applied to the transaction if it meets the conditions of the rule. Required when `outcomeType` is **scoreBased**.  The value must be between **-100** and **100**. |
| `start_date` | `str` | Optional | The date when the rule will start to be evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.<br><br>If not provided when creating a transaction rule, the `startDate` is set to the date when the rule status is set to **active**. |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Optional | The status of the transaction rule. If you provide a `startDate` in the request, the rule is automatically created<br>with an **active** status.<br><br>Possible values: **active**, **inactive**. |
| `mtype` | [`Type141Enum`](../../doc/models/type-141-enum.md) | Required | The [type of rule](https://docs.adyen.com/issuing/transaction-rules#rule-types), which defines if a rule blocks transactions based on individual characteristics or accumulates data.<br><br>Possible values:<br><br>* **blockList**: decline a transaction when the conditions are met.<br>* **maxUsage**: add the amount or number of transactions for the lifetime of a payment instrument, and then decline a transaction when the specified limits are met.<br>* **velocity**: add the amount or number of transactions based on a specified time interval, and then decline a transaction when the specified limits are met.<br>* **bypass**: bypass or skip a rule for the specified `entityKey`. Transactions processed to that entity are no longer evaluated by the bypassed rule.  You must provide the `id` of the rule to bypass in `overridesRule` and leave the `ruleRestrictions` object empty. |

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
from adyen.models.type_131_enum import Type131Enum
from adyen.models.type_141_enum import Type141Enum
from adyen.models.unit_enum import UnitEnum
from adyen.models.value_enum import ValueEnum

transaction_rule = TransactionRule(
    description='description2',
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
    reference='reference8',
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
    mtype=Type141Enum.BYPASS,
    aggregation_level='aggregationLevel4',
    end_date='endDate4',
    id='id2',
    outcome_type=OutcomeTypeEnum.SCOREBASED,
    overrides_rule='overridesRule8'
)
```

