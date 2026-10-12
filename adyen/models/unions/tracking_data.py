from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..confirmation_tracking_data import ConfirmationTrackingData, ConfirmationTrackingDataDict
from ..estimation_tracking_data import EstimationTrackingData, EstimationTrackingDataDict
from ..internal_review_tracking_data import InternalReviewTrackingData, InternalReviewTrackingDataDict

TrackingData: TypeAlias = Annotated[
    (
        Annotated[ConfirmationTrackingData, Tag("confirmation")]
        | Annotated[EstimationTrackingData, Tag("estimation")]
        | Annotated[InternalReviewTrackingData, Tag("internalReview")]
    ),
    WireDiscriminator("type"),
]
"""Additional information for the tracking event."""

TrackingDataDict: TypeAlias = ConfirmationTrackingDataDict | EstimationTrackingDataDict | InternalReviewTrackingDataDict
