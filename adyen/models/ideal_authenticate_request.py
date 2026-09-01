from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdealAuthenticateRequest(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier for an account holder."""

    payload: str
    """A payload provided by iDEAL to complete the authentication process."""


class IdealAuthenticateRequestDict(TypedDict):
    account_holder_id: str
    payload: str
