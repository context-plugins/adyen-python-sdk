from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.authentication_method import AuthenticationMethodOrStr
from .enums.payment_instrument import PaymentInstrumentOrStr


class PayAtTable(SdkBaseModel):
    authentication_method: Optional[AuthenticationMethodOrStr] = Field(default=UNSET, alias="authenticationMethod")
    """Allowed authentication methods: Magswipe, Manual Entry."""

    enable_pay_at_table: Optional[bool] = Field(default=UNSET, alias="enablePayAtTable")
    """Enable Pay at table."""

    payment_instrument: OptionalNullable[PaymentInstrumentOrStr] = Field(default=UNSET, alias="paymentInstrument")
    """Sets the allowed payment instrument for Pay at table transactions. Can be: **cash** or **card**. If not set, the
    terminal presents both options."""


class PayAtTableDict(TypedDict):
    authentication_method: NotRequired[AuthenticationMethodOrStr]
    enable_pay_at_table: NotRequired[bool]
    payment_instrument: NotRequired[PaymentInstrumentOrStr | None]
