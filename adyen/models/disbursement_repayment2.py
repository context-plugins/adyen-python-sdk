from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DisbursementRepayment2(SdkBaseModel):
    """Contains information about the basis points configured for repaying the disbursement."""

    basis_points: int = Field(alias="basisPoints")
    """The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage
    expressed in `basis points <https://www.investopedia.com/terms/b/basispoint.asp>`__."""

    update_description: str = Field(alias="updateDescription")


class DisbursementRepayment2Dict(TypedDict):
    basis_points: int
    update_description: str
