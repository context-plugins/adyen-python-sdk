from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessType(str, Enum):
    """The organization's business type.

    Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**,
    **governmentalOrganization**, **internationalOrganization**, **financialInstitution**."""

    OTHER = "other"
    LISTED_PUBLIC_COMPANY = "listedPublicCompany"
    SUBSIDIARY_OF_LISTED_PUBLIC_COMPANY = "subsidiaryOfListedPublicCompany"
    GOVERNMENTAL_ORGANIZATION = "governmentalOrganization"
    INTERNATIONAL_ORGANIZATION = "internationalOrganization"
    FINANCIAL_INSTITUTION = "financialInstitution"

    __str__ = str.__str__


BusinessTypeOrStr: TypeAlias = Annotated[BusinessType | str, open_enum_validator(BusinessType)]
