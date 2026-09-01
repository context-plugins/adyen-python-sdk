from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.business_type import BusinessTypeOrStr
from .enums.main_source_of_income import MainSourceOfIncomeOrStr
from .enums.type151 import Type151OrStr


class TaxReportingClassification2(SdkBaseModel):
    """The tax reporting classification (FATCA/CRS self-certification) of the organization."""

    business_type: Optional[BusinessTypeOrStr] = Field(default=UNSET, alias="businessType")
    """The organization's business type.

    Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**,
    **governmentalOrganization**, **internationalOrganization**, **financialInstitution**."""

    financial_institution_number: Optional[str] = Field(default=UNSET, alias="financialInstitutionNumber")
    """The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a
    US financial institution and the ``businessType`` is **financialInstitution**."""

    main_source_of_income: Optional[MainSourceOfIncomeOrStr] = Field(default=UNSET, alias="mainSourceOfIncome")
    """The organization's main source of income. Only required if ``businessType`` is **other**.

    Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**,
    **other**."""

    type_: Optional[Type151OrStr] = Field(default=UNSET, alias="type")
    """The tax reporting classification type.

    Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**,
    **nonFinancialPassive**."""


class TaxReportingClassification2Dict(TypedDict):
    business_type: NotRequired[BusinessTypeOrStr]
    financial_institution_number: NotRequired[str]
    main_source_of_income: NotRequired[MainSourceOfIncomeOrStr]
    type_: NotRequired[Type151OrStr]
