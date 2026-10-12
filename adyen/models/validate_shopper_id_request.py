from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shopper_id_payment_method1 import ShopperIdPaymentMethod1, ShopperIdPaymentMethod1Dict


class ValidateShopperIdRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    payment_method: ShopperIdPaymentMethod1 = Field(alias="paymentMethod")
    """paymentMethod"""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    shopper_ip: Optional[str] = Field(default=UNSET, alias="shopperIP")
    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")


class ValidateShopperIdRequestDict(TypedDict):
    merchant_account: str
    payment_method: ShopperIdPaymentMethod1Dict
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_reference: NotRequired[str]
