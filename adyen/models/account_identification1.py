from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountIdentification1(SdkBaseModel):
    """Contains the account number to which the payment funds are sent."""

    type_: Optional[str] = Field(default=UNSET, alias="type")


class AccountIdentification1Dict(TypedDict):
    type_: NotRequired[str]
