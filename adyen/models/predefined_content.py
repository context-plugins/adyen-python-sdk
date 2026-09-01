from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PredefinedContent(SdkBaseModel):
    """Reference of a predefined message to display or print. It conveys information related to the predefined
    message."""

    reference_id: str = Field(alias="ReferenceID")
    """Identification of a predefined message to display or print."""

    language: Optional[str] = Field(default=UNSET, alias="Language")
    """Identification of a language."""


class PredefinedContentDict(TypedDict):
    reference_id: str
    language: NotRequired[str]
