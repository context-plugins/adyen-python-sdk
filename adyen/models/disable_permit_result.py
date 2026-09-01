from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DisablePermitResult(SdkBaseModel):
    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """A unique reference associated with the request. This value is globally unique; quote it when communicating with
    us about this request."""

    status: Optional[str] = UNSET
    """Status of the disable request."""


class DisablePermitResultDict(TypedDict):
    psp_reference: NotRequired[str]
    status: NotRequired[str]
