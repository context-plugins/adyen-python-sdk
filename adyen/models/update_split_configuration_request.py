from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateSplitConfigurationRequest(SdkBaseModel):
    description: str
    """Your description for the split configuration."""


class UpdateSplitConfigurationRequestDict(TypedDict):
    description: str
