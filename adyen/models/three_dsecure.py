from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ThreeDsecure(SdkBaseModel):
    acs_transaction_id: Optional[str] = Field(default=UNSET, alias="acsTransactionId")
    """The transaction identifier for the Access Control Server"""


class ThreeDsecureDict(TypedDict):
    acs_transaction_id: NotRequired[str]
