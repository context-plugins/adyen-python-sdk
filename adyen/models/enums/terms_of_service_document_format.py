from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TermsOfServiceDocumentFormat(str, Enum):
    """The format of the Terms of Service document."""

    JSON = "JSON"
    PDF = "PDF"
    TXT = "TXT"

    __str__ = str.__str__


TermsOfServiceDocumentFormatOrStr: TypeAlias = Annotated[
    TermsOfServiceDocumentFormat | str, open_enum_validator(TermsOfServiceDocumentFormat)
]
