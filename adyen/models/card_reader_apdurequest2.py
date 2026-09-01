from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardReaderApdurequest2(SdkBaseModel):
    """Content of the Card Reader APDU Request message."""

    apdu_class: str = Field(alias="APDUClass")
    """Class field of the APDU command (CLA). APDU request for Card Reader device request. For specific card like
    synchronous card, a private value should be used in accordance to ISO 7816- 4 (private range D0-FE)."""

    apdu_instruction: str = Field(alias="APDUInstruction")
    """Instruction field of the APDU command (INS)."""

    apdu_par1: str = Field(alias="APDUPar1")
    """Parameter 1 field of the APDU command (P1)."""

    apdu_par2: str = Field(alias="APDUPar2")
    """Parameter 2 field of the APDU command(P2)."""

    apdu_data: Optional[str] = Field(default=UNSET, alias="APDUData")
    """Data field of the APDU command (Lc + Data)."""

    apdu_expected_length: Optional[str] = Field(default=UNSET, alias="APDUExpectedLength")
    """Expected length of the data field of the APDU response to the command (Le)."""


class CardReaderApdurequest2Dict(TypedDict):
    apdu_class: str
    apdu_instruction: str
    apdu_par1: str
    apdu_par2: str
    apdu_data: NotRequired[str]
    apdu_expected_length: NotRequired[str]
