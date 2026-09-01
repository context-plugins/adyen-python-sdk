from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentValidationsNameResultResponse2(SdkBaseModel):
    """Contains the scheme-agnostic match values returned by Adyen."""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """Informs you if the first name your shopper provided matches the cardholder first name on file at the issuing
    bank. The first name is only validated for Visa. Possible values:

    **match**, **partialMatch**, **noMatch**"""

    full_name: Optional[str] = Field(default=UNSET, alias="fullName")
    """Informs you if the full name your shopper provided matches the cardholder name on file at the issuing bank. The
    full name is the only field that is validated for Mastercard. Possible values:

    **match**, **partialMatch**, **noMatch**"""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """Informs you if the last name your shopper provided matches the cardholder last name on file at the issuing bank.
    The last name is only validated for Visa. Possible values:

    **match**, **partialMatch**, **noMatch**"""

    middle_name: Optional[str] = Field(default=UNSET, alias="middleName")
    """Informs you if the middle name your shopper provided matches the cardholder middle name on file at the issuing
    bank. The middle name is only validated for Visa. Possible values:

    **match**, **partialMatch**, **noMatch**"""


class PaymentValidationsNameResultResponse2Dict(TypedDict):
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    last_name: NotRequired[str]
    middle_name: NotRequired[str]
