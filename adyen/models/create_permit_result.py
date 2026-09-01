from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .permit_result import PermitResult, PermitResultDict


class CreatePermitResult(SdkBaseModel):
    permit_result_list: Optional[list[PermitResult]] = Field(default=UNSET, alias="permitResultList")
    """List of new permits."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """A unique reference associated with the request. This value is globally unique; quote it when communicating with
    us about this request."""


class CreatePermitResultDict(TypedDict):
    permit_result_list: NotRequired[list[PermitResult | PermitResultDict]]
    psp_reference: NotRequired[str]
