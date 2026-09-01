from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Contact1(SdkBaseModel):
    """The contact details for the shipping location."""

    email: Optional[str] = UNSET
    """The individual's email address."""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The individual's first name."""

    infix: Optional[str] = UNSET
    """The infix in the individual's name, if any."""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The individual's last name."""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The individual's phone number, specified as 10-14 digits with an optional ``+`` prefix."""


class Contact1Dict(TypedDict):
    email: NotRequired[str]
    first_name: NotRequired[str]
    infix: NotRequired[str]
    last_name: NotRequired[str]
    phone_number: NotRequired[str]
