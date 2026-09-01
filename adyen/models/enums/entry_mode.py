from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntryMode(str, Enum):
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
    MOBILE = "Mobile"

    __str__ = str.__str__


EntryModeOrStr: TypeAlias = Annotated[EntryMode | str, open_enum_validator(EntryMode)]
