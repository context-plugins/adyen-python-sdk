from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentType(str, Enum):
    """The content type of the tax form.

    Possible values:
    * **application/pdf**"""

    APPLICATION_PDF = "application/pdf"

    __str__ = str.__str__


ContentTypeOrStr: TypeAlias = Annotated[ContentType | str, open_enum_validator(ContentType)]
