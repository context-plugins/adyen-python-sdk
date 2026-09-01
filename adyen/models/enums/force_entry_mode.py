from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ForceEntryMode(str, Enum):
    RFID = "RFID"
    KEYED = "Keyed"
    MANUAL = "Manual"
    FILE = "File"
    SCANNED = "Scanned"
    MAG_STRIPE = "MagStripe"
    ICC = "ICC"
    SYNCHRONOUS_ICC = "SynchronousICC"
    TAPPED = "Tapped"
    CONTACTLESS = "Contactless"
    CHECK_READER = "CheckReader"

    __str__ = str.__str__


ForceEntryModeOrStr: TypeAlias = Annotated[ForceEntryMode | str, open_enum_validator(ForceEntryMode)]
