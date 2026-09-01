from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DirectoryResponse(str, Enum):
    """In 3D Secure 2, this is the ``transStatus`` from the ``ARes``."""

    A = "A"
    C = "C"
    D = "D"
    I_ = "I"
    N = "N"
    R = "R"
    U = "U"
    Y = "Y"

    __str__ = str.__str__


DirectoryResponseOrStr: TypeAlias = Annotated[DirectoryResponse | str, open_enum_validator(DirectoryResponse)]
