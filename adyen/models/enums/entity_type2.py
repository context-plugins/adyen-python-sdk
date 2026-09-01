from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntityType2(str, Enum):
    """The type of the entity the payout is processed for.

    Allowed values:
    * NaturalPerson
    * Company
    > This field is required to update the existing ``entityType`` that is associated with this recurring contract."""

    NATURAL_PERSON = "NaturalPerson"
    COMPANY = "Company"

    __str__ = str.__str__


EntityType2OrStr: TypeAlias = Annotated[EntityType2 | str, open_enum_validator(EntityType2)]
