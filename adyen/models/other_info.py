from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.product_type11 import ProductType11OrStr
from .enums.sub_type11 import SubType11OrStr


class OtherInfo(SdkBaseModel):
    description_of_issue: str = Field(alias="descriptionOfIssue")
    """Your description of the issue for raising a dispute of ``type`` **other**."""

    sub_type: SubType11OrStr = Field(alias="subType")
    """The specific category of **other** dispute that you are raising.

    Possible values: **atmDispute**, **cancelledGoodsServices**, **cancelledRecurring**, **counterfeit**,
    **creditNotProcessed**, **notAsDescribed**."""

    what_was_purchased: ProductType11OrStr = Field(alias="whatWasPurchased")
    """The type of product that you purchased.

    Possible values: **goods**, **services**."""


class OtherInfoDict(TypedDict):
    description_of_issue: str
    sub_type: SubType11OrStr
    what_was_purchased: ProductType11OrStr
