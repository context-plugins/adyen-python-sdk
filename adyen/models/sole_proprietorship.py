from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address41 import Address41, Address41Dict
from .address51 import Address51, Address51Dict
from .enums.vat_absence_reason1 import VatAbsenceReason1OrStr
from .financial_report import FinancialReport, FinancialReportDict
from .tax_information import TaxInformation, TaxInformationDict


class SoleProprietorship(SdkBaseModel):
    country_of_governing_law: str = Field(alias="countryOfGoverningLaw")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
    governing country."""

    date_of_incorporation: Optional[str] = Field(default=UNSET, alias="dateOfIncorporation")
    """The date when the legal arrangement was incorporated in YYYY-MM-DD format."""

    doing_business_as: Optional[str] = Field(default=UNSET, alias="doingBusinessAs")
    """The registered name, if different from the ``name``."""

    doing_business_as_absent: OptionalNullable[bool] = Field(default=UNSET, alias="doingBusinessAsAbsent")
    """Set this to **true** if the legal arrangement does not have a ``Doing business as`` name."""

    financial_reports: Optional[list[FinancialReport]] = Field(default=UNSET, alias="financialReports")
    """The information from the financial report of the sole proprietorship."""

    name: str
    """The legal name."""

    principal_place_of_business: Optional[Address41] = Field(default=UNSET, alias="principalPlaceOfBusiness")
    """The business address. Required if the principal place of business is different from the ``registeredAddress``."""

    registered_address: Address51 = Field(alias="registeredAddress")
    """The address registered at the registrar, such as the Chamber of Commerce."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The registration number."""

    tax_absent: OptionalNullable[bool] = Field(default=UNSET, alias="taxAbsent")
    """The tax information is absent."""

    tax_information: Optional[list[TaxInformation]] = Field(default=UNSET, alias="taxInformation")
    """The tax information of the entity."""

    vat_absence_reason: Optional[VatAbsenceReason1OrStr] = Field(default=UNSET, alias="vatAbsenceReason")
    """The reason for not providing a VAT number.

    Possible values: **industryExemption**, **belowTaxThreshold**."""

    vat_number: Optional[str] = Field(default=UNSET, alias="vatNumber")
    """The VAT number."""


class SoleProprietorshipDict(TypedDict):
    country_of_governing_law: str
    date_of_incorporation: NotRequired[str]
    doing_business_as: NotRequired[str]
    doing_business_as_absent: NotRequired[bool | None]
    financial_reports: NotRequired[list[FinancialReport | FinancialReportDict]]
    name: str
    principal_place_of_business: NotRequired[Address41 | Address41Dict]
    registered_address: Address51 | Address51Dict
    registration_number: NotRequired[str]
    tax_absent: NotRequired[bool | None]
    tax_information: NotRequired[list[TaxInformation | TaxInformationDict]]
    vat_absence_reason: NotRequired[VatAbsenceReason1OrStr]
    vat_number: NotRequired[str]
