from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .split_configuration_rule import SplitConfigurationRule, SplitConfigurationRuleDict


class SplitConfiguration(SdkBaseModel):
    description: str
    """Your description for the split configuration."""

    rules: list[SplitConfigurationRule]
    """Array of rules that define the split configuration behavior."""

    split_configuration_id: Optional[str] = Field(default=UNSET, alias="splitConfigurationId")
    """Unique identifier of the split configuration."""


class SplitConfigurationDict(TypedDict):
    description: str
    rules: list[SplitConfigurationRule | SplitConfigurationRuleDict]
    split_configuration_id: NotRequired[str]
