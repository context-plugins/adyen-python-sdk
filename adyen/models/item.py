from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item(SdkBaseModel):
    """The token requestor is an entity who requested tokenization of the card for secure payments."""

    id: Optional[str] = UNSET
    """The value to provide in the result."""

    name: Optional[str] = UNSET
    """The display name."""


class ItemDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
