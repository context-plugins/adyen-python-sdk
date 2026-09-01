from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalForm(str, Enum):
    """The form of legal arrangement. Required if ``type`` is **Trust** or **Partnership**.

    The possible values depend on the ``type``.

    - For ``type`` **Trust**: **CashManagementTrust**, **CorporateUnitTrust**, **DeceasedEstate**,
        **DiscretionaryInvestmentTrust**, **DiscretionaryServicesManagementTrust**, **DiscretionaryTradingTrust**,
        **FirstHomeSaverAccountsTrust**, **FixedTrust**, **FixedUnitTrust**, **HybridTrust**, **ListedPublicUnitTrust**,
        **OtherTrust**, **PooledSuperannuationTrust**, **PublicTradingTrust**, or **UnlistedPublicUnitTrust**.

    - For ``type`` **Partnership**: **LimitedPartnership**, **FamilyPartnership**, or **OtherPartnership**"""

    CASH_MANAGEMENT_TRUST = "CashManagementTrust"
    CORPORATE_UNIT_TRUST = "CorporateUnitTrust"
    DECEASED_ESTATE = "DeceasedEstate"
    DISCRETIONARY_INVESTMENT_TRUST = "DiscretionaryInvestmentTrust"
    DISCRETIONARY_SERVICES_MANAGEMENT_TRUST = "DiscretionaryServicesManagementTrust"
    DISCRETIONARY_TRADING_TRUST = "DiscretionaryTradingTrust"
    FIRST_HOME_SAVER_ACCOUNTS_TRUST = "FirstHomeSaverAccountsTrust"
    FIXED_TRUST = "FixedTrust"
    FIXED_UNIT_TRUST = "FixedUnitTrust"
    HYBRID_TRUST = "HybridTrust"
    LISTED_PUBLIC_UNIT_TRUST = "ListedPublicUnitTrust"
    OTHER_TRUST = "OtherTrust"
    POOLED_SUPERANNUATION_TRUST = "PooledSuperannuationTrust"
    PUBLIC_TRADING_TRUST = "PublicTradingTrust"
    UNLISTED_PUBLIC_UNIT_TRUST = "UnlistedPublicUnitTrust"
    LIMITED_PARTNERSHIP = "LimitedPartnership"
    FAMILY_PARTNERSHIP = "FamilyPartnership"
    OTHER_PARTNERSHIP = "OtherPartnership"

    __str__ = str.__str__


LegalFormOrStr: TypeAlias = Annotated[LegalForm | str, open_enum_validator(LegalForm)]
