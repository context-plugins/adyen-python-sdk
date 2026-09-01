from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .minor_units_monetary_value import MinorUnitsMonetaryValue, MinorUnitsMonetaryValueDict
from .supported_card_types2 import SupportedCardTypes2, SupportedCardTypes2Dict


class StoreAndForward1(SdkBaseModel):
    """Settings for store-and-forward offline payments. The ``maxAmount``, ``maxPayments``, and ``supportedCardTypes``
    parameters must be configured, either in the request or inherited from a higher level in your account structure."""

    max_amount: Optional[list[MinorUnitsMonetaryValue]] = Field(default=UNSET, alias="maxAmount")
    """The maximum amount that the terminal accepts for a single store-and-forward payment."""

    max_payments: Optional[int] = Field(default=UNSET, alias="maxPayments")
    """The maximum number of store-and-forward transactions per terminal that you can process while offline."""

    supported_card_types: Optional[SupportedCardTypes2] = Field(default=UNSET, alias="supportedCardTypes")
    """The type of card for which the terminal accepts store-and-forward payments. You can specify multiple card
    types."""


class StoreAndForward1Dict(TypedDict):
    max_amount: NotRequired[list[MinorUnitsMonetaryValue | MinorUnitsMonetaryValueDict]]
    max_payments: NotRequired[int]
    supported_card_types: NotRequired[SupportedCardTypes2 | SupportedCardTypes2Dict]
