from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links21 import Links21, Links21Dict
from .transfer_data import TransferData, TransferDataDict


class FindTransfersResponse(SdkBaseModel):
    links: Optional[Links21] = Field(default=UNSET, alias="_links")
    """Contains links to the next and previous page whenever applicable."""

    data: Optional[list[TransferData]] = UNSET
    """Contains the transfers that match the query parameters."""


class FindTransfersResponseDict(TypedDict):
    links: NotRequired[Links21Dict]
    data: NotRequired[list[TransferDataDict]]
