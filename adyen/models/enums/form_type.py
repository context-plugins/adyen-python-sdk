from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FormType(str, Enum):
    US1099K = "US1099k"
    US1099NEC = "US1099nec"

    __str__ = str.__str__


FormTypeOrStr: TypeAlias = Annotated[FormType | str, open_enum_validator(FormType)]
