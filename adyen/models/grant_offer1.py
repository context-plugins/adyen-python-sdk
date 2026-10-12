from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.contract_type import ContractTypeOrStr
from .grant_offer_fee1 import GrantOfferFee1, GrantOfferFee1Dict
from .repayment11 import Repayment11, Repayment11Dict


class GrantOffer1(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder to which the grant is offered."""

    amount: Optional[Amount17] = UNSET
    """The amount that would be paid out to the user for business financing."""

    contract_type: Optional[ContractTypeOrStr] = Field(default=UNSET, alias="contractType")
    """The contract type of the offer.

    Possible values:
    * **loan**
    * **cashAdvance**"""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The expiration date and time of the offer validity period."""

    fee: Optional[GrantOfferFee1] = UNSET
    """Contains information about the fee that your user would pay for the grant."""

    id: Optional[str] = UNSET
    """The unique identifier of the offer."""

    repayment: Optional[Repayment11] = UNSET
    """Contains information about the repayment configuration of the grant."""

    starts_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startsAt")
    """The starting date and time of the offer validity period."""


class GrantOffer1Dict(TypedDict):
    account_holder_id: str
    amount: NotRequired[Amount17Dict]
    contract_type: NotRequired[ContractTypeOrStr]
    expires_at: NotRequired[RFC3339DateTime]
    fee: NotRequired[GrantOfferFee1Dict]
    id: NotRequired[str]
    repayment: NotRequired[Repayment11Dict]
    starts_at: NotRequired[RFC3339DateTime]
