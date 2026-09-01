from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThreeDsreqPriorAuthMethod(str, Enum):
    """Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values:
    * **01** — Frictionless authentication occurred by ACS.
    * **02** — Cardholder challenge occurred by ACS.
    * **03** — AVS verified.
    * **04** — Other issuer methods."""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"

    __str__ = str.__str__


ThreeDsreqPriorAuthMethodOrStr: TypeAlias = Annotated[
    ThreeDsreqPriorAuthMethod | str, open_enum_validator(ThreeDsreqPriorAuthMethod)
]
