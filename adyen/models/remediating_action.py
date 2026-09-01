from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RemediatingAction(SdkBaseModel):
    code: Optional[str] = UNSET
    """The remediating action code."""

    message: Optional[str] = UNSET
    """A description of how you can resolve the verification error."""


class RemediatingActionDict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]
