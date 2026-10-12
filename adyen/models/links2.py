from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .links_element6 import LinksElement6, LinksElement6Dict


class Links2(SdkBaseModel):
    """References to resources linked to the allowed origin."""

    self: LinksElement6
    """Link to the resource itself."""


class Links2Dict(TypedDict):
    self: LinksElement6Dict
