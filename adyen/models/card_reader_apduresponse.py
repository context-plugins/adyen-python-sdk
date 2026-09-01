from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response11 import Response11, Response11Dict


class CardReaderApduresponse(SdkBaseModel):
    """Content of the Card Reader APDU Response message. It contains the result of the requested service, APDU response
    sent by the chip of the card in response to the APDU request."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    apdu_data: Optional[str] = Field(default=UNSET, alias="APDUData")
    """Data field of the APDU command (Lc + Data)."""

    card_status_words: str = Field(alias="CardStatusWords")
    """Status of a smartcard response to a command (SW1-SW2)."""


class CardReaderApduresponseDict(TypedDict):
    response: Response11 | Response11Dict
    apdu_data: NotRequired[str]
    card_status_words: str
