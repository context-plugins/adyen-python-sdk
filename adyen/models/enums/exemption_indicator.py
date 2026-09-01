from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExemptionIndicator(str, Enum):
    """Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied. Allowed
    values:
    * ``lowValue``
    * ``secureCorporate``
    * ``trustedBeneficiary``
    * ``transactionRiskAnalysis``"""

    LOW_VALUE = "lowValue"
    SECURE_CORPORATE = "secureCorporate"
    TRUSTED_BENEFICIARY = "trustedBeneficiary"
    TRANSACTION_RISK_ANALYSIS = "transactionRiskAnalysis"

    __str__ = str.__str__


ExemptionIndicatorOrStr: TypeAlias = Annotated[ExemptionIndicator | str, open_enum_validator(ExemptionIndicator)]
