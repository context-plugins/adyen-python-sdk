from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .split_configuration import SplitConfiguration, SplitConfigurationDict


class SplitConfigurationList(SdkBaseModel):
    data: Optional[list[SplitConfiguration]] = UNSET
    """List of split configurations applied to the stores under the merchant account."""


class SplitConfigurationListDict(TypedDict):
    data: NotRequired[list[SplitConfiguration | SplitConfigurationDict]]
