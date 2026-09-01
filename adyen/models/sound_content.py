from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sound_format1 import SoundFormat1OrStr


class SoundContent(SdkBaseModel):
    sound_format: SoundFormat1OrStr = Field(alias="SoundFormat")
    """Possible values:
    * **MessageRef**
    * **SoundRef**
    * **Text**"""

    language: Optional[str] = Field(default=UNSET, alias="Language")
    reference_id: Optional[str] = Field(default=UNSET, alias="ReferenceID")
    text: Optional[str] = Field(default=UNSET, alias="Text")


class SoundContentDict(TypedDict):
    sound_format: SoundFormat1OrStr
    language: NotRequired[str]
    reference_id: NotRequired[str]
    text: NotRequired[str]
