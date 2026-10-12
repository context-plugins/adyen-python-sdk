from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account import LoyaltyAccount, LoyaltyAccountDict
from .payment_instrument_data1 import PaymentInstrumentData1, PaymentInstrumentData1Dict
from .poidata1 import Poidata1, Poidata1Dict
from .response11 import Response11, Response11Dict
from .sale_data1 import SaleData1, SaleData1Dict


class CardAcquisitionResponse(SdkBaseModel):
    """It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered
    by the Customer. Content of the Card Acquisition Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    poi_data: Poidata1 = Field(alias="POIData")
    """Data related to the POI System."""

    payment_brand: Optional[list[str]] = Field(default=UNSET, alias="PaymentBrand")
    """Type of payment card. Brands available for payment by the card and not chosen by the Customer."""

    payment_instrument_data: Optional[PaymentInstrumentData1] = Field(default=UNSET, alias="PaymentInstrumentData")
    """Data related to the instrument of payment for the transaction. If this type of payment card is configured to send
    information if the CardAcquisition response."""

    loyalty_account: Optional[list[LoyaltyAccount]] = Field(default=UNSET, alias="LoyaltyAccount")
    """Data related to the loyalty System."""


class CardAcquisitionResponseDict(TypedDict):
    response: Response11Dict
    sale_data: SaleData1Dict
    poi_data: Poidata1Dict
    payment_brand: NotRequired[list[str]]
    payment_instrument_data: NotRequired[PaymentInstrumentData1Dict]
    loyalty_account: NotRequired[list[LoyaltyAccountDict]]
