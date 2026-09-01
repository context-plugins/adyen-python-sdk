from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.contract_type import ContractTypeOrStr
from .fee1 import Fee1, Fee1Dict
from .repayment2 import Repayment2, Repayment2Dict


class GrantOffer(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The identifier of the account holder to which the grant is offered."""

    amount: Optional[Amount17] = UNSET
    """The principal amount of the grant."""

    contract_type: Optional[ContractTypeOrStr] = Field(default=UNSET, alias="contractType")
    """The contract type of the grant offer. Possible value: **cashAdvance**, **loan**."""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The end date of the grant offer validity period."""

    fee: Optional[Fee1] = UNSET
    """Details of the fee configuration."""

    id: Optional[str] = UNSET
    """The unique identifier of the grant offer."""

    repayment: Optional[Repayment2] = UNSET
    """Details of the repayment configuration."""

    starts_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startsAt")
    """The starting date of the grant offer validity period."""


class GrantOfferDict(TypedDict):
    account_holder_id: str
    amount: NotRequired[Amount17 | Amount17Dict]
    contract_type: NotRequired[ContractTypeOrStr]
    expires_at: NotRequired[RFC3339DateTime]
    fee: NotRequired[Fee1 | Fee1Dict]
    id: NotRequired[str]
    repayment: NotRequired[Repayment2 | Repayment2Dict]
    starts_at: NotRequired[RFC3339DateTime]
