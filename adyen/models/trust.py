from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address41 import Address41, Address41Dict
from .address51 import Address51, Address51Dict
from .enums.type171 import Type171OrStr
from .enums.vat_absence_reason1 import VatAbsenceReason1OrStr
from .tax_information import TaxInformation, TaxInformationDict
from .undefined_beneficiary import UndefinedBeneficiary, UndefinedBeneficiaryDict


class Trust(SdkBaseModel):
    country_of_governing_law: str = Field(alias="countryOfGoverningLaw")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
    governing country."""

    date_of_incorporation: Optional[str] = Field(default=UNSET, alias="dateOfIncorporation")
    """The date when the legal arrangement was incorporated in YYYY-MM-DD format."""

    description: Optional[str] = UNSET
    """A short description about the trust. Only applicable for charitable trusts in New Zealand."""

    doing_business_as: Optional[str] = Field(default=UNSET, alias="doingBusinessAs")
    """The registered name, if different from the ``name``."""

    doing_business_as_absent: OptionalNullable[bool] = Field(default=UNSET, alias="doingBusinessAsAbsent")
    """Set this to **true** if the legal arrangement does not have a ``Doing business as`` name."""

    name: str
    """The legal name."""

    principal_place_of_business: Optional[Address41] = Field(default=UNSET, alias="principalPlaceOfBusiness")
    """The business address. Required if the principal place of business is different from the ``registeredAddress``."""

    registered_address: Address51 = Field(alias="registeredAddress")
    """The address registered at the registrar, such as the Chamber of Commerce."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The registration number."""

    tax_information: Optional[list[TaxInformation]] = Field(default=UNSET, alias="taxInformation")
    """The tax information of the entity."""

    type_: Type171OrStr = Field(alias="type")
    """Type of trust.

    See possible values for trusts in `Australia
    <https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-australia>`__ and `New
    Zealand
    <https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-new-zealand>`__."""

    undefined_beneficiary_info: Optional[list[UndefinedBeneficiary]] = Field(
        default=UNSET, alias="undefinedBeneficiaryInfo"
    )
    """The undefined beneficiary information of the entity."""

    vat_absence_reason: Optional[VatAbsenceReason1OrStr] = Field(default=UNSET, alias="vatAbsenceReason")
    """The reason for not providing a VAT number.

    Possible values: **industryExemption**, **belowTaxThreshold**."""

    vat_number: Optional[str] = Field(default=UNSET, alias="vatNumber")
    """The VAT number."""


class TrustDict(TypedDict):
    country_of_governing_law: str
    date_of_incorporation: NotRequired[str]
    description: NotRequired[str]
    doing_business_as: NotRequired[str]
    doing_business_as_absent: NotRequired[bool | None]
    name: str
    principal_place_of_business: NotRequired[Address41 | Address41Dict]
    registered_address: Address51 | Address51Dict
    registration_number: NotRequired[str]
    tax_information: NotRequired[list[TaxInformation | TaxInformationDict]]
    type_: Type171OrStr
    undefined_beneficiary_info: NotRequired[list[UndefinedBeneficiary | UndefinedBeneficiaryDict]]
    vat_absence_reason: NotRequired[VatAbsenceReason1OrStr]
    vat_number: NotRequired[str]
