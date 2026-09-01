from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShowPages2(SdkBaseModel):
    """Contains indicators whether specific pages must be shown to the account holder."""

    bank_details_summary_page: Optional[bool] = Field(default=UNSET, alias="bankDetailsSummaryPage")
    """Indicates whether the page with bank account details must be shown. Defaults to **true**."""

    bank_verification_page: Optional[bool] = Field(default=UNSET, alias="bankVerificationPage")
    """Indicates whether the bank check instant verification' details must be shown. Defaults to **true**."""

    business_details_summary_page: Optional[bool] = Field(default=UNSET, alias="businessDetailsSummaryPage")
    """Indicates whether the page with the company's or organization's details must be shown. Defaults to **true**."""

    checks_overview_page: Optional[bool] = Field(default=UNSET, alias="checksOverviewPage")
    """Indicates whether the checks overview page must be shown. Defaults to **false**."""

    individual_details_summary_page: Optional[bool] = Field(default=UNSET, alias="individualDetailsSummaryPage")
    """Indicates whether the page with the individual's details must be shown. Defaults to **true**."""

    legal_arrangements_details_summary_page: Optional[bool] = Field(
        default=UNSET, alias="legalArrangementsDetailsSummaryPage"
    )
    """Indicates whether the page with the legal arrangements' details must be shown. Defaults to **true**."""

    manual_bank_account_page: Optional[bool] = Field(default=UNSET, alias="manualBankAccountPage")
    """Indicates whether the page to manually add bank account' details must be shown. Defaults to **true**."""

    shareholder_details_summary_page: Optional[bool] = Field(default=UNSET, alias="shareholderDetailsSummaryPage")
    """Indicates whether the page with the shareholders' details must be shown. Defaults to **true**."""

    welcome_page: Optional[bool] = Field(default=UNSET, alias="welcomePage")
    """Indicates whether the welcome page must be shown. Defaults to **false**."""


class ShowPages2Dict(TypedDict):
    bank_details_summary_page: NotRequired[bool]
    bank_verification_page: NotRequired[bool]
    business_details_summary_page: NotRequired[bool]
    checks_overview_page: NotRequired[bool]
    individual_details_summary_page: NotRequired[bool]
    legal_arrangements_details_summary_page: NotRequired[bool]
    manual_bank_account_page: NotRequired[bool]
    shareholder_details_summary_page: NotRequired[bool]
    welcome_page: NotRequired[bool]
