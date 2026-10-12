from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .card_acquisition_transaction1 import CardAcquisitionTransaction1, CardAcquisitionTransaction1Dict
from .sale_data1 import SaleData1, SaleData1Dict


class CardAcquisitionRequest2(SdkBaseModel):
    """Content of the Card Acquisition Request message."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    card_acquisition_transaction: CardAcquisitionTransaction1 = Field(alias="CardAcquisitionTransaction")
    """Data related to the payment and loyalty card acquisition."""


class CardAcquisitionRequest2Dict(TypedDict):
    sale_data: SaleData1Dict
    card_acquisition_transaction: CardAcquisitionTransaction1Dict
