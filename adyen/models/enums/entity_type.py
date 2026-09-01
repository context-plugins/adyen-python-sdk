from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntityType(str, Enum):
    """The type of the entity the payment is processed for."""

    NATURAL_PERSON = "NaturalPerson"
    COMPANY_NAME = "CompanyName"

    __str__ = str.__str__


EntityTypeOrStr: TypeAlias = Annotated[EntityType | str, open_enum_validator(EntityType)]
