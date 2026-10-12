from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .capital_grant import CapitalGrant, CapitalGrantDict


class CapitalGrants(SdkBaseModel):
    grants: list[CapitalGrant]
    """The unique identifier of the grant."""


class CapitalGrantsDict(TypedDict):
    grants: list[CapitalGrantDict]
