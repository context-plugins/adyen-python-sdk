from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name4(SdkBaseModel):
    """The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're
    enrolled in the PayPal Seller Protection program."""

    first_name: str = Field(alias="firstName")
    """The first name."""

    last_name: str = Field(alias="lastName")
    """The last name."""


class Name4Dict(TypedDict):
    first_name: str
    last_name: str
