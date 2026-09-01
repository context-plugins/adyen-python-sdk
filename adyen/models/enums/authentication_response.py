from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticationResponse(str, Enum):
    """In 3D Secure 2, this is the ``transStatus`` from the challenge result. If the transaction was frictionless, omit
    this parameter."""

    Y = "Y"
    N = "N"
    U = "U"
    A = "A"

    __str__ = str.__str__


AuthenticationResponseOrStr: TypeAlias = Annotated[
    AuthenticationResponse | str, open_enum_validator(AuthenticationResponse)
]
