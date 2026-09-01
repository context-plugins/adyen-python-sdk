from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TermsOfServiceType(str, Enum):
    ADYEN_ACCOUNT = "adyenAccount"
    ADYEN_CAPITAL = "adyenCapital"
    ADYEN_CARD = "adyenCard"
    ADYEN_CHARGE_CARD = "adyenChargeCard"
    ADYEN_FOR_PLATFORMS_ADVANCED = "adyenForPlatformsAdvanced"
    ADYEN_FOR_PLATFORMS_MANAGE = "adyenForPlatformsManage"
    ADYEN_FRANCHISEE = "adyenFranchisee"
    ADYEN_ISSUING = "adyenIssuing"
    ADYEN_PCCR = "adyenPccr"
    KYC_ON_INVITE = "kycOnInvite"

    __str__ = str.__str__


TermsOfServiceTypeOrStr: TypeAlias = Annotated[TermsOfServiceType | str, open_enum_validator(TermsOfServiceType)]
