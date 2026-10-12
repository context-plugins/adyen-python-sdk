from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element import LinksElement, LinksElementDict
from .links_element6 import LinksElement6, LinksElement6Dict


class CompanyLinks(SdkBaseModel):
    api_credentials: Optional[LinksElement] = Field(default=UNSET, alias="apiCredentials")
    self: LinksElement6
    """Link to the resource itself."""

    users: Optional[LinksElement] = UNSET
    webhooks: Optional[LinksElement] = UNSET


class CompanyLinksDict(TypedDict):
    api_credentials: NotRequired[LinksElementDict]
    self: LinksElement6Dict
    users: NotRequired[LinksElementDict]
    webhooks: NotRequired[LinksElementDict]
