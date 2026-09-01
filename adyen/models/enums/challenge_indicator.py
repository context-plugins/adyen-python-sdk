from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChallengeIndicator(str, Enum):
    """Possibility to specify a preference for receiving a challenge from the issuer. Allowed values:
    * ``noPreference``
    * ``requestNoChallenge``
    * ``requestChallenge``
    * ``requestChallengeAsMandate``"""

    NO_PREFERENCE = "noPreference"
    REQUEST_NO_CHALLENGE = "requestNoChallenge"
    REQUEST_CHALLENGE = "requestChallenge"
    REQUEST_CHALLENGE_AS_MANDATE = "requestChallengeAsMandate"

    __str__ = str.__str__


ChallengeIndicatorOrStr: TypeAlias = Annotated[ChallengeIndicator | str, open_enum_validator(ChallengeIndicator)]
