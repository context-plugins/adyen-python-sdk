from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .href3 import Href3, Href3Dict


class IdealAuthLinkResponse(SdkBaseModel):
    redirect_url: Optional[Href3] = Field(default=UNSET, alias="redirectUrl")
    """A short-lived URL that redirects the user to the iDEAL profile management page."""


class IdealAuthLinkResponseDict(TypedDict):
    redirect_url: NotRequired[Href3Dict]
