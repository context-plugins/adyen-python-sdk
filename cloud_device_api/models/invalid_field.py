from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InvalidField(SdkBaseModel):
    name: str
    """The field that has an invalid value."""

    value: str
    """The invalid value."""

    message: str
    """Description of the validation error."""


class InvalidFieldDict(TypedDict):
    name: str
    value: str
    message: str
