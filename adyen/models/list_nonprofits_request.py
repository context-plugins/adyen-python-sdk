from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ListNonprofitsRequest(SdkBaseModel):
    account_holder_ids: list[str] = Field(alias="accountHolderIds")
    """The unique identifiers of the account holders to be included in a donation campaign."""


class ListNonprofitsRequestDict(TypedDict):
    account_holder_ids: list[str]
