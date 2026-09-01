from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FraudInfo1(SdkBaseModel):
    """Additional information for raising a dispute of ``type`` **fraud**. Required for disputes of ``type``
    **fraud**."""

    card_does_not_belong_to_cardholder: bool = Field(alias="cardDoesNotBelongToCardholder")
    """The card is no longer in the cardholder's possession. Set to **true** if the card is lost or stolen."""

    card_was_counterfeited: bool = Field(alias="cardWasCounterfeited")
    """The card was counterfeited."""

    description_of_issue: str = Field(alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **fraud**."""

    report_only: Optional[bool] = Field(default=UNSET, alias="reportOnly")
    """Set to **true** to report fraud to Adyen with no further action, such as a request for a chargeback or fee
    reversal. The default value is **false**."""


class FraudInfo1Dict(TypedDict):
    card_does_not_belong_to_cardholder: bool
    card_was_counterfeited: bool
    description_of_issue: str
    report_only: NotRequired[bool]
