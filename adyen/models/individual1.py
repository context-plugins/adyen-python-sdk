from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address13 import Address13, Address13Dict
from .birth_data1 import BirthData1, BirthData1Dict
from .identification_data1 import IdentificationData1, IdentificationData1Dict
from .name23 import Name23, Name23Dict
from .phone_number2 import PhoneNumber2, PhoneNumber2Dict
from .support1 import Support1, Support1Dict
from .tax_information import TaxInformation, TaxInformationDict
from .web_data1 import WebData1, WebData1Dict


class Individual1(SdkBaseModel):
    """Information about the individual. Required if ``type`` is **individual**."""

    birth_data: Optional[BirthData1] = Field(default=UNSET, alias="birthData")
    """The individual's birth information."""

    email: Optional[str] = UNSET
    """The email address of the legal entity."""

    identification_data: Optional[IdentificationData1] = Field(default=UNSET, alias="identificationData")
    """Information about the individual's identification document."""

    name: Name23
    """The individual's name."""

    nationality: Optional[str] = UNSET
    """The individual's nationality."""

    phone: Optional[PhoneNumber2] = UNSET
    """The phone number of the legal entity."""

    residential_address: Address13 = Field(alias="residentialAddress")
    """The residential address of the individual."""

    support: Optional[Support1] = UNSET
    """Support information for the legal entity. Required if you have a platform setup."""

    tax_information: Optional[list[TaxInformation]] = Field(default=UNSET, alias="taxInformation")
    """The tax information of the individual."""

    web_data: Optional[WebData1] = Field(default=UNSET, alias="webData")
    """The website and app URL of the legal entity."""


class Individual1Dict(TypedDict):
    birth_data: NotRequired[BirthData1 | BirthData1Dict]
    email: NotRequired[str]
    identification_data: NotRequired[IdentificationData1 | IdentificationData1Dict]
    name: Name23 | Name23Dict
    nationality: NotRequired[str]
    phone: NotRequired[PhoneNumber2 | PhoneNumber2Dict]
    residential_address: Address13 | Address13Dict
    support: NotRequired[Support1 | Support1Dict]
    tax_information: NotRequired[list[TaxInformation | TaxInformationDict]]
    web_data: NotRequired[WebData1 | WebData1Dict]
