
# Transaction Rule Restrictions 1

Contains one or more objects that define the [rule conditions](https://docs.adyen.com/issuing/transaction-rules#conditions). Each object must have a value and an operation which determines how the values must be evaluated.

For example, a `countries` object can have a list of country codes **["US", "CA"]** in the `value` field and **anyMatch** in the `operation` field.

*This model accepts additional fields of type Any.*

## Structure

`TransactionRuleRestrictions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_network_tokens` | [`ActiveNetworkTokensRestriction`](../../doc/models/active-network-tokens-restriction.md) | Optional | - |
| `brand_variants` | [`BrandVariantsRestriction`](../../doc/models/brand-variants-restriction.md) | Optional | - |
| `counterparty_bank` | [`CounterpartyBankRestriction`](../../doc/models/counterparty-bank-restriction.md) | Optional | - |
| `counterparty_types` | [`CounterpartyTypesRestriction`](../../doc/models/counterparty-types-restriction.md) | Optional | - |
| `countries` | [`CountriesRestriction`](../../doc/models/countries-restriction.md) | Optional | - |
| `day_of_week` | [`DayOfWeekRestriction`](../../doc/models/day-of-week-restriction.md) | Optional | - |
| `different_currencies` | [`DifferentCurrenciesRestriction`](../../doc/models/different-currencies-restriction.md) | Optional | - |
| `entry_modes` | [`EntryModesRestriction`](../../doc/models/entry-modes-restriction.md) | Optional | - |
| `international_transaction` | [`InternationalTransactionRestriction`](../../doc/models/international-transaction-restriction.md) | Optional | - |
| `matching_transactions` | [`MatchingTransactionsRestriction`](../../doc/models/matching-transactions-restriction.md) | Optional | - |
| `matching_values` | [`MatchingValuesRestriction`](../../doc/models/matching-values-restriction.md) | Optional | - |
| `mccs` | [`MccsRestriction`](../../doc/models/mccs-restriction.md) | Optional | - |
| `merchant_names` | [`MerchantNamesRestriction`](../../doc/models/merchant-names-restriction.md) | Optional | - |
| `merchants` | [`MerchantsRestriction`](../../doc/models/merchants-restriction.md) | Optional | - |
| `processing_types` | [`ProcessingTypesRestriction`](../../doc/models/processing-types-restriction.md) | Optional | - |
| `risk_scores` | [`RiskScoresRestriction`](../../doc/models/risk-scores-restriction.md) | Optional | - |
| `same_amount_restriction` | [`SameAmountRestriction`](../../doc/models/same-amount-restriction.md) | Optional | - |
| `same_counterparty_restriction` | [`SameAmountRestriction`](../../doc/models/same-amount-restriction.md) | Optional | - |
| `source_account_types` | [`SourceAccountTypesRestriction`](../../doc/models/source-account-types-restriction.md) | Optional | - |
| `time_of_day` | [`TimeOfDayRestriction`](../../doc/models/time-of-day-restriction.md) | Optional | - |
| `token_requestors` | [`TokenRequestorsRestriction`](../../doc/models/token-requestors-restriction.md) | Optional | - |
| `total_amount` | [`TotalAmountRestriction`](../../doc/models/total-amount-restriction.md) | Optional | - |
| `wallet_provider_account_score` | [`WalletProviderAccountScoreRestriction`](../../doc/models/wallet-provider-account-score-restriction.md) | Optional | - |
| `wallet_provider_device_score` | [`WalletProviderAccountScoreRestriction`](../../doc/models/wallet-provider-account-score-restriction.md) | Optional | - |
| `wallet_provider_device_type` | [`WalletProviderDeviceType`](../../doc/models/wallet-provider-device-type.md) | Optional | - |
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
from adyen.models.identification_type import IdentificationType
from adyen.models.transaction_rule_restrictions_1 import TransactionRuleRestrictions1
from adyen.models.value import Value

transaction_rule_restrictions_1 = TransactionRuleRestrictions1(
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
)
```

