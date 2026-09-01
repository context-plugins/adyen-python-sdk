from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubjectErasureByPspReferenceRequest(SdkBaseModel):
    force_erasure: Optional[bool] = Field(default=UNSET, alias="forceErasure")
    """Set this to **true** if you want to delete shopper-related data, even if the shopper has an existing recurring
    transaction. This only deletes the shopper-related data for the specific payment, but does not cancel the existing
    recurring transaction."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """Your merchant account"""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The PSP reference of the payment. We will delete all shopper-related data for this payment."""


class SubjectErasureByPspReferenceRequestDict(TypedDict):
    force_erasure: NotRequired[bool]
    merchant_account: NotRequired[str]
    psp_reference: NotRequired[str]
