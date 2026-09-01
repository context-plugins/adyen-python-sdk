from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutputFormat2(str, Enum):
    """Possible values:
    * **BarCode**
    * **MessageRef**
    * **Text**
    * **XHTML**"""

    MESSAGE_REF = "MessageRef"
    TEXT = "Text"
    XHTML = "XHTML"
    BAR_CODE = "BarCode"

    __str__ = str.__str__


OutputFormat2OrStr: TypeAlias = Annotated[OutputFormat2 | str, open_enum_validator(OutputFormat2)]
