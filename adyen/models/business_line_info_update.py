from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .source_of_funds11 import SourceOfFunds11, SourceOfFunds11Dict
from .web_data import WebData, WebDataDict
from .web_data_exemption1 import WebDataExemption1, WebDataExemption1Dict


class BusinessLineInfoUpdate(SdkBaseModel):
    industry_code: Optional[str] = Field(default=UNSET, alias="industryCode")
    """A code that represents the industry of your legal entity. For example, **4431A** for computer software stores."""

    industry_code_description: Optional[str] = Field(default=UNSET, alias="industryCodeDescription")
    """The description of the industry code."""

    sales_channels: Optional[list[str]] = Field(default=UNSET, alias="salesChannels")
    """A list of channels where goods or services are sold.

    Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.

    Required only in combination with the ``service`` **paymentProcessing**."""

    source_of_funds: Optional[SourceOfFunds11] = Field(default=UNSET, alias="sourceOfFunds")
    """Contains information about the source of your user's funds. Required only if the ``service`` is **banking** or
    **issuing**."""

    web_data: Optional[list[WebData]] = Field(default=UNSET, alias="webData")
    """List of website URLs where your user's goods or services are sold. When this is required for a service but your
    user does not have an online presence, provide the reason in the ``webDataExemption`` object."""

    web_data_exemption: Optional[WebDataExemption1] = Field(default=UNSET, alias="webDataExemption")
    """The reason why the web data is not provided."""


class BusinessLineInfoUpdateDict(TypedDict):
    industry_code: NotRequired[str]
    industry_code_description: NotRequired[str]
    sales_channels: NotRequired[list[str]]
    source_of_funds: NotRequired[SourceOfFunds11Dict]
    web_data: NotRequired[list[WebDataDict]]
    web_data_exemption: NotRequired[WebDataExemption1Dict]
