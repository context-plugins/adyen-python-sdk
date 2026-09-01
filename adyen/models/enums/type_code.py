from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TypeCode(str, Enum):
    """Possible values:
    * **Personal**
    * **Company**"""

    PERSONAL = "Personal"
    COMPANY = "Company"

    __str__ = str.__str__


TypeCodeOrStr: TypeAlias = Annotated[TypeCode | str, open_enum_validator(TypeCode)]
