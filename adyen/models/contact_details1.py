from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .phone31 import Phone31, Phone31Dict


class ContactDetails1(SdkBaseModel):
    """Contact details of the account holder."""

    address: Address
    """The address of the account holder."""

    email: str
    """The email address of the account holder."""

    phone: Phone31
    """The phone number of the account holder."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the account holder's website."""


class ContactDetails1Dict(TypedDict):
    address: AddressDict
    email: str
    phone: Phone31Dict
    web_address: NotRequired[str]
