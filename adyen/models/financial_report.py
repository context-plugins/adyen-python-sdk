from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FinancialReport(SdkBaseModel):
    annual_turnover: Optional[str] = Field(default=UNSET, alias="annualTurnover")
    """The annual turnover of the business."""

    balance_sheet_total: Optional[str] = Field(default=UNSET, alias="balanceSheetTotal")
    """The balance sheet total of the business."""

    currency_of_financial_data: Optional[str] = Field(default=UNSET, alias="currencyOfFinancialData")
    """The currency used for the annual turnover, balance sheet total, and net assets."""

    date_of_financial_data: Optional[str] = Field(default=UNSET, alias="dateOfFinancialData")
    """The date the financial data were provided, in YYYY-MM-DD format."""

    employee_count: Optional[str] = Field(default=UNSET, alias="employeeCount")
    """The number of employees of the business."""

    net_assets: Optional[str] = Field(default=UNSET, alias="netAssets")
    """The net assets of the business."""


class FinancialReportDict(TypedDict):
    annual_turnover: NotRequired[str]
    balance_sheet_total: NotRequired[str]
    currency_of_financial_data: NotRequired[str]
    date_of_financial_data: NotRequired[str]
    employee_count: NotRequired[str]
    net_assets: NotRequired[str]
