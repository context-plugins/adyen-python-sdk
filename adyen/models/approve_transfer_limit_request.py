from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApproveTransferLimitRequest(SdkBaseModel):
    transfer_limit_ids: list[str] = Field(alias="transferLimitIds")
    """A list that includes the ``transferLimitId`` of all the pending transfer limits you want to approve."""


class ApproveTransferLimitRequestDict(TypedDict):
    transfer_limit_ids: list[str]
