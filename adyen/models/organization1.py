from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address22 import Address22, Address22Dict
from .address31 import Address31, Address31Dict
from .enums.institutional_sector import InstitutionalSectorOrStr
from .enums.status_of_legal_proceeding import StatusOfLegalProceedingOrStr
from .enums.type161 import Type161OrStr
from .enums.vat_absence_reason import VatAbsenceReasonOrStr
from .financial_report import FinancialReport, FinancialReportDict
from .phone_number2 import PhoneNumber2, PhoneNumber2Dict
from .stock_data2 import StockData2, StockData2Dict
from .support1 import Support1, Support1Dict
from .tax_information import TaxInformation, TaxInformationDict
from .tax_reporting_classification2 import TaxReportingClassification2, TaxReportingClassification2Dict
from .web_data1 import WebData1, WebData1Dict


class Organization1(SdkBaseModel):
    """Information about the organization. Required if ``type`` is **organization**."""

    country_of_governing_law: Optional[str] = Field(default=UNSET, alias="countryOfGoverningLaw")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the
    governing country."""

    date_of_incorporation: Optional[str] = Field(default=UNSET, alias="dateOfIncorporation")
    """The date when the organization was incorporated in YYYY-MM-DD format."""

    date_of_initiation_of_legal_proceeding: Optional[str] = Field(
        default=UNSET, alias="dateOfInitiationOfLegalProceeding"
    )
    """Required if the value of ``statusOfLegalProceeding`` is one of the following:

    **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**

    The date at which a legal proceeding was initiated, in **YYYY-MM-DD** format. Example: **2000-02-12**"""

    description: Optional[str] = UNSET
    """Your description for the organization."""

    doing_business_as: Optional[str] = Field(default=UNSET, alias="doingBusinessAs")
    """The organization's trading name, if different from the registered legal name."""

    doing_business_as_absent: OptionalNullable[bool] = Field(default=UNSET, alias="doingBusinessAsAbsent")
    """Set this to **true** if the organization or legal arrangement does not have a ``Doing business as`` name."""

    economic_sector: Optional[str] = Field(default=UNSET, alias="economicSector")
    """The sector of the economy the legal entity operates within, represented by a 2-4 digit code that may include a
    ".". Example: 45.11

    You can locate economic sector codes for your area by referencing codes defined by the NACE (Nomenclature of
    Economic Activities) used in the European Union."""

    email: Optional[str] = UNSET
    """The email address of the legal entity."""

    financial_reports: Optional[list[FinancialReport]] = Field(default=UNSET, alias="financialReports")
    """The financial report information of the organization."""

    global_legal_entity_identifier: Optional[str] = Field(default=UNSET, alias="globalLegalEntityIdentifier")
    """The global legal entity identifier for the organization.

    This field is not required if the ``registrationNumber`` for the organization has been provided."""

    head_office_indicator: Optional[bool] = Field(default=UNSET, alias="headOfficeIndicator")
    """Indicates that the registered business address is also the company's headquarters."""

    institutional_sector: Optional[InstitutionalSectorOrStr] = Field(default=UNSET, alias="institutionalSector")
    """The institutional sector the organization operates within."""

    legal_form: Optional[str] = Field(default=UNSET, alias="legalForm")
    """The type of business entity as defined in the national legal system. Use a legal form listed within the accepted
    legal forms compiled by the Central Bank of Europe."""

    legal_name: str = Field(alias="legalName")
    """The organization's legal name."""

    phone: Optional[PhoneNumber2] = UNSET
    """The phone number of the legal entity."""

    principal_place_of_business: Optional[Address22] = Field(default=UNSET, alias="principalPlaceOfBusiness")
    """The address where the organization operates from. Provide this if the principal place of business is different
    from the ``registeredAddress``."""

    registered_address: Address31 = Field(alias="registeredAddress")
    """The address of the organization registered at their registrar (such as the Chamber of Commerce)."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The organization's registration number."""

    registration_number_absent: OptionalNullable[bool] = Field(default=UNSET, alias="registrationNumberAbsent")
    """Set this to **true** if the organization does not have a registration number available. Only applicable for
    organizations in New Zealand, and incorporated partnerships and government organizations in Australia."""

    status_of_legal_proceeding: Optional[StatusOfLegalProceedingOrStr] = Field(
        default=UNSET, alias="statusOfLegalProceeding"
    )
    """The status of any current or past legal action taken against the legal entity.

    Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**,
    **otherLegalMeasures**

    If the value of this field is **noLegalActionsTaken**, then ``dateOfInitiationOfLegalProceeding`` is not required.
    Otherwise, it is required."""

    stock_data: Optional[StockData2] = Field(default=UNSET, alias="stockData")
    """Information about the organization's publicly traded stock. Provide this object only if ``type`` is
    **listedPublicCompany**."""

    support: Optional[Support1] = UNSET
    """Support information for the legal entity. Required if you have a platform setup."""

    tax_information: Optional[list[TaxInformation]] = Field(default=UNSET, alias="taxInformation")
    """The tax information of the organization."""

    tax_reporting_classification: Optional[TaxReportingClassification2] = Field(
        default=UNSET, alias="taxReportingClassification"
    )
    """The tax reporting classification (FATCA/CRS self-certification) of the organization."""

    type_: Optional[Type161OrStr] = Field(default=UNSET, alias="type")
    """Type of organization.

    Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**,
    **partnershipIncorporated**, **privateCompany**."""

    vat_absence_reason: Optional[VatAbsenceReasonOrStr] = Field(default=UNSET, alias="vatAbsenceReason")
    """The reason the organization has not provided a VAT number.

    Possible values: **industryExemption**, **belowTaxThreshold**."""

    vat_number: Optional[str] = Field(default=UNSET, alias="vatNumber")
    """The organization's VAT number."""

    web_data: Optional[WebData1] = Field(default=UNSET, alias="webData")
    """The website and app URL of the legal entity."""


class Organization1Dict(TypedDict):
    country_of_governing_law: NotRequired[str]
    date_of_incorporation: NotRequired[str]
    date_of_initiation_of_legal_proceeding: NotRequired[str]
    description: NotRequired[str]
    doing_business_as: NotRequired[str]
    doing_business_as_absent: NotRequired[bool | None]
    economic_sector: NotRequired[str]
    email: NotRequired[str]
    financial_reports: NotRequired[list[FinancialReportDict]]
    global_legal_entity_identifier: NotRequired[str]
    head_office_indicator: NotRequired[bool]
    institutional_sector: NotRequired[InstitutionalSectorOrStr]
    legal_form: NotRequired[str]
    legal_name: str
    phone: NotRequired[PhoneNumber2Dict]
    principal_place_of_business: NotRequired[Address22Dict]
    registered_address: Address31Dict
    registration_number: NotRequired[str]
    registration_number_absent: NotRequired[bool | None]
    status_of_legal_proceeding: NotRequired[StatusOfLegalProceedingOrStr]
    stock_data: NotRequired[StockData2Dict]
    support: NotRequired[Support1Dict]
    tax_information: NotRequired[list[TaxInformationDict]]
    tax_reporting_classification: NotRequired[TaxReportingClassification2Dict]
    type_: NotRequired[Type161OrStr]
    vat_absence_reason: NotRequired[VatAbsenceReasonOrStr]
    vat_number: NotRequired[str]
    web_data: NotRequired[WebData1Dict]
