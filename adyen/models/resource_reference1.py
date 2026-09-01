from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourceReference1(SdkBaseModel):
    """Contains information about the balance account involved in the transfer."""

    description: Optional[str] = UNSET
    """The description of the resource."""

    id: Optional[str] = UNSET
    """The unique identifier of the resource."""

    reference: Optional[str] = UNSET
    """The reference for the resource."""


class ResourceReference1Dict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    reference: NotRequired[str]
