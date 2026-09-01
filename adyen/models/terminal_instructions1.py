from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalInstructions1(SdkBaseModel):
    """Settings to define the behaviour of the payment terminal."""

    adyen_app_restart: Optional[bool] = Field(default=UNSET, alias="adyenAppRestart")
    """Indicates whether the Adyen app on the payment terminal restarts automatically when the configuration is
    updated."""


class TerminalInstructions1Dict(TypedDict):
    adyen_app_restart: NotRequired[bool]
