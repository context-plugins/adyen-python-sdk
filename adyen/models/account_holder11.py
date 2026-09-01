from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountHolder11(SdkBaseModel):
    """Contains the full name of the person or entity that receives the payment funds)."""

    full_name: str = Field(alias="fullName")
    """Full name of the account holder."""


class AccountHolder11Dict(TypedDict):
    full_name: str
