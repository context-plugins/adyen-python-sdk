from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutcomeType(str, Enum):
    """The `outcome <https://docs.adyen.com/issuing/transaction-rules#outcome>`__ that will be applied when a
    transaction meets the conditions of the rule.

    Possible values:
    * **hardBlock** (default): the transaction is declined.
    * **scoreBased**: the transaction is assigned the ``score`` you specified. Adyen calculates the total score and if
        it exceeds 100, the transaction is declined. This value is not allowed when ``requestType`` is **bankTransfer**.

    * **enforceSCA**: your user is prompted to verify their identity using `3D Secure authentication
        <https://docs.adyen.com/issuing/3d-secure/>`__. If the authentication fails or times out, the transaction is
        declined. This value is only allowed when ``requestType`` is **authentication**."""

    ENFORCE_SCA = "enforceSCA"
    HARD_BLOCK = "hardBlock"
    SCORE_BASED = "scoreBased"
    TIMED_BLOCK = "timedBlock"

    __str__ = str.__str__


OutcomeTypeOrStr: TypeAlias = Annotated[OutcomeType | str, open_enum_validator(OutcomeType)]
