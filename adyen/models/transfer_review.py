from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sca_on_approval import ScaOnApprovalOrStr


class TransferReview(SdkBaseModel):
    number_of_approvals_required: Optional[int] = Field(default=UNSET, alias="numberOfApprovalsRequired")
    """Shows the number of `approvals <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve>`__
    required to process the transfer."""

    sca_on_approval: Optional[ScaOnApprovalOrStr] = Field(default=UNSET, alias="scaOnApproval")
    """Shows the status of the Strong Customer Authentication (SCA) process.

    Possible values: **required**, **notApplicable**."""


class TransferReviewDict(TypedDict):
    number_of_approvals_required: NotRequired[int]
    sca_on_approval: NotRequired[ScaOnApprovalOrStr]
