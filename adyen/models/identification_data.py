from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type132 import Type132OrStr


class IdentificationData(SdkBaseModel):
    card_number: Optional[str] = Field(default=UNSET, alias="cardNumber")
    """The card number of the document that was issued (AU only)."""

    expiry_date: Optional[str] = Field(default=UNSET, alias="expiryDate")
    """The expiry date of the document, in YYYY-MM-DD format."""

    issuer_country: Optional[str] = Field(default=UNSET, alias="issuerCountry")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the document was issued. For example, **US**."""

    issuer_state: Optional[str] = Field(default=UNSET, alias="issuerState")
    """The state or province where the document was issued (AU only)."""

    national_id_exempt: Optional[bool] = Field(default=UNSET, alias="nationalIdExempt")
    """Applies only to individuals in the US. Set to **true** if the individual does not have an SSN. To verify their
    identity, Adyen will require them to upload an ID document."""

    number: Optional[str] = UNSET
    """The number in the document."""

    type_: Type132OrStr = Field(alias="type")
    """Type of identity data. For individuals, the following types are supported. See our `onboarding guide
    <https://docs.adyen.com/platforms/onboard-users/onboarding-steps/?onboarding_type=custom>`__ for other supported
    countries.

    - Australia: **driversLicense**, **passport**

    - Hong Kong: **driversLicense**, **nationalIdNumber**, **passport**

    - New Zealand: **driversLicense**, **passport**

    - Singapore: **driversLicense**, **nationalIdNumber**, **passport**

    - All other supported countries: **nationalIdNumber**"""


class IdentificationDataDict(TypedDict):
    card_number: NotRequired[str]
    expiry_date: NotRequired[str]
    issuer_country: NotRequired[str]
    issuer_state: NotRequired[str]
    national_id_exempt: NotRequired[bool]
    number: NotRequired[str]
    type_: Type132OrStr
