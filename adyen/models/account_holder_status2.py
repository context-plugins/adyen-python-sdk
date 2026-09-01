from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_event import AccountEvent, AccountEventDict
from .account_payout_state2 import AccountPayoutState2, AccountPayoutState2Dict
from .account_processing_state2 import AccountProcessingState2, AccountProcessingState2Dict
from .enums.status12 import Status12OrStr


class AccountHolderStatus2(SdkBaseModel):
    """The status of the new account holder."""

    events: Optional[list[AccountEvent]] = UNSET
    """A list of events scheduled for the account holder."""

    payout_state: Optional[AccountPayoutState2] = Field(default=UNSET, alias="payoutState")
    """The payout state of the account holder."""

    processing_state: Optional[AccountProcessingState2] = Field(default=UNSET, alias="processingState")
    """The processing state of the account holder."""

    status: Status12OrStr
    """The status of the account holder. >Permitted values: ``Active``, ``Inactive``, ``Suspended``, ``Closed``."""

    status_reason: Optional[str] = Field(default=UNSET, alias="statusReason")
    """The reason why the status was assigned to the account holder."""


class AccountHolderStatus2Dict(TypedDict):
    events: NotRequired[list[AccountEvent | AccountEventDict]]
    payout_state: NotRequired[AccountPayoutState2 | AccountPayoutState2Dict]
    processing_state: NotRequired[AccountProcessingState2 | AccountProcessingState2Dict]
    status: Status12OrStr
    status_reason: NotRequired[str]
