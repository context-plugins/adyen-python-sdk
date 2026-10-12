from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UkfpsTracingData(SdkBaseModel):
    fpid: str
    """The FPS trace number. This is a unique identifier assigned to transfers processed by `FPS
    <https://www.bankofengland.co.uk/payment-systems/services/faster-payments-service>`__."""

    type_: Literal["ukFps"] = Field(default="ukFps", alias="type")
    """**ukFps**"""


class UkfpsTracingDataDict(TypedDict):
    fpid: str
    type_: Literal["ukFps"]
