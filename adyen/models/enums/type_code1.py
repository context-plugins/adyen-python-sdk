from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TypeCode1(str, Enum):
    """Type of bank check. Possible values:
    * **Company**
    * **Personal**"""

    PERSONAL = "Personal"
    COMPANY = "Company"

    __str__ = str.__str__


TypeCode1OrStr: TypeAlias = Annotated[TypeCode1 | str, open_enum_validator(TypeCode1)]
