from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict


class TerminalModelsResponse(SdkBaseModel):
    data: Optional[list[Item]] = UNSET
    """The terminal models that the API credential has access to."""


class TerminalModelsResponseDict(TypedDict):
    data: NotRequired[list[Item | ItemDict]]
