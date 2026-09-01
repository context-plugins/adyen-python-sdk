from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutputFormat1(str, Enum):
    """Format of the content to display or print. Possible values:
    * **BarCode**
    * **MessageRef**
    * **Text**
    * **XHTML**"""

    MESSAGE_REF = "MessageRef"
    TEXT = "Text"
    XHTML = "XHTML"
    BAR_CODE = "BarCode"

    __str__ = str.__str__


OutputFormat1OrStr: TypeAlias = Annotated[OutputFormat1 | str, open_enum_validator(OutputFormat1)]
