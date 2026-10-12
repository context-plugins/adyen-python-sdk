from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.limit_status import LimitStatusOrStr
from .enums.scope import ScopeOrStr
from .enums.transfer_type import TransferTypeOrStr
from .sca_information1 import ScaInformation1, ScaInformation1Dict


class TransferLimit(SdkBaseModel):
    """The transfer limit configured to regulate outgoing transfers."""

    amount: Amount17
    """The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on the
    ``scope`` of the limit."""

    ends_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endsAt")
    """The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays
    active until you override it with a new limit.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: **YYYY-MM-DDThh:mm:ss.sssTZD**"""

    id: str
    """The unique identifier of the transfer limit."""

    limit_status: LimitStatusOrStr = Field(alias="limitStatus")
    """The status of the transfer limit. Possible values:
    * **active**: the limit is currently active.
    * **inactive**: the limit is currently inactive.
    * **pendingSCA**: the limit is pending until your user performs SCA.
    * **scheduled**: the limit is scheduled to become active at a future date."""

    reference: Optional[str] = UNSET
    """Your reference for the transfer limit."""

    sca_information: Optional[ScaInformation1] = Field(default=UNSET, alias="scaInformation")
    """Information for the Strong Customer Authentication (SCA)"""

    scope: ScopeOrStr
    """The scope to which the transfer limit applies. Possible values:
    * **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.
    * **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in
        a day."""

    starts_at: RFC3339DateTime = Field(alias="startsAt")
    """The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a
    transfer limit.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: **YYYY-MM-DDThh:mm:ss.sssTZD**"""

    transfer_type: TransferTypeOrStr = Field(alias="transferType")
    """The type of transfer to which the limit applies. Possible values:
    * **instant**: the limit applies to transfers with an **instant** priority.
    * **all**: the limit applies to all transfers, regardless of priority."""


class TransferLimitDict(TypedDict):
    amount: Amount17Dict
    ends_at: NotRequired[RFC3339DateTime]
    id: str
    limit_status: LimitStatusOrStr
    reference: NotRequired[str]
    sca_information: NotRequired[ScaInformation1Dict]
    scope: ScopeOrStr
    starts_at: RFC3339DateTime
    transfer_type: TransferTypeOrStr
