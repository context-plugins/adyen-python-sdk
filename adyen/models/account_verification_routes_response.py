from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .route import Route, RouteDict


class AccountVerificationRoutesResponse(SdkBaseModel):
    routes: list[Route]
    """This array lists available open banking redirection links, each with its associated provider metadata."""


class AccountVerificationRoutesResponseDict(TypedDict):
    routes: list[RouteDict]
