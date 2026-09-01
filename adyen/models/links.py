from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .links_element6 import LinksElement6, LinksElement6Dict


class Links(SdkBaseModel):
    self: LinksElement6
    """Link to the resource itself."""


class LinksDict(TypedDict):
    self: LinksElement6 | LinksElement6Dict
