from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountHolder1(SdkBaseModel):
    full_name: str = Field(alias="fullName")
    """Full name of the account holder."""


class AccountHolder1Dict(TypedDict):
    full_name: str
