from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .href4 import Href4, Href4Dict


class IdealAuthenticateResponse(SdkBaseModel):
    redirect_url: Optional[Href4] = Field(default=UNSET, alias="redirectUrl")
    """A short-lived URL that redirects the user to the iDEAL page that is required for authentication."""


class IdealAuthenticateResponseDict(TypedDict):
    redirect_url: NotRequired[Href4Dict]
