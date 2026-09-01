from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonField1(SdkBaseModel):
    """Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc."""

    name: Optional[str] = UNSET
    """Name of the field. For example, Name of External Platform."""

    version: Optional[str] = UNSET
    """Version of the field. For example, Version of External Platform."""


class CommonField1Dict(TypedDict):
    name: NotRequired[str]
    version: NotRequired[str]
