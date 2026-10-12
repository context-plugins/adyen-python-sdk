from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class GrantOfferFee(SdkBaseModel):
    amount: Amount17
    """Contains the amount of the offer fee."""

    apr_basis_points: Optional[int] = Field(default=UNSET, alias="aprBasisPoints")
    """Annual Percentage Rate (APR) of the offer. The percentage is expressed in `basis points
    <https://www.investopedia.com/terms/b/basispoint.asp>`__."""


class GrantOfferFeeDict(TypedDict):
    amount: Amount17Dict
    apr_basis_points: NotRequired[int]
