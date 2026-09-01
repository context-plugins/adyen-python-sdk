from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem_entity_recursive1 import (
    CapabilityProblemEntityRecursive1,
    CapabilityProblemEntityRecursive1Dict,
)
from .enums.type311 import Type311OrStr


class CapabilityProblemEntity1(SdkBaseModel):
    documents: Optional[list[str]] = UNSET
    """List of document IDs corresponding to the verification errors from capabilities."""

    id: Optional[str] = UNSET
    owner: Optional[CapabilityProblemEntityRecursive1] = UNSET
    type_: Optional[Type311OrStr] = Field(default=UNSET, alias="type")


class CapabilityProblemEntity1Dict(TypedDict):
    documents: NotRequired[list[str]]
    id: NotRequired[str]
    owner: NotRequired[CapabilityProblemEntityRecursive1 | CapabilityProblemEntityRecursive1Dict]
    type_: NotRequired[Type311OrStr]
