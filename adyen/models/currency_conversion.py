from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .converted_amount1 import ConvertedAmount1, ConvertedAmount1Dict


class CurrencyConversion(SdkBaseModel):
    """Information related to a currency conversion. A currency conversion occurred in the payment, and the merchant
    needs to know information related to this conversion (e.g. to print on the sale receipt)."""

    customer_approved_flag: bool = Field(default=True, alias="CustomerApprovedFlag")
    """Notify if the customer has approved something. Indicates if the customer has accepted a currency conversion."""

    converted_amount: ConvertedAmount1 = Field(alias="ConvertedAmount")
    """Amount after a currency conversion."""

    rate: Optional[float] = Field(default=UNSET, alias="Rate")
    """Rate of currency conversion."""

    markup: Optional[float] = Field(default=UNSET, alias="Markup")
    """Markup of a currency conversion amount as a percentage."""

    commission: Optional[float] = Field(default=UNSET, alias="Commission")
    """Commission for a currency conversion."""

    declaration: Optional[str] = Field(default=UNSET, alias="Declaration")
    """Declaration to present to the customer or the cashier for validation. If a declaration has to be presented to the
    customer."""


class CurrencyConversionDict(TypedDict):
    customer_approved_flag: NotRequired[bool]
    converted_amount: ConvertedAmount1Dict
    rate: NotRequired[float]
    markup: NotRequired[float]
    commission: NotRequired[float]
    declaration: NotRequired[str]
