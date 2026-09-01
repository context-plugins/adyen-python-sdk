from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .provider2 import Provider2, Provider2Dict


class Route(SdkBaseModel):
    link: str
    """The redirection link. You can use this link to redirect the user to the open banking flow when the user selects
    it."""

    provider: Provider2
    """Metadata about the selected provider, including the name and company logo. You can use this information to inform
    the user about the provider they will be redirected to when they select the link."""


class RouteDict(TypedDict):
    link: str
    provider: Provider2 | Provider2Dict
