from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.product_type11 import ProductType11OrStr
from .enums.sub_type11 import SubType11OrStr


class PatchableOtherInfo(SdkBaseModel):
    description_of_issue: Optional[str] = Field(default=UNSET, alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **other**."""

    sub_type: Optional[SubType11OrStr] = Field(default=UNSET, alias="subType")
    """The specific category of **other** dispute that you are raising.

    Possible values: **atmDispute**, **cancelledGoodsServices**, **cancelledRecurring**, **counterfeit**,
    **creditNotProcessed**, **notAsDescribed**."""

    what_was_purchased: Optional[ProductType11OrStr] = Field(default=UNSET, alias="whatWasPurchased")
    """The type of product that you purchased.

    Possible values: **goods**, **services**."""


class PatchableOtherInfoDict(TypedDict):
    description_of_issue: NotRequired[str]
    sub_type: NotRequired[SubType11OrStr]
    what_was_purchased: NotRequired[ProductType11OrStr]
