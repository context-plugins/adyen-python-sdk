from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.contract_type import ContractTypeOrStr
from .grant_offer_fee1 import GrantOfferFee1, GrantOfferFee1Dict
from .repayment11 import Repayment11, Repayment11Dict


class CalculatedGrantOffer(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder that the dynamic offer is for."""

    amount: Amount17
    """The financing amount that would be paid out to your user."""

    contract_type: ContractTypeOrStr = Field(alias="contractType")
    """The contract type of the offer.

    Possible values:
    * **loan**
    * **cashAdvance**"""

    expires_at: RFC3339DateTime = Field(alias="expiresAt")
    """The expiration date and time of the offer validity period."""

    fee: GrantOfferFee1
    """Contains information about the fee that your user would pay for the grant."""

    repayment: Repayment11
    """Contains information about the repayment configuration of the grant."""

    starts_at: RFC3339DateTime = Field(alias="startsAt")
    """The starting date and time of the offer validity period."""


class CalculatedGrantOfferDict(TypedDict):
    account_holder_id: str
    amount: Amount17Dict
    contract_type: ContractTypeOrStr
    expires_at: RFC3339DateTime
    fee: GrantOfferFee1Dict
    repayment: Repayment11Dict
    starts_at: RFC3339DateTime
