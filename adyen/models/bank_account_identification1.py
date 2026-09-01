from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankAccountIdentification1(SdkBaseModel):
    """Contains the identification information of the account to which you can transfer funds related to repayments."""

    type_: Optional[str] = Field(default=UNSET, alias="type")


class BankAccountIdentification1Dict(TypedDict):
    type_: NotRequired[str]
