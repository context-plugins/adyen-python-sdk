from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason11 import Reason11OrStr
from .enums.status44 import Status44OrStr


class InternalReviewTrackingData(SdkBaseModel):
    reason: Optional[Reason11OrStr] = UNSET
    """The reason why the transfer failed Adyen's internal review.

    Possible values:

    - **refusedForRegulatoryReasons**: the transfer does not comply with Adyen's risk policy. For more information,
        `contact the Support Team <https://www.adyen.help/hc/en-us/requests/new>`__."""

    status: Status44OrStr
    """The status of the transfer.

    Possible values:

     - **pending**: the transfer is under internal review by Adyen.

    - **failed**: the transfer failed Adyen's internal review. For details, see ``reason``."""

    type_: Literal["internalReview"] = Field(default="internalReview", alias="type")
    """The type of tracking event.

    Possible values:

     - **internalReview**: the transfer was flagged because it does not comply with Adyen's risk policy."""


class InternalReviewTrackingDataDict(TypedDict):
    reason: NotRequired[Reason11OrStr]
    status: Status44OrStr
    type_: NotRequired[Literal["internalReview"]]
