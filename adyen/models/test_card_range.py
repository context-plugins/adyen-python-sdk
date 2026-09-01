from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .avs_address1 import AvsAddress1, AvsAddress1Dict
from .enums.expiry_month import ExpiryMonthOrStr
from .enums.three_ddirectory_server_response import ThreeDdirectoryServerResponseOrStr


class TestCardRange(SdkBaseModel):
    address: Optional[AvsAddress1] = UNSET
    """Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that
    you need to provide at least street address."""

    card_holder_name: str = Field(alias="cardHolderName")
    """The name of the card holder, as it appears on the card, for the test card range."""

    cvc: Optional[str] = UNSET
    """The test card range security code.

    Example: 123"""

    expiry_month: ExpiryMonthOrStr = Field(alias="expiryMonth")
    """Expiry month for the test card range.

    Allowed values:
    * JANUARY
    * FEBRUARY
    * MARCH
    * APRIL
    * MAY
    * JUNE
    * JULY
    * AUGUST
    * SEPTEMBER
    * OCTOBER
    * NOVEMBER
    * DECEMBER"""

    expiry_year: int = Field(alias="expiryYear")
    """Expiry year for the test card range.

    Example: 2020"""

    range_end: str = Field(alias="rangeEnd")
    """The last test card number in the test card range (inclusive):

    * Min 6, max 19 digits
    * BIN compliant
    Example: 5432 1234 1234 4321"""

    range_start: str = Field(alias="rangeStart")
    """The first test card number in the test card range (inclusive):

    * Min 6, max 19 digits
    * BIN compliant
    Example: 5432 1234 1234 1234"""

    three_d_directory_server_response: Optional[ThreeDdirectoryServerResponseOrStr] = Field(
        default=UNSET, alias="threeDDirectoryServerResponse"
    )
    """3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service.
    Possible values:

    * Y (Authentication available)
    * N (Card holder not enrolled/not participating)
    * U (Unable to authenticate)"""

    three_d_password: Optional[str] = Field(default=UNSET, alias="threeDPassword")
    """The password used for 3D Secure authentication."""

    three_d_username: Optional[str] = Field(default=UNSET, alias="threeDUsername")
    """The username used for 3D Secure authentication."""


class TestCardRangeDict(TypedDict):
    address: NotRequired[AvsAddress1 | AvsAddress1Dict]
    card_holder_name: str
    cvc: NotRequired[str]
    expiry_month: ExpiryMonthOrStr
    expiry_year: int
    range_end: str
    range_start: str
    three_d_directory_server_response: NotRequired[ThreeDdirectoryServerResponseOrStr]
    three_d_password: NotRequired[str]
    three_d_username: NotRequired[str]
