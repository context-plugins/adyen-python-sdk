from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .links_element6 import LinksElement6, LinksElement6Dict


class Links7(SdkBaseModel):
    """Reference to resources connected with the store."""

    self: LinksElement6
    """Link to the resource itself."""


class Links7Dict(TypedDict):
    self: LinksElement6Dict
