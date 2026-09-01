from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StockData2(SdkBaseModel):
    """Information about the organization's publicly traded stock. Provide this object only if ``type`` is
    **listedPublicCompany**."""

    market_identifier: Optional[str] = Field(default=UNSET, alias="marketIdentifier")
    """The four-digit `Market Identifier Code <https://en.wikipedia.org/wiki/Market_Identifier_Code>`__ of the stock
    market where the organization's stocks are traded."""

    stock_number: Optional[str] = Field(default=UNSET, alias="stockNumber")
    """The 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-)."""

    ticker_symbol: Optional[str] = Field(default=UNSET, alias="tickerSymbol")
    """The stock ticker symbol."""


class StockData2Dict(TypedDict):
    market_identifier: NotRequired[str]
    stock_number: NotRequired[str]
    ticker_symbol: NotRequired[str]
