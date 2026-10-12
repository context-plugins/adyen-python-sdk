from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name_location2 import NameLocation2, NameLocation2Dict


class MerchantData(SdkBaseModel):
    acquirer_id: Optional[str] = Field(default=UNSET, alias="acquirerId")
    """The unique identifier of the merchant's acquirer."""

    mcc: Optional[str] = UNSET
    """The merchant category code."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant."""

    name_location: Optional[NameLocation2] = Field(default=UNSET, alias="nameLocation")
    """Contains the name and location of the merchant."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code of the merchant."""


class MerchantDataDict(TypedDict):
    acquirer_id: NotRequired[str]
    mcc: NotRequired[str]
    merchant_id: NotRequired[str]
    name_location: NotRequired[NameLocation2Dict]
    postal_code: NotRequired[str]
