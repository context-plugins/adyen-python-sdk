from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type411 import Type411, Type411OrStr


class InternalCategoryData(SdkBaseModel):
    modification_merchant_reference: Optional[str] = Field(default=UNSET, alias="modificationMerchantReference")
    """The capture's merchant reference included in the transfer."""

    modification_psp_reference: Optional[str] = Field(default=UNSET, alias="modificationPspReference")
    """The capture reference included in the transfer."""

    type_: Type411OrStr = Field(default=Type411.INTERNAL, alias="type")
    """**internal**"""


class InternalCategoryDataDict(TypedDict):
    modification_merchant_reference: NotRequired[str]
    modification_psp_reference: NotRequired[str]
    type_: NotRequired[Type411OrStr]
