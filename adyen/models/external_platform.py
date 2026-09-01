from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExternalPlatform(SdkBaseModel):
    """Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc."""

    integrator: Optional[str] = UNSET
    """External platform integrator."""

    name: Optional[str] = UNSET
    """Name of the field. For example, Name of External Platform."""

    version: Optional[str] = UNSET
    """Version of the field. For example, Version of External Platform."""


class ExternalPlatformDict(TypedDict):
    integrator: NotRequired[str]
    name: NotRequired[str]
    version: NotRequired[str]
