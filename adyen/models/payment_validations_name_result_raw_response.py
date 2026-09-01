from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentValidationsNameResultRawResponse(SdkBaseModel):
    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The raw first name validation result that Adyen received from the scheme. First name validation result is only
    returned for Visa."""

    full_name: Optional[str] = Field(default=UNSET, alias="fullName")
    """The raw full name validation result that Adyen received from the scheme. Full name is the only field that is
    validated for Mastercard"""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The raw last name validation result that Adyen received from the scheme. Last name validation result is only
    returned for Visa."""

    middle_name: Optional[str] = Field(default=UNSET, alias="middleName")
    """The raw middle name validation result that Adyen received from the scheme. Middle name validation result is only
    returned for Visa."""

    status: Optional[str] = UNSET
    """The raw name validation status value that Adyen received from the scheme. Only returned for Visa."""


class PaymentValidationsNameResultRawResponseDict(TypedDict):
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    last_name: NotRequired[str]
    middle_name: NotRequired[str]
    status: NotRequired[str]
