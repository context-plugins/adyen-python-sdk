from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrinterStatus1(str, Enum):
    """Possible values:
    * **NoPaper**
    * **OK**
    * **OutOfOrder**
    * **PaperJam**
    * **PaperLow**"""

    OK = "OK"
    PAPER_LOW = "PaperLow"
    NO_PAPER = "NoPaper"
    PAPER_JAM = "PaperJam"
    OUT_OF_ORDER = "OutOfOrder"

    __str__ = str.__str__


PrinterStatus1OrStr: TypeAlias = Annotated[PrinterStatus1 | str, open_enum_validator(PrinterStatus1)]
