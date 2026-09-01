from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UltimateParentCompanyBusinessDetails(SdkBaseModel):
    legal_business_name: Optional[str] = Field(default=UNSET, alias="legalBusinessName")
    """The legal name of the company."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The registration number of the company."""

    stock_exchange: Optional[str] = Field(default=UNSET, alias="stockExchange")
    """Market Identifier Code (MIC)."""

    stock_number: Optional[str] = Field(default=UNSET, alias="stockNumber")
    """International Securities Identification Number (ISIN)."""

    stock_ticker: Optional[str] = Field(default=UNSET, alias="stockTicker")
    """Stock Ticker symbol."""


class UltimateParentCompanyBusinessDetailsDict(TypedDict):
    legal_business_name: NotRequired[str]
    registration_number: NotRequired[str]
    stock_exchange: NotRequired[str]
    stock_number: NotRequired[str]
    stock_ticker: NotRequired[str]
