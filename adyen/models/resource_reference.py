from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourceReference(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description of the resource."""

    id: Optional[str] = UNSET
    """The unique identifier of the resource."""

    reference: Optional[str] = UNSET
    """The reference for the resource."""


class ResourceReferenceDict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    reference: NotRequired[str]
