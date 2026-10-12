from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account_id2 import LoyaltyAccountId2, LoyaltyAccountId2Dict


class LoyaltyAccount(SdkBaseModel):
    """This data structure conveys the identification of the account and the associated loyalty brand. Data related to a
    loyalty account processed in the transaction."""

    loyalty_account_id: LoyaltyAccountId2 = Field(alias="LoyaltyAccountID")
    """Identification of a Loyalty account."""

    loyalty_brand: Optional[str] = Field(default=UNSET, alias="LoyaltyBrand")
    """Identification of a Loyalty brand. If a card is analysed."""


class LoyaltyAccountDict(TypedDict):
    loyalty_account_id: LoyaltyAccountId2Dict
    loyalty_brand: NotRequired[str]
