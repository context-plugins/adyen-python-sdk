from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Namespace(str, Enum):
    """The namespace that corresponds to the reason code.

    Possible values:
    * **ukFpsRejectionCode**
    * **ukFpsReturnReasonCode**
    * **usAchReturnReasonCode**
    * **iso8583ResponseCode**"""

    ISO8583_RESPONSE_CODE = "iso8583ResponseCode"
    UK_FPS_REJECTION_CODE = "ukFpsRejectionCode"
    UK_FPS_RETURN_REASON_CODE = "ukFpsReturnReasonCode"
    US_ACH_RETURN_REASON_CODE = "usAchReturnReasonCode"

    __str__ = str.__str__


NamespaceOrStr: TypeAlias = Annotated[Namespace | str, open_enum_validator(Namespace)]
