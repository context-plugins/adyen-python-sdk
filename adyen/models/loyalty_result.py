from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account1 import LoyaltyAccount1, LoyaltyAccount1Dict
from .loyalty_acquirer_data1 import LoyaltyAcquirerData1, LoyaltyAcquirerData1Dict


class LoyaltyResult(SdkBaseModel):
    """Data related to the result of a processed loyalty transaction. In the Message Response, the result of each
    loyalty brand transaction."""

    loyalty_account: LoyaltyAccount1 = Field(alias="LoyaltyAccount")
    """Data related to a loyalty account processed in the transaction."""

    current_balance: Optional[float] = Field(default=UNSET, alias="CurrentBalance")
    """Balance of an account. If known (provided by the card or an external host)."""

    loyalty_acquirer_data: Optional[LoyaltyAcquirerData1] = Field(default=UNSET, alias="LoyaltyAcquirerData")
    """Data related to the loyalty Acquirer during a loyalty transaction. If content not empty."""


class LoyaltyResultDict(TypedDict):
    loyalty_account: LoyaltyAccount1 | LoyaltyAccount1Dict
    current_balance: NotRequired[float]
    loyalty_acquirer_data: NotRequired[LoyaltyAcquirerData1 | LoyaltyAcquirerData1Dict]
