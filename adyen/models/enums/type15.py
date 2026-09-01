from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type15(str, Enum):
    """The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**,
    **VISA**.

    To delete an existing entry for a document ``type``, send only the ``type`` field in your request."""

    DRIVINGLICENSE = "DRIVINGLICENSE"
    ID = "ID"
    PASSPORT = "PASSPORT"
    SOCIALSECURITY = "SOCIALSECURITY"
    VISA = "VISA"

    __str__ = str.__str__


Type15OrStr: TypeAlias = Annotated[Type15 | str, open_enum_validator(Type15)]
