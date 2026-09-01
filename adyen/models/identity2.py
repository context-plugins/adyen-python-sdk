from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Identity2(SdkBaseModel):
    """Contains the identity details of the party."""

    full_legal_name: str = Field(alias="fullLegalName")
    """The complete legal name of the individual or entity."""

    name: str
    """A commonly used or human-readable name for the individual or entity."""


class Identity2Dict(TypedDict):
    full_legal_name: str
    name: str
