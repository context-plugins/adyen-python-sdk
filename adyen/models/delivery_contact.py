from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name import Name, NameDict
from .store_location import StoreLocation, StoreLocationDict
from .vias_phone_number import ViasPhoneNumber, ViasPhoneNumberDict


class DeliveryContact(SdkBaseModel):
    address: StoreLocation
    """The address of the contact."""

    company: Optional[str] = UNSET
    """The company name of the contact."""

    email: Optional[str] = UNSET
    """The email address of the contact."""

    full_phone_number: Optional[str] = Field(default=UNSET, alias="fullPhoneNumber")
    """The full phone number of the contact provided as a single string. It will be handled as a landline phone.
    **Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
    """

    name: Name
    """The name of the contact."""

    phone_number: Optional[ViasPhoneNumber] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the contact."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the contact's website."""


class DeliveryContactDict(TypedDict):
    address: StoreLocationDict
    company: NotRequired[str]
    email: NotRequired[str]
    full_phone_number: NotRequired[str]
    name: NameDict
    phone_number: NotRequired[ViasPhoneNumberDict]
    web_address: NotRequired[str]
