from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service import ServiceOrStr
from .source_of_funds11 import SourceOfFunds11, SourceOfFunds11Dict
from .web_data import WebData, WebDataDict
from .web_data_exemption1 import WebDataExemption1, WebDataExemption1Dict


class BusinessLineInfo(SdkBaseModel):
    industry_code: str = Field(alias="industryCode")
    """A code that represents the industry of the legal entity for `marketplaces
    <https://docs.adyen.com/marketplaces/verification-requirements/reference-additional-products/#list-industry-codes>`__
    or `platforms
    <https://docs.adyen.com/platforms/verification-requirements/reference-additional-products/#list-industry-codes>`__.
    For example, **4431A** for computer software stores."""

    industry_code_description: Optional[str] = Field(default=UNSET, alias="industryCodeDescription")
    """The description of the industry code."""

    legal_entity_id: str = Field(alias="legalEntityId")
    """Unique identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id>`__ that owns the business
    line."""

    sales_channels: Optional[list[str]] = Field(default=UNSET, alias="salesChannels")
    """A list of channels where goods or services are sold.

    Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.

    Required only in combination with the ``service`` **paymentProcessing**."""

    service: ServiceOrStr
    """The service for which you are creating the business line.



    Possible values:
    * **paymentProcessing**
    * **issuing**
    * **banking**"""

    source_of_funds: Optional[SourceOfFunds11] = Field(default=UNSET, alias="sourceOfFunds")
    """Contains information about the source of your user's funds. Required only if the ``service`` is **banking** or
    **issuing**."""

    web_data: Optional[list[WebData]] = Field(default=UNSET, alias="webData")
    """List of website URLs where your user's goods or services are sold. When this is required for a service but your
    user does not have an online presence, provide the reason in the ``webDataExemption`` object."""

    web_data_exemption: Optional[WebDataExemption1] = Field(default=UNSET, alias="webDataExemption")
    """The reason why the web data is not provided."""


class BusinessLineInfoDict(TypedDict):
    industry_code: str
    industry_code_description: NotRequired[str]
    legal_entity_id: str
    sales_channels: NotRequired[list[str]]
    service: ServiceOrStr
    source_of_funds: NotRequired[SourceOfFunds11 | SourceOfFunds11Dict]
    web_data: NotRequired[list[WebData | WebDataDict]]
    web_data_exemption: NotRequired[WebDataExemption1 | WebDataExemption1Dict]
