from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.category_data import CategoryData, CategoryDataDict


class TransferView2(SdkBaseModel):
    """Contains information about the transfer related to the transaction."""

    category_data: Optional[CategoryData] = Field(default=UNSET, alias="categoryData")
    """The relevant data according to the transfer category."""

    id: Optional[str] = UNSET
    """The ID of the resource."""

    reference: str
    """The https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference from the
    ``/transfers`` request. If you haven't provided any, Adyen generates a unique reference."""


class TransferView2Dict(TypedDict):
    category_data: NotRequired[CategoryDataDict]
    id: NotRequired[str]
    reference: str
