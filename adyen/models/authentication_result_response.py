from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .three_ds1_result2 import ThreeDs1Result2, ThreeDs1Result2Dict
from .three_ds2_result import ThreeDs2Result, ThreeDs2ResultDict


class AuthenticationResultResponse(SdkBaseModel):
    three_ds1_result: Optional[ThreeDs1Result2] = Field(default=UNSET, alias="threeDS1Result")
    """The result of the 3D Secure authentication."""

    three_ds2_result: Optional[ThreeDs2Result] = Field(default=UNSET, alias="threeDS2Result")
    """The result of the 3D Secure 2 authentication."""


class AuthenticationResultResponseDict(TypedDict):
    three_ds1_result: NotRequired[ThreeDs1Result2 | ThreeDs1Result2Dict]
    three_ds2_result: NotRequired[ThreeDs2Result | ThreeDs2ResultDict]
