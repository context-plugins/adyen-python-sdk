from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type_code1 import TypeCode1OrStr
from .track_data1 import TrackData1, TrackData1Dict


class CheckData(SdkBaseModel):
    """Information related to the paper check used for the transaction. Allows the check information to be provided by
    the Sale System before requesting the payment, or stored by the Sale System after processing of the payment."""

    bank_id: Optional[str] = Field(default=UNSET, alias="BankID")
    """Identification of the bank. Mandatory if TrackData absent."""

    account_number: Optional[str] = Field(default=UNSET, alias="AccountNumber")
    """Identification of the customer account. Mandatory if TrackData absent."""

    check_number: Optional[str] = Field(default=UNSET, alias="CheckNumber")
    """Identification of the bank check. Mandatory if TrackData absent."""

    track_data: Optional[TrackData1] = Field(default=UNSET, alias="TrackData")
    """Magnetic track or magnetic ink characters line. Mandatory if CheckNumber absent."""

    check_card_number: Optional[str] = Field(default=UNSET, alias="CheckCardNumber")
    """Check guarantee card number. If provided by the customer."""

    type_code: Optional[TypeCode1OrStr] = Field(default=UNSET, alias="TypeCode")
    """Type of bank check. Possible values:
    * **Company**
    * **Personal**"""

    country: Optional[str] = Field(default=UNSET, alias="Country")
    """Country of the bank check. Absent if country of the Sale system."""


class CheckDataDict(TypedDict):
    bank_id: NotRequired[str]
    account_number: NotRequired[str]
    check_number: NotRequired[str]
    track_data: NotRequired[TrackData1Dict]
    check_card_number: NotRequired[str]
    type_code: NotRequired[TypeCode1OrStr]
    country: NotRequired[str]
