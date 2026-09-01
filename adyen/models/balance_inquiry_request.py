from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account_req2 import LoyaltyAccountReq2, LoyaltyAccountReq2Dict
from .payment_account_req2 import PaymentAccountReq2, PaymentAccountReq2Dict


class BalanceInquiryRequest(SdkBaseModel):
    """It conveys Information related to the account for which a Balance Inquiry is requested. Content of the Balance
    Inquiry Request message."""

    payment_account_req: Optional[PaymentAccountReq2] = Field(default=UNSET, alias="PaymentAccountReq")
    """Data related to the account pointed by the payment card."""

    loyalty_account_req: Optional[LoyaltyAccountReq2] = Field(default=UNSET, alias="LoyaltyAccountReq")
    """Data related to a requested Loyalty program or account."""


class BalanceInquiryRequestDict(TypedDict):
    payment_account_req: NotRequired[PaymentAccountReq2 | PaymentAccountReq2Dict]
    loyalty_account_req: NotRequired[LoyaltyAccountReq2 | LoyaltyAccountReq2Dict]
