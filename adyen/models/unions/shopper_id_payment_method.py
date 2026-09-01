from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..pay_to_payment_method import PayToPaymentMethod, PayToPaymentMethodDict
from ..upipayment_method import UpipaymentMethod, UpipaymentMethodDict

ShopperIdPaymentMethod: TypeAlias = Annotated[PayToPaymentMethod | UpipaymentMethod, Field(discriminator="type_")]

ShopperIdPaymentMethodDict: TypeAlias = PayToPaymentMethodDict | UpipaymentMethodDict
