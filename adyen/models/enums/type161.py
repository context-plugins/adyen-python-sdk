from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type161(str, Enum):
    """Type of organization.

    Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**,
    **partnershipIncorporated**, **privateCompany**."""

    ASSOCIATION_INCORPORATED = "associationIncorporated"
    GOVERNMENTAL_ORGANIZATION = "governmentalOrganization"
    LISTED_PUBLIC_COMPANY = "listedPublicCompany"
    NON_PROFIT = "nonProfit"
    PARTNERSHIP_INCORPORATED = "partnershipIncorporated"
    PRIVATE_COMPANY = "privateCompany"

    __str__ = str.__str__


Type161OrStr: TypeAlias = Annotated[Type161 | str, open_enum_validator(Type161)]
