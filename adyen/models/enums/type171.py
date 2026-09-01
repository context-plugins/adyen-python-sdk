from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type171(str, Enum):
    """Type of trust.

    See possible values for trusts in `Australia
    <https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-australia>`__ and `New
    Zealand
    <https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-new-zealand>`__."""

    BUSINESS_TRUST = "businessTrust"
    CASH_MANAGEMENT_TRUST = "cashManagementTrust"
    CHARITABLE_TRUST = "charitableTrust"
    CORPORATE_UNIT_TRUST = "corporateUnitTrust"
    DECEASED_ESTATE = "deceasedEstate"
    DISCRETIONARY_TRUST = "discretionaryTrust"
    DISCRETIONARY_INVESTMENT_TRUST = "discretionaryInvestmentTrust"
    DISCRETIONARY_SERVICES_MANAGEMENT_TRUST = "discretionaryServicesManagementTrust"
    DISCRETIONARY_TRADING_TRUST = "discretionaryTradingTrust"
    FAMILY_TRUST = "familyTrust"
    FIRST_HOME_SAVER_ACCOUNTS_TRUST = "firstHomeSaverAccountsTrust"
    FIXED_TRUST = "fixedTrust"
    FIXED_UNIT_TRUST = "fixedUnitTrust"
    HYBRID_TRUST = "hybridTrust"
    LISTED_PUBLIC_UNIT_TRUST = "listedPublicUnitTrust"
    OTHER_TRUST = "otherTrust"
    POOLED_SUPERANNUATION_TRUST = "pooledSuperannuationTrust"
    PUBLIC_TRADING_TRUST = "publicTradingTrust"
    UNLISTED_PUBLIC_UNIT_TRUST = "unlistedPublicUnitTrust"

    __str__ = str.__str__


Type171OrStr: TypeAlias = Annotated[Type171 | str, open_enum_validator(Type171)]
