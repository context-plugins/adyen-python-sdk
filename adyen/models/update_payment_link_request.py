from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UpdatePaymentLinkRequest(SdkBaseModel):
    status: Literal["expired"] = "expired"
    """Status of the payment link. Possible values:
    * **expired**"""


class UpdatePaymentLinkRequestDict(TypedDict):
    status: NotRequired[Literal["expired"]]
