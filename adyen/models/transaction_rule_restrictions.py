from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .active_network_tokens_restriction1 import ActiveNetworkTokensRestriction1, ActiveNetworkTokensRestriction1Dict
from .brand_variants_restriction1 import BrandVariantsRestriction1, BrandVariantsRestriction1Dict
from .counterparty_bank_restriction1 import CounterpartyBankRestriction1, CounterpartyBankRestriction1Dict
from .counterparty_types_restriction1 import CounterpartyTypesRestriction1, CounterpartyTypesRestriction1Dict
from .countries_restriction1 import CountriesRestriction1, CountriesRestriction1Dict
from .day_of_week_restriction1 import DayOfWeekRestriction1, DayOfWeekRestriction1Dict
from .different_currencies_restriction1 import DifferentCurrenciesRestriction1, DifferentCurrenciesRestriction1Dict
from .entry_modes_restriction1 import EntryModesRestriction1, EntryModesRestriction1Dict
from .international_transaction_restriction1 import (
    InternationalTransactionRestriction1,
    InternationalTransactionRestriction1Dict,
)
from .matching_transactions_restriction1 import MatchingTransactionsRestriction1, MatchingTransactionsRestriction1Dict
from .matching_values_restriction1 import MatchingValuesRestriction1, MatchingValuesRestriction1Dict
from .mccs_restriction1 import MccsRestriction1, MccsRestriction1Dict
from .merchant_names_restriction1 import MerchantNamesRestriction1, MerchantNamesRestriction1Dict
from .merchants_restriction1 import MerchantsRestriction1, MerchantsRestriction1Dict
from .processing_types_restriction1 import ProcessingTypesRestriction1, ProcessingTypesRestriction1Dict
from .risk_scores_restriction1 import RiskScoresRestriction1, RiskScoresRestriction1Dict
from .same_amount_restriction1 import SameAmountRestriction1, SameAmountRestriction1Dict
from .same_counterparty_restriction1 import SameCounterpartyRestriction1, SameCounterpartyRestriction1Dict
from .source_account_types_restriction1 import SourceAccountTypesRestriction1, SourceAccountTypesRestriction1Dict
from .time_of_day_restriction1 import TimeOfDayRestriction1, TimeOfDayRestriction1Dict
from .token_requestors_restriction1 import TokenRequestorsRestriction1, TokenRequestorsRestriction1Dict
from .total_amount_restriction1 import TotalAmountRestriction1, TotalAmountRestriction1Dict
from .wallet_provider_account_score_restriction2 import (
    WalletProviderAccountScoreRestriction2,
    WalletProviderAccountScoreRestriction2Dict,
)
from .wallet_provider_device_score2 import WalletProviderDeviceScore2, WalletProviderDeviceScore2Dict
from .wallet_provider_device_type2 import WalletProviderDeviceType2, WalletProviderDeviceType2Dict


class TransactionRuleRestrictions(SdkBaseModel):
    active_network_tokens: Optional[ActiveNetworkTokensRestriction1] = Field(default=UNSET, alias="activeNetworkTokens")
    """The total number of tokens that a card can have across different kinds of digital wallets on the user's phones,
    watches, or other wearables.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    brand_variants: Optional[BrandVariantsRestriction1] = Field(default=UNSET, alias="brandVariants")
    """List of card brand variants and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    counterparty_bank: Optional[CounterpartyBankRestriction1] = Field(default=UNSET, alias="counterpartyBank")
    """Contains a list of counterparty financial institutions and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**."""

    counterparty_types: Optional[CounterpartyTypesRestriction1] = Field(default=UNSET, alias="counterpartyTypes")
    """Contains a list of counterparty types and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **balanceAccount**
    - **bankAccount**
    - **card**
    - **transferInstrument**"""

    countries: Optional[CountriesRestriction1] = UNSET
    """List of countries and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    day_of_week: Optional[DayOfWeekRestriction1] = Field(default=UNSET, alias="dayOfWeek")
    """List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**."""

    different_currencies: Optional[DifferentCurrenciesRestriction1] = Field(default=UNSET, alias="differentCurrencies")
    """Compares the currency of the payment against the currency of the payment instrument, and specifies the operation.

    Supported operations: **equals**, **notEquals**."""

    entry_modes: Optional[EntryModesRestriction1] = Field(default=UNSET, alias="entryModes")
    """List of point-of-sale entry modes and the operation..

    Supported operations: **anyMatch**, **noneMatch**."""

    international_transaction: Optional[InternationalTransactionRestriction1] = Field(
        default=UNSET, alias="internationalTransaction"
    )
    """Indicates whether transaction is an international transaction and specifies the operation.

    Supported operations: **equals**, **notEquals**."""

    matching_transactions: Optional[MatchingTransactionsRestriction1] = Field(
        default=UNSET, alias="matchingTransactions"
    )
    """The number of transactions and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    matching_values: Optional[MatchingValuesRestriction1] = Field(default=UNSET, alias="matchingValues")
    """Checks if a user has recently made multiple transfers with the specified values.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operation: **allMatch**.

    Supported value inputs:
    - **merchantId** and **acquirerId**
    - **amount** and **currency**
    - **merchantName**."""

    mccs: Optional[MccsRestriction1] = UNSET
    """List of merchant category codes (MCCs) and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    merchant_names: Optional[MerchantNamesRestriction1] = Field(default=UNSET, alias="merchantNames")
    """List of names that will be compared to the merchant name according to the matching type.

    Supported operations: **anyMatch**, **noneMatch**."""

    merchants: Optional[MerchantsRestriction1] = UNSET
    """List of merchant ID and acquirer ID pairs, and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    processing_types: Optional[ProcessingTypesRestriction1] = Field(default=UNSET, alias="processingTypes")
    """List of processing types and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    risk_scores: Optional[RiskScoresRestriction1] = Field(default=UNSET, alias="riskScores")
    """Risk scores provided by specific sources. The same operation applies to all scores.

    Current sources available: **visa**, **mastercard**

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    same_amount_restriction: Optional[SameAmountRestriction1] = Field(default=UNSET, alias="sameAmountRestriction")
    """Checks if a user has recently sent the same amount of funds in multiple transfers.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operation: **equals**."""

    same_counterparty_restriction: Optional[SameCounterpartyRestriction1] = Field(
        default=UNSET, alias="sameCounterpartyRestriction"
    )
    """Checks if a user has recently made multiple transfers to the same counterparty.

    To use this restriction, you must:

    - Set the rule ``type`` to **velocity**.

    - Specify a time ``interval``.

    - Specify a number of ``matchingTransactions``.

    Supported operations: **equals**."""

    source_account_types: Optional[SourceAccountTypesRestriction1] = Field(default=UNSET, alias="sourceAccountTypes")
    """Contains a list of source account types and how they must be evaluated.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **balanceAccount**
    - **businessAccount**."""

    time_of_day: Optional[TimeOfDayRestriction1] = Field(default=UNSET, alias="timeOfDay")
    """A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**,
    **notEquals**."""

    token_requestors: Optional[TokenRequestorsRestriction1] = Field(default=UNSET, alias="tokenRequestors")
    """List of token requestor IDs and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    total_amount: Optional[TotalAmountRestriction1] = Field(default=UNSET, alias="totalAmount")
    """The total amount and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    wallet_provider_account_score: Optional[WalletProviderAccountScoreRestriction2] = Field(
        default=UNSET, alias="walletProviderAccountScore"
    )
    """Checks the wallet account score.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    wallet_provider_device_score: Optional[WalletProviderDeviceScore2] = Field(
        default=UNSET, alias="walletProviderDeviceScore"
    )
    """Wallet Provider Device Score and the operation.

    Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**,
    **lessThan**."""

    wallet_provider_device_type: Optional[WalletProviderDeviceType2] = Field(
        default=UNSET, alias="walletProviderDeviceType"
    )
    """Wallet Provider Device Type and the operation.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **MOBILE_PHONE**
    - **TABLET_OR_EREADER**
    - **WATCH_OR_WRISTBAND**
    - **WEARABLE**

    - **CARD**
    - **PC**
    - **OTHER**
    - **UNKNOWN**"""


class TransactionRuleRestrictionsDict(TypedDict):
    active_network_tokens: NotRequired[ActiveNetworkTokensRestriction1Dict]
    brand_variants: NotRequired[BrandVariantsRestriction1Dict]
    counterparty_bank: NotRequired[CounterpartyBankRestriction1Dict]
    counterparty_types: NotRequired[CounterpartyTypesRestriction1Dict]
    countries: NotRequired[CountriesRestriction1Dict]
    day_of_week: NotRequired[DayOfWeekRestriction1Dict]
    different_currencies: NotRequired[DifferentCurrenciesRestriction1Dict]
    entry_modes: NotRequired[EntryModesRestriction1Dict]
    international_transaction: NotRequired[InternationalTransactionRestriction1Dict]
    matching_transactions: NotRequired[MatchingTransactionsRestriction1Dict]
    matching_values: NotRequired[MatchingValuesRestriction1Dict]
    mccs: NotRequired[MccsRestriction1Dict]
    merchant_names: NotRequired[MerchantNamesRestriction1Dict]
    merchants: NotRequired[MerchantsRestriction1Dict]
    processing_types: NotRequired[ProcessingTypesRestriction1Dict]
    risk_scores: NotRequired[RiskScoresRestriction1Dict]
    same_amount_restriction: NotRequired[SameAmountRestriction1Dict]
    same_counterparty_restriction: NotRequired[SameCounterpartyRestriction1Dict]
    source_account_types: NotRequired[SourceAccountTypesRestriction1Dict]
    time_of_day: NotRequired[TimeOfDayRestriction1Dict]
    token_requestors: NotRequired[TokenRequestorsRestriction1Dict]
    total_amount: NotRequired[TotalAmountRestriction1Dict]
    wallet_provider_account_score: NotRequired[WalletProviderAccountScoreRestriction2Dict]
    wallet_provider_device_score: NotRequired[WalletProviderDeviceScore2Dict]
    wallet_provider_device_type: NotRequired[WalletProviderDeviceType2Dict]
