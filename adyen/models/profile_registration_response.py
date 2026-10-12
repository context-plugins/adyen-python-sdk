from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .href5 import Href5, Href5Dict


class ProfileRegistrationResponse(SdkBaseModel):
    redirect_url: Optional[Href5] = Field(default=UNSET, alias="redirectUrl")
    """A short-lived URL that redirects the user to the iDEAL profile registration page."""


class ProfileRegistrationResponseDict(TypedDict):
    redirect_url: NotRequired[Href5Dict]
