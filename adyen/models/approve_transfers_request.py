from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApproveTransfersRequest(SdkBaseModel):
    transfer_ids: Optional[list[str]] = Field(default=UNSET, alias="transferIds")
    """Contains the unique identifiers of the transfers that you want to approve."""


class ApproveTransfersRequestDict(TypedDict):
    transfer_ids: NotRequired[list[str]]
