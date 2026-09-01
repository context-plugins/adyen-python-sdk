from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status13 import Status13OrStr


class PinChangeResponse(SdkBaseModel):
    status: Status13OrStr
    """The status of the request for PIN change.

    Possible values: **completed**, **pending**, **unavailable**."""


class PinChangeResponseDict(TypedDict):
    status: Status13OrStr
