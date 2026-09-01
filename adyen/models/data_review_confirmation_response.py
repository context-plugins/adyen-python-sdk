from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataReviewConfirmationResponse(SdkBaseModel):
    data_reviewed_at: Optional[str] = Field(default=UNSET, alias="dataReviewedAt")
    """Date when data review was confirmed."""


class DataReviewConfirmationResponseDict(TypedDict):
    data_reviewed_at: NotRequired[str]
