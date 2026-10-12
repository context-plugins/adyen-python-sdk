from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .three_ds2_result import ThreeDs2Result, ThreeDs2ResultDict


class ThreeDs2ResultResponse(SdkBaseModel):
    three_ds2_result: Optional[ThreeDs2Result] = Field(default=UNSET, alias="threeDS2Result")
    """The result of the 3D Secure 2 authentication."""


class ThreeDs2ResultResponseDict(TypedDict):
    three_ds2_result: NotRequired[ThreeDs2ResultDict]
