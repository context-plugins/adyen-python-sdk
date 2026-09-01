from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScheduleAccountUpdaterResult(SdkBaseModel):
    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character unique reference associated with the transaction. This value is globally unique; quote it
    when communicating with us about this request."""

    result: str
    """The result of scheduling an Account Updater. If scheduling was successful, this field returns **Success**;
    otherwise it contains the error message."""


class ScheduleAccountUpdaterResultDict(TypedDict):
    psp_reference: str
    result: str
