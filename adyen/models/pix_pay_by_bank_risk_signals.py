from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .confidence_score import ConfidenceScore, ConfidenceScoreDict
from .screen_dimensions import ScreenDimensions, ScreenDimensionsDict


class PixPayByBankRiskSignals(SdkBaseModel):
    confidence_score: Optional[ConfidenceScore] = Field(default=UNSET, alias="confidenceScore")
    elapsed_time_since_boot: Optional[int] = Field(default=UNSET, alias="elapsedTimeSinceBoot")
    is_rooted_device: Optional[bool] = Field(default=UNSET, alias="isRootedDevice")
    language: Optional[str] = UNSET
    os_version: Optional[str] = Field(default=UNSET, alias="osVersion")
    screen_brightness: Optional[int] = Field(default=UNSET, alias="screenBrightness")
    screen_dimensions: Optional[ScreenDimensions] = Field(default=UNSET, alias="screenDimensions")
    user_time_zone_offset: Optional[int] = Field(default=UNSET, alias="userTimeZoneOffset")


class PixPayByBankRiskSignalsDict(TypedDict):
    confidence_score: NotRequired[ConfidenceScore | ConfidenceScoreDict]
    elapsed_time_since_boot: NotRequired[int]
    is_rooted_device: NotRequired[bool]
    language: NotRequired[str]
    os_version: NotRequired[str]
    screen_brightness: NotRequired[int]
    screen_dimensions: NotRequired[ScreenDimensions | ScreenDimensionsDict]
    user_time_zone_offset: NotRequired[int]
