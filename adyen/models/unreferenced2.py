from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Unreferenced2(SdkBaseModel):
    """Settings for unreferenced refunds."""

    enable_unreferenced_refunds: Optional[bool] = Field(default=UNSET, alias="enableUnreferencedRefunds")
    """Indicates whether unreferenced refunds are enabled on the terminal.

    > You're fully liable for losses resulting from fraudulent or duplicate unreferenced refunds. We recommend that you
        `set an unreferenced refund limit and a refund delay
        <https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/unreferenced/#risk-with-unreferenced-refunds>`__
        to reduce this risk."""


class Unreferenced2Dict(TypedDict):
    enable_unreferenced_refunds: NotRequired[bool]
