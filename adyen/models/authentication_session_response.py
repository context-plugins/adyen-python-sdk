from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthenticationSessionResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the session."""

    token: Optional[str] = UNSET
    """The session token created."""


class AuthenticationSessionResponseDict(TypedDict):
    id: NotRequired[str]
    token: NotRequired[str]
