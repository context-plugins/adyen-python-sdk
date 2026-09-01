from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FraudRiskLevel(str, Enum):
    """The risk level of the transaction as classified by the `machine learning
    <https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules/>`__ fraud risk rule. The
    risk level indicates the likelihood that a transaction will result in a fraudulent dispute. Possible values:
    * veryLow
    * low
    * medium
    * high
    * veryHigh"""

    VERY_LOW = "veryLow"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "veryHigh"

    __str__ = str.__str__


FraudRiskLevelOrStr: TypeAlias = Annotated[FraudRiskLevel | str, open_enum_validator(FraudRiskLevel)]
