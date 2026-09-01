from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeCancel(str, Enum):
    """Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has
    been cancelled. For possible values, refer to `3D Secure API reference
    <https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata>`__."""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"
    _06 = "06"
    _07 = "07"

    __str__ = str.__str__


ChallengeCancelOrStr: TypeAlias = Annotated[ChallengeCancel | str, open_enum_validator(ChallengeCancel)]
