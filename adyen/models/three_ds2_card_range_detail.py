from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ThreeDs2CardRangeDetail(SdkBaseModel):
    acs_info_ind: Optional[list[str]] = Field(default=UNSET, alias="acsInfoInd")
    """Provides additional information to the 3DS Server. Possible values:
    - 01 (Authentication is available at ACS)
    - 02 (Attempts supported by ACS or DS)
    - 03 (Decoupled authentication supported)
    - 04 (Whitelisting supported)"""

    brand_code: Optional[str] = Field(default=UNSET, alias="brandCode")
    """Card brand."""

    end_range: Optional[str] = Field(default=UNSET, alias="endRange")
    """BIN end range."""

    start_range: Optional[str] = Field(default=UNSET, alias="startRange")
    """BIN start range."""

    three_ds2_versions: Optional[list[str]] = Field(default=UNSET, alias="threeDS2Versions")
    """Supported 3D Secure protocol versions"""

    three_ds_method_url: Optional[str] = Field(default=UNSET, alias="threeDSMethodURL")
    """In a 3D Secure 2 browser-based flow, this is the URL where you should send the device fingerprint to."""


class ThreeDs2CardRangeDetailDict(TypedDict):
    acs_info_ind: NotRequired[list[str]]
    brand_code: NotRequired[str]
    end_range: NotRequired[str]
    start_range: NotRequired[str]
    three_ds2_versions: NotRequired[list[str]]
    three_ds_method_url: NotRequired[str]
