from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type110(str, Enum):
    """The `type of legal arrangement
    <https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements#types-of-legal-arrangements>`__.

    Possible values:

    - **Association**

    - **Partnership**

    - **SoleProprietorship**

    - **Trust**"""

    ASSOCIATION = "Association"
    PARTNERSHIP = "Partnership"
    SOLE_PROPRIETORSHIP = "SoleProprietorship"
    TRUST = "Trust"

    __str__ = str.__str__


Type110OrStr: TypeAlias = Annotated[Type110 | str, open_enum_validator(Type110)]
