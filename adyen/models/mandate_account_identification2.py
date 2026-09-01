from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MandateAccountIdentification2(SdkBaseModel):
    """Contains the bank account details of the counterparty. The fields required in this object depend on the country
    of the bank account and the currency of the transfer."""

    type_: Optional[str] = Field(default=UNSET, alias="type")


class MandateAccountIdentification2Dict(TypedDict):
    type_: NotRequired[str]
