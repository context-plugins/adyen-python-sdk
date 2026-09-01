from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element import LinksElement, LinksElementDict
from .links_element6 import LinksElement6, LinksElement6Dict


class CompanyLinks2(SdkBaseModel):
    """References to resources connected with this company."""

    api_credentials: Optional[LinksElement] = Field(default=UNSET, alias="apiCredentials")
    self: LinksElement6
    """Link to the resource itself."""

    users: Optional[LinksElement] = UNSET
    webhooks: Optional[LinksElement] = UNSET


class CompanyLinks2Dict(TypedDict):
    api_credentials: NotRequired[LinksElement | LinksElementDict]
    self: LinksElement6 | LinksElement6Dict
    users: NotRequired[LinksElement | LinksElementDict]
    webhooks: NotRequired[LinksElement | LinksElementDict]
