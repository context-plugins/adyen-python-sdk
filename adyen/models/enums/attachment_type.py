from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AttachmentType(str, Enum):
    RECEIPT = "receipt"
    CORRESPONDENCE = "correspondence"
    OTHER = "other"

    __str__ = str.__str__


AttachmentTypeOrStr: TypeAlias = Annotated[AttachmentType | str, open_enum_validator(AttachmentType)]
