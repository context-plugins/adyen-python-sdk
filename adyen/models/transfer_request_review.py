from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferRequestReview(SdkBaseModel):
    number_of_approvals_required: Optional[int] = Field(default=UNSET, alias="numberOfApprovalsRequired")
    """Specifies the number of `approvals
    <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve>`__ required to process the
    transfer."""

    sca_on_approval: Optional[bool] = Field(default=UNSET, alias="scaOnApproval")
    """Specifies whether you will initiate Strong Customer Authentication (SCA) in thePOST `/transfers/approve
    <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve>`__ request.

    Only applies to transfers made with an Adyen `business account
    <https://docs.adyen.com/platforms/business-accounts>`__."""


class TransferRequestReviewDict(TypedDict):
    number_of_approvals_required: NotRequired[int]
    sca_on_approval: NotRequired[bool]
