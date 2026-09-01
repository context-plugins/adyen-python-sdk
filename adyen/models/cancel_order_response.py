from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class CancelOrderResponse(SdkBaseModel):
    psp_reference: str = Field(alias="pspReference")
    """A unique reference of the cancellation request."""

    result_code: Literal["Received"] = Field(default="Received", alias="resultCode")
    """The result of the cancellation request.

    Possible values:

    * **Received** – Indicates the cancellation has successfully been received by Adyen, and will be processed."""


class CancelOrderResponseDict(TypedDict):
    psp_reference: str
    result_code: NotRequired[Literal["Received"]]
