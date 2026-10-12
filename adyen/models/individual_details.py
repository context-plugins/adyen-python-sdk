from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vias_name2 import ViasName2, ViasName2Dict
from .vias_personal_data2 import ViasPersonalData2, ViasPersonalData2Dict


class IndividualDetails(SdkBaseModel):
    name: Optional[ViasName2] = UNSET
    """The name of the individual. >Make sure your account holder registers using the name shown on their Photo ID.
     Maximum length: 80 characters
     Cannot contain numbers. /n Cannot be empty."""

    personal_data: Optional[ViasPersonalData2] = Field(default=UNSET, alias="personalData")
    """Personal information of the individual."""


class IndividualDetailsDict(TypedDict):
    name: NotRequired[ViasName2Dict]
    personal_data: NotRequired[ViasPersonalData2Dict]
