from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PatchableFraudInfo(SdkBaseModel):
    card_does_not_belong_to_cardholder: Optional[bool] = Field(default=UNSET, alias="cardDoesNotBelongToCardholder")
    """The card is no longer in the cardholder's possession. Set to **true** if the card is lost or stolen."""

    card_was_counterfeited: Optional[bool] = Field(default=UNSET, alias="cardWasCounterfeited")
    """The card was counterfeited."""

    description_of_issue: Optional[str] = Field(default=UNSET, alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **fraud**."""

    report_only: OptionalNullable[bool] = Field(default=UNSET, alias="reportOnly")
    """Set to **true** to report fraud to Adyen with no further action, such as a request for a chargeback or fee
    reversal. The default value is **false**."""


class PatchableFraudInfoDict(TypedDict):
    card_does_not_belong_to_cardholder: NotRequired[bool]
    card_was_counterfeited: NotRequired[bool]
    description_of_issue: NotRequired[str]
    report_only: NotRequired[bool | None]
