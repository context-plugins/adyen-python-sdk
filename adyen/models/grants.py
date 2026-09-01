from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grant import Grant, GrantDict


class Grants(SdkBaseModel):
    grants: list[Grant]
    """Contains a list of the grants that the account holder has received."""


class GrantsDict(TypedDict):
    grants: list[Grant | GrantDict]
