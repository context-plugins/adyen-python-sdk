from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PatchableAmountDto(SdkBaseModel):
    """Required if ``type`` is **business**, **assetSale**, **gamblingWinnings** or **inheritance**.

    For ``type`` **business**, provide the annual turn over of the business. For ``type`` **assetSale**,
    **gamblingWinnings** or **inheritance**, provide the amount of the funds., The amount of the funds the financier
    provided., The maximum amount a card holder can withdraw per day."""

    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    value: Optional[int] = UNSET
    """The amount of the transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""


class PatchableAmountDtoDict(TypedDict):
    currency: NotRequired[str]
    value: NotRequired[int]
