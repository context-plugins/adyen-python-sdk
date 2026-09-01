from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BirthData1(SdkBaseModel):
    """The individual's birth information."""

    date_of_birth: Optional[str] = Field(default=UNSET, alias="dateOfBirth")
    """The individual's date of birth, in YYYY-MM-DD format."""


class BirthData1Dict(TypedDict):
    date_of_birth: NotRequired[str]
