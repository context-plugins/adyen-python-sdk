from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address3 import Address3, Address3Dict
from .name1 import Name1, Name1Dict


class FundOrigin1(SdkBaseModel):
    """The person or entity funding the money."""

    billing_address: Optional[Address3] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The email address of the person funding the money."""

    shopper_name: Optional[Name1] = Field(default=UNSET, alias="shopperName")
    """The name of the person funding the money."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The phone number of the person funding the money."""

    wallet_identifier: Optional[str] = Field(default=UNSET, alias="walletIdentifier")
    """The unique identifier of the wallet where the funds are coming from."""


class FundOrigin1Dict(TypedDict):
    billing_address: NotRequired[Address3 | Address3Dict]
    shopper_email: NotRequired[str]
    shopper_name: NotRequired[Name1 | Name1Dict]
    telephone_number: NotRequired[str]
    wallet_identifier: NotRequired[str]
