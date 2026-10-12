from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .dynamic_offer_repayment2 import DynamicOfferRepayment2, DynamicOfferRepayment2Dict
from .enums.contract_type import ContractTypeOrStr
from .enums.financing_type2 import FinancingType2OrStr


class DynamicOffer(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the account holder that the dynamic offer is for."""

    contract_type: ContractTypeOrStr = Field(alias="contractType")
    """The contract type of the offer.

    Possible values:
    * **loan**
    * **cashAdvance**"""

    expires_at: RFC3339DateTime = Field(alias="expiresAt")
    """The expiration date and time of the offer validity period."""

    financing_type: FinancingType2OrStr = Field(alias="financingType")
    """The type of financing that the offer is for.

    Possible values: **businessFinancing**."""

    id: str
    """The unique identifier of the dynamic offer."""

    maximum_amount: Amount17 = Field(alias="maximumAmount")
    """The maximum financing amount available to the account holder under this offer."""

    minimum_amount: Amount17 = Field(alias="minimumAmount")
    """The minimum financing amount available to the account holder under this offer."""

    repayment: DynamicOfferRepayment2
    """Contains information about the repayment configuration of the grant."""

    starts_at: RFC3339DateTime = Field(alias="startsAt")
    """The starting date and time of the offer validity period."""


class DynamicOfferDict(TypedDict):
    account_holder_id: str
    contract_type: ContractTypeOrStr
    expires_at: RFC3339DateTime
    financing_type: FinancingType2OrStr
    id: str
    maximum_amount: Amount17Dict
    minimum_amount: Amount17Dict
    repayment: DynamicOfferRepayment2Dict
    starts_at: RFC3339DateTime
