from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bin_detail1 import BinDetail1, BinDetail1Dict
from .dspublic_key_detail import DspublicKeyDetail, DspublicKeyDetailDict
from .three_ds2_card_range_detail import ThreeDs2CardRangeDetail, ThreeDs2CardRangeDetailDict


class ThreeDsavailabilityResponse(SdkBaseModel):
    bin_details: Optional[BinDetail1] = Field(default=UNSET, alias="binDetails")
    """Bin Group Details"""

    ds_public_keys: Optional[list[DspublicKeyDetail]] = Field(default=UNSET, alias="dsPublicKeys")
    """List of Directory Server (DS) public keys."""

    three_ds1_supported: Optional[bool] = Field(default=UNSET, alias="threeDS1Supported")
    """Indicator if 3D Secure 1 is supported."""

    three_ds2_card_range_details: Optional[list[ThreeDs2CardRangeDetail]] = Field(
        default=UNSET, alias="threeDS2CardRangeDetails"
    )
    """List of brand and card range pairs."""

    three_ds2supported: Optional[bool] = Field(default=UNSET, alias="threeDS2supported")
    """Indicator if 3D Secure 2 is supported."""


class ThreeDsavailabilityResponseDict(TypedDict):
    bin_details: NotRequired[BinDetail1Dict]
    ds_public_keys: NotRequired[list[DspublicKeyDetailDict]]
    three_ds1_supported: NotRequired[bool]
    three_ds2_card_range_details: NotRequired[list[ThreeDs2CardRangeDetailDict]]
    three_ds2supported: NotRequired[bool]
