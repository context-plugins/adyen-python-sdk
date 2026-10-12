from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .geolocation1 import Geolocation1, Geolocation1Dict
from .sensitive_mobile_data1 import SensitiveMobileData1, SensitiveMobileData1Dict


class MobileData(SdkBaseModel):
    """Mobile phone is used as a payment instrument for the transaction. Information related to the mobile for the
    payment transaction."""

    mobile_country_code: Optional[int] = Field(default=UNSET, alias="MobileCountryCode")
    """Identifies the country of a mobile phone operator. If data available."""

    mobile_network_code: Optional[int] = Field(default=UNSET, alias="MobileNetworkCode")
    """Identifies the mobile phone operator inside a country. If data available."""

    masked_msisdn: Optional[int] = Field(default=UNSET, alias="MaskedMSISDN")
    """Masked Mobile Subscriber Integrated Service Digital Network. If data available."""

    geolocation: Optional[Geolocation1] = Field(default=UNSET, alias="Geolocation")
    """Geographic location specified by geographic or UTM coordinates. If data available."""

    protected_mobile_data: Optional[str] = Field(default=UNSET, alias="ProtectedMobileData")
    """Sensitive information related to the mobile phone, protected by CMS. SensitiveMobileData."""

    sensitive_mobile_data: Optional[SensitiveMobileData1] = Field(default=UNSET, alias="SensitiveMobileData")
    """Sensitive information related to the mobile phone. If unprotected mobile data."""


class MobileDataDict(TypedDict):
    mobile_country_code: NotRequired[int]
    mobile_network_code: NotRequired[int]
    masked_msisdn: NotRequired[int]
    geolocation: NotRequired[Geolocation1Dict]
    protected_mobile_data: NotRequired[str]
    sensitive_mobile_data: NotRequired[SensitiveMobileData1Dict]
