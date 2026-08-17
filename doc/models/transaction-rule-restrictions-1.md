
# Transaction Rule Restrictions 1

Contains one or more objects that define the [rule conditions](https://docs.adyen.com/issuing/transaction-rules#conditions). Each object must have a value and an operation which determines how the values must be evaluated.

For example, a `countries` object can have a list of country codes **["US", "CA"]** in the `value` field and **anyMatch** in the `operation` field.

## Structure

`TransactionRuleRestrictions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_network_tokens` | [`ActiveNetworkTokensRestriction1`](../../doc/models/active-network-tokens-restriction-1.md) | Optional | The total number of tokens that a card can have across different kinds of digital wallets on the user's phones, watches, or other wearables.<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `brand_variants` | [`BrandVariantsRestriction1`](../../doc/models/brand-variants-restriction-1.md) | Optional | List of card brand variants and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `counterparty_bank` | [`CounterpartyBankRestriction1`](../../doc/models/counterparty-bank-restriction-1.md) | Optional | Contains a list of counterparty financial institutions and how they must be evaluated.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `counterparty_types` | [`CounterpartyTypesRestriction1`](../../doc/models/counterparty-types-restriction-1.md) | Optional | Contains a list of counterparty types and how they must be evaluated.<br><br>Supported operations: **anyMatch**, **noneMatch**.<br><br>Supported value inputs:<br><br>- **balanceAccount**<br>- **bankAccount**<br>- **card**<br>- **transferInstrument** |
| `countries` | [`CountriesRestriction1`](../../doc/models/countries-restriction-1.md) | Optional | List of countries and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `day_of_week` | [`DayOfWeekRestriction1`](../../doc/models/day-of-week-restriction-1.md) | Optional | List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**. |
| `different_currencies` | [`DifferentCurrenciesRestriction1`](../../doc/models/different-currencies-restriction-1.md) | Optional | Compares the currency of the payment against the currency of the payment instrument, and specifies the operation.<br><br>Supported operations: **equals**, **notEquals**. |
| `entry_modes` | [`EntryModesRestriction1`](../../doc/models/entry-modes-restriction-1.md) | Optional | List of point-of-sale entry modes and the operation..<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `international_transaction` | [`InternationalTransactionRestriction1`](../../doc/models/international-transaction-restriction-1.md) | Optional | Indicates whether transaction is an international transaction and specifies the operation.<br><br>Supported operations: **equals**, **notEquals**. |
| `matching_transactions` | [`MatchingTransactionsRestriction1`](../../doc/models/matching-transactions-restriction-1.md) | Optional | The number of transactions and the operation.<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `matching_values` | [`MatchingValuesRestriction1`](../../doc/models/matching-values-restriction-1.md) | Optional | Checks if a user has recently made multiple transfers with the specified values.<br><br>To use this restriction, you must:<br><br>- Set the rule `type` to **velocity**.<br><br>- Specify a time `interval`.<br><br>- Specify a number of `matchingTransactions`.<br><br>Supported operation: **allMatch**.<br><br>Supported value inputs:<br><br>- **merchantId** and **acquirerId**<br>- **amount** and **currency**<br>- **merchantName**. |
| `mccs` | [`MccsRestriction1`](../../doc/models/mccs-restriction-1.md) | Optional | List of merchant category codes (MCCs) and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `merchant_names` | [`MerchantNamesRestriction1`](../../doc/models/merchant-names-restriction-1.md) | Optional | List of names that will be compared to the merchant name according to the matching type.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `merchants` | [`MerchantsRestriction1`](../../doc/models/merchants-restriction-1.md) | Optional | List of merchant ID and acquirer ID pairs, and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `processing_types` | [`ProcessingTypesRestriction1`](../../doc/models/processing-types-restriction-1.md) | Optional | List of processing types and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `risk_scores` | [`RiskScoresRestriction1`](../../doc/models/risk-scores-restriction-1.md) | Optional | Risk scores provided by specific sources. The same operation applies to all scores.<br><br>Current sources available: **visa**, **mastercard**<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `same_amount_restriction` | [`SameAmountRestriction1`](../../doc/models/same-amount-restriction-1.md) | Optional | Checks if a user has recently sent the same amount of funds in multiple transfers.<br><br>To use this restriction, you must:<br><br>- Set the rule `type` to **velocity**.<br><br>- Specify a time `interval`.<br><br>- Specify a number of `matchingTransactions`.<br><br>Supported operation: **equals**. |
| `same_counterparty_restriction` | [`SameCounterpartyRestriction1`](../../doc/models/same-counterparty-restriction-1.md) | Optional | Checks if a user has recently made multiple transfers to the same counterparty.<br><br>To use this restriction, you must:<br><br>- Set the rule `type` to **velocity**.<br><br>- Specify a time `interval`.<br><br>- Specify a number of `matchingTransactions`.<br><br>Supported operations: **equals**. |
| `source_account_types` | [`SourceAccountTypesRestriction1`](../../doc/models/source-account-types-restriction-1.md) | Optional | Contains a list of source account types and how they must be evaluated.<br><br>Supported operations: **anyMatch**, **noneMatch**.<br><br>Supported value inputs:<br><br>- **balanceAccount**<br>- **businessAccount**. |
| `time_of_day` | [`TimeOfDayRestriction1`](../../doc/models/time-of-day-restriction-1.md) | Optional | A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**, **notEquals**. |
| `token_requestors` | [`TokenRequestorsRestriction1`](../../doc/models/token-requestors-restriction-1.md) | Optional | List of token requestor IDs and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**. |
| `total_amount` | [`TotalAmountRestriction1`](../../doc/models/total-amount-restriction-1.md) | Optional | The total amount and the operation.<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `wallet_provider_account_score` | [`WalletProviderAccountScoreRestriction2`](../../doc/models/wallet-provider-account-score-restriction-2.md) | Optional | Checks the wallet account score.<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `wallet_provider_device_score` | [`WalletProviderDeviceScore2`](../../doc/models/wallet-provider-device-score-2.md) | Optional | Wallet Provider Device Score and the operation.<br><br>Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
| `wallet_provider_device_type` | [`WalletProviderDeviceType2`](../../doc/models/wallet-provider-device-type-2.md) | Optional | Wallet Provider Device Type and the operation.<br><br>Supported operations: **anyMatch**, **noneMatch**.<br><br>Supported value inputs:<br><br>- **MOBILE_PHONE**<br><br>- **TABLET_OR_EREADER**<br><br>- **WATCH_OR_WRISTBAND**<br><br>- **WEARABLE**<br><br>- **CARD**<br><br>- **PC**<br><br>- **OTHER**<br><br>- **UNKNOWN** |

## Example

```python
from adyen.models.active_network_tokens_restriction_1 import ActiveNetworkTokensRestriction1
from adyen.models.bank_identification import BankIdentification
from adyen.models.brand_variants_restriction_1 import BrandVariantsRestriction1
from adyen.models.counterparty_bank_restriction_1 import CounterpartyBankRestriction1
from adyen.models.counterparty_types_restriction_1 import CounterpartyTypesRestriction1
from adyen.models.countries_restriction_1 import CountriesRestriction1
from adyen.models.identification_type_enum import IdentificationTypeEnum
from adyen.models.transaction_rule_restrictions_1 import TransactionRuleRestrictions1
from adyen.models.value_enum import ValueEnum

transaction_rule_restrictions_1 = TransactionRuleRestrictions1(
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
)
```

