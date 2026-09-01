from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssociationStatus1(str, Enum):
    """The status of the association.

    Possible values: **active** or **pendingApproval**."""

    PENDING_APPROVAL = "pendingApproval"
    ACTIVE = "active"

    __str__ = str.__str__


AssociationStatus1OrStr: TypeAlias = Annotated[AssociationStatus1 | str, open_enum_validator(AssociationStatus1)]
