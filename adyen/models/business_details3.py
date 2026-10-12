from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shareholder_contact import ShareholderContact, ShareholderContactDict
from .signatory_contact import SignatoryContact, SignatoryContactDict
from .ultimate_parent_company import UltimateParentCompany, UltimateParentCompanyDict


class BusinessDetails3(SdkBaseModel):
    """Details about the business or nonprofit account holder. Required when creating an account holder with
    ``legalEntity`` **Business** or **NonProfit**."""

    doing_business_as: Optional[str] = Field(default=UNSET, alias="doingBusinessAs")
    """The registered name of the company (if it differs from the legal name of the company)."""

    legal_business_name: Optional[str] = Field(default=UNSET, alias="legalBusinessName")
    """The legal name of the company."""

    listed_ultimate_parent_company: Optional[list[UltimateParentCompany]] = Field(
        default=UNSET, alias="listedUltimateParentCompany"
    )
    """Information about the parent public company. Required if the account holder is 100% owned by a publicly listed
    company."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The registration number of the company."""

    shareholders: Optional[list[ShareholderContact]] = UNSET
    """Array containing information about individuals associated with the account holder either through ownership or
    control. For details about how you can identify them, refer to `our verification guide
    <https://docs.adyen.com/classic-platforms/verification-process#identify-ubos>`__."""

    signatories: Optional[list[SignatoryContact]] = UNSET
    """Signatories associated with the company. Each array entry should represent one signatory."""

    stock_exchange: Optional[str] = Field(default=UNSET, alias="stockExchange")
    """Market Identifier Code (MIC)."""

    stock_number: Optional[str] = Field(default=UNSET, alias="stockNumber")
    """International Securities Identification Number (ISIN)."""

    stock_ticker: Optional[str] = Field(default=UNSET, alias="stockTicker")
    """Stock Ticker symbol."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax ID of the company."""


class BusinessDetails3Dict(TypedDict):
    doing_business_as: NotRequired[str]
    legal_business_name: NotRequired[str]
    listed_ultimate_parent_company: NotRequired[list[UltimateParentCompanyDict]]
    registration_number: NotRequired[str]
    shareholders: NotRequired[list[ShareholderContactDict]]
    signatories: NotRequired[list[SignatoryContactDict]]
    stock_exchange: NotRequired[str]
    stock_number: NotRequired[str]
    stock_ticker: NotRequired[str]
    tax_id: NotRequired[str]
