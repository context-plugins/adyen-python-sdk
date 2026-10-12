from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .create_sca_information1 import CreateScaInformation1, CreateScaInformation1Dict
from .enums.scope import ScopeOrStr
from .enums.transfer_type import TransferTypeOrStr


class CreateTransferLimitRequest(SdkBaseModel):
    amount: Amount17
    """The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on the
    ``scope`` of the limit."""

    ends_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endsAt")
    """The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays
    active until you override it with a new limit.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: **YYYY-MM-DDThh:mm:ss.sssTZD**"""

    reference: Optional[str] = UNSET
    """Your reference for the transfer limit."""

    sca_information: Optional[CreateScaInformation1] = Field(default=UNSET, alias="scaInformation")
    """Information for the Strong Customer Authentication (SCA)"""

    scope: ScopeOrStr
    """The scope to which the transfer limit applies. Possible values:
    * **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.
    * **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in
        a day."""

    starts_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startsAt")
    """The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a
    transfer limit.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: **YYYY-MM-DDThh:mm:ss.sssTZD**"""

    transfer_type: TransferTypeOrStr = Field(alias="transferType")
    """The type of transfer to which the limit applies. Possible values:
    * **instant**: the limit applies to transfers with an **instant** priority.
    * **all**: the limit applies to all transfers, regardless of priority."""


class CreateTransferLimitRequestDict(TypedDict):
    amount: Amount17Dict
    ends_at: NotRequired[RFC3339DateTime]
    reference: NotRequired[str]
    sca_information: NotRequired[CreateScaInformation1Dict]
    scope: ScopeOrStr
    starts_at: NotRequired[RFC3339DateTime]
    transfer_type: TransferTypeOrStr
