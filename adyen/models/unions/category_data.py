from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..bank_category_data import BankCategoryData, BankCategoryDataDict
from ..internal_category_data import InternalCategoryData, InternalCategoryDataDict
from ..issued_card import IssuedCard, IssuedCardDict
from ..platform_payment import PlatformPayment, PlatformPaymentDict

CategoryData: TypeAlias = Annotated[
    BankCategoryData | InternalCategoryData | IssuedCard | PlatformPayment, Field(discriminator="type_")
]
"""The relevant data according to the transfer category."""

CategoryDataDict: TypeAlias = BankCategoryDataDict | InternalCategoryDataDict | IssuedCardDict | PlatformPaymentDict
