from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..pay_to_payment_method import PayToPaymentMethod, PayToPaymentMethodDict
from ..upipayment_method import UpipaymentMethod, UpipaymentMethodDict

ShopperIdPaymentMethod: TypeAlias = Annotated[
    Annotated[PayToPaymentMethod, Tag("payTo")] | Annotated[UpipaymentMethod, Tag("upi_collect")],
    WireDiscriminator("type"),
]

ShopperIdPaymentMethodDict: TypeAlias = PayToPaymentMethodDict | UpipaymentMethodDict
