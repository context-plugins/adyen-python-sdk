from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type64(str, Enum):
    """The type of Terms of Service.

    Possible values:
    * **adyenForPlatformsManage**
    * **adyenIssuing**
    * **adyenForPlatformsAdvanced**
    * **adyenCapital**
    * **adyenAccount**
    * **adyenCard**
    * **adyenFranchisee**
    * **adyenPccr**
    * **adyenChargeCard**
    * **kycOnInvite**"""

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


Type64OrStr: TypeAlias = Annotated[Type64 | str, open_enum_validator(Type64)]
