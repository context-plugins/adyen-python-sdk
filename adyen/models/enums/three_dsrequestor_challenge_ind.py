from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThreeDsrequestorChallengeInd(str, Enum):
    """Indicates whether a challenge is requested for this transaction. Possible values:
    * **01** — No preference
    * **02** — No challenge requested
    * **03** — Challenge requested (3DS Requestor preference)
    * **04** — Challenge requested (Mandate)
    * **05** — No challenge (transactional risk analysis is already performed)
    * **06** — Data Only"""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"
    _06 = "06"

    __str__ = str.__str__


ThreeDsrequestorChallengeIndOrStr: TypeAlias = Annotated[
    ThreeDsrequestorChallengeInd | str, open_enum_validator(ThreeDsrequestorChallengeInd)
]
