from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type311 import Type311OrStr


class CapabilityProblemEntityRecursive1(SdkBaseModel):
    documents: Optional[list[str]] = UNSET
    """List of document IDs corresponding to the verification errors from capabilities."""

    id: Optional[str] = UNSET
    type_: Optional[Type311OrStr] = Field(default=UNSET, alias="type")


class CapabilityProblemEntityRecursive1Dict(TypedDict):
    documents: NotRequired[list[str]]
    id: NotRequired[str]
    type_: NotRequired[Type311OrStr]
