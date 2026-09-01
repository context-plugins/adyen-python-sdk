from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardBrandDetails(SdkBaseModel):
    healthcare: Optional[bool] = UNSET
    """Indicates if the card supports FSA/HSA healthcare payments."""

    supported: Optional[bool] = UNSET
    """Indicates if you support the card brand."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The name of the card brand."""


class CardBrandDetailsDict(TypedDict):
    healthcare: NotRequired[bool]
    supported: NotRequired[bool]
    type_: NotRequired[str]
