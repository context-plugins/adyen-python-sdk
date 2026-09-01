from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisbursementRepaymentInfoUpdate(SdkBaseModel):
    basis_points: Optional[int] = Field(default=UNSET, alias="basisPoints")
    """The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage
    expressed in `basis points <https://www.investopedia.com/terms/b/basispoint.asp>`__."""

    update_description: Optional[str] = Field(default=UNSET, alias="updateDescription")


class DisbursementRepaymentInfoUpdateDict(TypedDict):
    basis_points: NotRequired[int]
    update_description: NotRequired[str]
