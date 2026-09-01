from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sale_data1 import SaleData1, SaleData1Dict
from .stored_value_data import StoredValueData, StoredValueDataDict


class StoredValueRequest2(SdkBaseModel):
    """Content of the Stored Value Request message."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    stored_value_data: list[StoredValueData] = Field(alias="StoredValueData")
    """Data related to the stored value card."""


class StoredValueRequest2Dict(TypedDict):
    sale_data: SaleData1 | SaleData1Dict
    stored_value_data: list[StoredValueData | StoredValueDataDict]
