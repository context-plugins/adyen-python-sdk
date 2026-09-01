from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .links_element6 import LinksElement6, LinksElement6Dict


class Links1(SdkBaseModel):
    """References to resources connected with this user."""

    self: LinksElement6
    """Link to the resource itself."""


class Links1Dict(TypedDict):
    self: LinksElement6 | LinksElement6Dict
