from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrinterStatus(str, Enum):
    """Indicates if the printer is working and usable. Possible values:
    * **OK**
    * **PaperLow**
    * **NoPaper**
    * **PaperJam**
    * **OutOfOrder**"""

    OK = "OK"
    PAPER_LOW = "PaperLow"
    NO_PAPER = "NoPaper"
    PAPER_JAM = "PaperJam"
    OUT_OF_ORDER = "OutOfOrder"

    __str__ = str.__str__


PrinterStatusOrStr: TypeAlias = Annotated[PrinterStatus | str, open_enum_validator(PrinterStatus)]
