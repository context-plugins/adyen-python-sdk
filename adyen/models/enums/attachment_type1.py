from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AttachmentType1(str, Enum):
    """The type of information contained in the attachment: **receipt**, **correspondence**, **other**."""

    RECEIPT = "receipt"
    CORRESPONDENCE = "correspondence"
    OTHER = "other"

    __str__ = str.__str__


AttachmentType1OrStr: TypeAlias = Annotated[AttachmentType1 | str, open_enum_validator(AttachmentType1)]
