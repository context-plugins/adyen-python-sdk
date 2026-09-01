from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ultimate_parent_company_business_details2 import (
    UltimateParentCompanyBusinessDetails2,
    UltimateParentCompanyBusinessDetails2Dict,
)
from .vias_address1 import ViasAddress1, ViasAddress1Dict


class UltimateParentCompany(SdkBaseModel):
    address: Optional[ViasAddress1] = UNSET
    """Address of the ultimate parent company."""

    business_details: Optional[UltimateParentCompanyBusinessDetails2] = Field(default=UNSET, alias="businessDetails")
    """Details about the ultimate parent company's business."""

    ultimate_parent_company_code: Optional[str] = Field(default=UNSET, alias="ultimateParentCompanyCode")
    """Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an
    ultimate parent company. Required when updating an existing entry in an ``/updateAccountHolder`` request."""


class UltimateParentCompanyDict(TypedDict):
    address: NotRequired[ViasAddress1 | ViasAddress1Dict]
    business_details: NotRequired[UltimateParentCompanyBusinessDetails2 | UltimateParentCompanyBusinessDetails2Dict]
    ultimate_parent_company_code: NotRequired[str]
