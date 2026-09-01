from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem_entity_recursive2 import (
    CapabilityProblemEntityRecursive2,
    CapabilityProblemEntityRecursive2Dict,
)
from .enums.type33 import Type33OrStr


class CapabilityProblemEntity(SdkBaseModel):
    documents: Optional[list[str]] = UNSET
    """List of document IDs to which the verification errors related to the capabilities correspond to."""

    id: Optional[str] = UNSET
    """The ID of the entity."""

    owner: Optional[CapabilityProblemEntityRecursive2] = UNSET
    """Contains details about the owner of the entity that has an error."""

    type_: Optional[Type33OrStr] = Field(default=UNSET, alias="type")
    """Type of entity.

    Possible values: **LegalEntity**, **BankAccount**, **Document**."""


class CapabilityProblemEntityDict(TypedDict):
    documents: NotRequired[list[str]]
    id: NotRequired[str]
    owner: NotRequired[CapabilityProblemEntityRecursive2 | CapabilityProblemEntityRecursive2Dict]
    type_: NotRequired[Type33OrStr]
