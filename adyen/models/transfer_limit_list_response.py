from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_limit import TransferLimit, TransferLimitDict


class TransferLimitListResponse(SdkBaseModel):
    transfer_limits: list[TransferLimit] = Field(alias="transferLimits")
    """List of available transfer limits."""


class TransferLimitListResponseDict(TypedDict):
    transfer_limits: list[TransferLimitDict]
