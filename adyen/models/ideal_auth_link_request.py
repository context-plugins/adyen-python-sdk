from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdealAuthLinkRequest(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder."""


class IdealAuthLinkRequestDict(TypedDict):
    account_holder_id: str
