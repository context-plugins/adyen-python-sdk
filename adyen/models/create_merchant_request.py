from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateMerchantRequest(SdkBaseModel):
    business_line_id: Optional[str] = Field(default=UNSET, alias="businessLineId")
    """The unique identifier of the `business line
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines>`__. Required for an Adyen for
    Platforms Manage integration."""

    company_id: str = Field(alias="companyId")
    """The unique identifier of the company account."""

    description: Optional[str] = UNSET
    """Your description for the merchant account, maximum 300 characters."""

    legal_entity_id: Optional[str] = Field(default=UNSET, alias="legalEntityId")
    """The unique identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__. Required for an Adyen for
    Platforms Manage integration."""

    pricing_plan: Optional[str] = Field(default=UNSET, alias="pricingPlan")
    """Sets the pricing plan for the merchant account. Required for an Adyen for Platforms Manage integration. Your
    Adyen contact will provide the values that you can use."""

    reference: Optional[str] = UNSET
    """Your reference for the merchant account. To make this reference the unique identifier of the merchant account,
    your Adyen contact can set up a template on your company account. The template can have 6 to 255 characters with
    upper- and lower-case letters, underscores, and numbers. When your company account has a template, then the
    ``reference`` is required and must be unique within the company account."""

    sales_channels: Optional[list[str]] = Field(default=UNSET, alias="salesChannels")
    """List of sales channels that the merchant will process payments with"""


class CreateMerchantRequestDict(TypedDict):
    business_line_id: NotRequired[str]
    company_id: str
    description: NotRequired[str]
    legal_entity_id: NotRequired[str]
    pricing_plan: NotRequired[str]
    reference: NotRequired[str]
    sales_channels: NotRequired[list[str]]
