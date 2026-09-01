from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..confirmation_tracking_data import ConfirmationTrackingData, ConfirmationTrackingDataDict
from ..estimation_tracking_data import EstimationTrackingData, EstimationTrackingDataDict
from ..internal_review_tracking_data import InternalReviewTrackingData, InternalReviewTrackingDataDict

TrackingData: TypeAlias = Annotated[
    ConfirmationTrackingData | EstimationTrackingData | InternalReviewTrackingData, Field(discriminator="type_")
]
"""Additional information for the tracking event."""

TrackingDataDict: TypeAlias = ConfirmationTrackingDataDict | EstimationTrackingDataDict | InternalReviewTrackingDataDict
