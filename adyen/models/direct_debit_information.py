from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DirectDebitInformation(SdkBaseModel):
    date_of_signature: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dateOfSignature")
    """The date when the direct debit mandate was accepted by your user, in `ISO-8601
    <https://www.w3.org/TR/NOTE-datetime>`__ format."""

    due_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dueDate")
    """The date when the funds are deducted from your user's balance account."""

    mandate_id: Optional[str] = Field(default=UNSET, alias="mandateId")
    """Your unique identifier for the direct debit mandate."""

    sequence_type: Optional[str] = Field(default=UNSET, alias="sequenceType")
    """Identifies the direct debit transfer's type. Possible values: **OneOff**, **First**, **Recurring**, **Final**."""


class DirectDebitInformationDict(TypedDict):
    date_of_signature: NotRequired[RFC3339DateTime]
    due_date: NotRequired[RFC3339DateTime]
    mandate_id: NotRequired[str]
    sequence_type: NotRequired[str]
