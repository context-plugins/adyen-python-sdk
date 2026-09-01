from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssociationStatus(str, Enum):
    PENDING_APPROVAL = "pendingApproval"
    ACTIVE = "active"

    __str__ = str.__str__


AssociationStatusOrStr: TypeAlias = Annotated[AssociationStatus | str, open_enum_validator(AssociationStatus)]
