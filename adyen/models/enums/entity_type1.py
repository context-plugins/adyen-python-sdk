from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntityType1(str, Enum):
    """The type of the entity the payout is processed for."""

    NATURAL_PERSON = "NaturalPerson"
    COMPANY = "Company"

    __str__ = str.__str__


EntityType1OrStr: TypeAlias = Annotated[EntityType1 | str, open_enum_validator(EntityType1)]
