from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type33 import Type33OrStr


class CapabilityProblemEntityRecursive2(SdkBaseModel):
    """Contains details about the owner of the entity that has an error."""

    documents: Optional[list[str]] = UNSET
    """List of document IDs to which the verification errors related to the capabilities correspond to."""

    id: Optional[str] = UNSET
    """The ID of the entity."""

    type_: Optional[Type33OrStr] = Field(default=UNSET, alias="type")
    """Type of entity.

    Possible values: **LegalEntity**, **BankAccount**, **Document**."""


class CapabilityProblemEntityRecursive2Dict(TypedDict):
    documents: NotRequired[list[str]]
    id: NotRequired[str]
    type_: NotRequired[Type33OrStr]
