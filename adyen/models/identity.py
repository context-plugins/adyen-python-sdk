from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Identity(SdkBaseModel):
    full_legal_name: str = Field(alias="fullLegalName")
    """The complete legal name of the individual or entity."""

    name: str
    """A commonly used or human-readable name for the individual or entity."""


class IdentityDict(TypedDict):
    full_legal_name: str
    name: str
