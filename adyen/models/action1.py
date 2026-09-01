from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Action1(SdkBaseModel):
    action_code: str = Field(alias="actionCode")
    """The code identifying the action that needs to be completed."""

    resolved: bool
    """Indicates whether this action has been successfully completed."""


class Action1Dict(TypedDict):
    action_code: str
    resolved: bool
