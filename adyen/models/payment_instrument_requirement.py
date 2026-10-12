from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payment_instrument_type import PaymentInstrumentTypeOrStr


class PaymentInstrumentRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies the requirements for the payment instrument that need to be included in the request for a particular
    route."""

    issuing_country_code: Optional[str] = Field(default=UNSET, alias="issuingCountryCode")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the payment instrument is issued. For example, **NL** or **US**."""

    issuing_country_codes: Optional[list[str]] = Field(default=UNSET, alias="issuingCountryCodes")
    """The two-character ISO-3166-1 alpha-2 country code list for payment instruments."""

    only_for_cross_balance_platform: Optional[bool] = Field(default=UNSET, alias="onlyForCrossBalancePlatform")
    """Specifies if the requirement only applies to transfers to another balance platform."""

    payment_instrument_type: Optional[PaymentInstrumentTypeOrStr] = Field(default=UNSET, alias="paymentInstrumentType")
    """The type of the payment instrument. For example, "BankAccount" or "Card"."""

    type_: Literal["paymentInstrumentRequirement"] = Field(default="paymentInstrumentRequirement", alias="type")
    """**paymentInstrumentRequirement**"""


class PaymentInstrumentRequirementDict(TypedDict):
    description: NotRequired[str]
    issuing_country_code: NotRequired[str]
    issuing_country_codes: NotRequired[list[str]]
    only_for_cross_balance_platform: NotRequired[bool]
    payment_instrument_type: NotRequired[PaymentInstrumentTypeOrStr]
    type_: Literal["paymentInstrumentRequirement"]
