from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SensitiveMobileData(SdkBaseModel):
    msisdn: int = Field(alias="MSISDN")
    """Mobile Subscriber Integrated Service Digital Network (i.e. mobile phone number of the SIM card). Country,
    National Destination Code, and Subscriber Number."""

    imsi: Optional[int] = Field(default=UNSET, alias="IMSI")
    """International Mobile Subscriber Identity. Unique number associated with the mobile phone user, containing the
    Mobile Country Code (MCC), the Mobile Network Code (MNC), and the Mobile Identification Number (MSIN)"""

    imei: Optional[int] = Field(default=UNSET, alias="IMEI")
    """International Mobile Equipment Identity. Unique number associated with the mobile phone device."""


class SensitiveMobileDataDict(TypedDict):
    msisdn: int
    imsi: NotRequired[int]
    imei: NotRequired[int]
