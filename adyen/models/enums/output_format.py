from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutputFormat(str, Enum):
    """Format of the content to display or print. Display or print device function. Possible values:
    * **MessageRef**
    * **Text**
    * **XHTML**
    * **BarCode**"""

    MESSAGE_REF = "MessageRef"
    TEXT = "Text"
    XHTML = "XHTML"
    BAR_CODE = "BarCode"

    __str__ = str.__str__


OutputFormatOrStr: TypeAlias = Annotated[OutputFormat | str, open_enum_validator(OutputFormat)]
