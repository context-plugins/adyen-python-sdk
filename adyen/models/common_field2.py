from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonField2(SdkBaseModel):
    """Merchant developed software, such as cashier application, used to interact with the Adyen API."""

    name: Optional[str] = UNSET
    """Name of the field. For example, Name of External Platform."""

    version: Optional[str] = UNSET
    """Version of the field. For example, Version of External Platform."""


class CommonField2Dict(TypedDict):
    name: NotRequired[str]
    version: NotRequired[str]
