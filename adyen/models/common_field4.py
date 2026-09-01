from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonField4(SdkBaseModel):
    """Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example,
    Magento plugin, Java API library, etc."""

    name: Optional[str] = UNSET
    """Name of the field. For example, Name of External Platform."""

    version: Optional[str] = UNSET
    """Version of the field. For example, Version of External Platform."""


class CommonField4Dict(TypedDict):
    name: NotRequired[str]
    version: NotRequired[str]
