from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CostEstimateAssumptions1(SdkBaseModel):
    """Assumptions made for the expected characteristics of the transaction, for which the charges are being
    estimated."""

    assume3_d_secure_authenticated: Optional[bool] = Field(default=UNSET, alias="assume3DSecureAuthenticated")
    """If true, the cardholder is expected to successfully authorise via 3D Secure."""

    assume_level3_data: Optional[bool] = Field(default=UNSET, alias="assumeLevel3Data")
    """If true, the transaction is expected to have valid Level 3 data."""

    installments: Optional[int] = UNSET
    """If not zero, the number of installments."""


class CostEstimateAssumptions1Dict(TypedDict):
    assume3_d_secure_authenticated: NotRequired[bool]
    assume_level3_data: NotRequired[bool]
    installments: NotRequired[int]
