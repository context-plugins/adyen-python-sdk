from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .delegated_authentication_data1 import DelegatedAuthenticationData1, DelegatedAuthenticationData1Dict


class RegisterScarequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the SCA device that you are registering. You can use it to help your users identify the device.

    If you do not specify a ``name``, Adyen automatically generates one."""

    payment_instrument_id: str = Field(alias="paymentInstrumentId")
    """The unique identifier of the payment instrument for which you are registering the SCA device."""

    strong_customer_authentication: DelegatedAuthenticationData1 = Field(alias="strongCustomerAuthentication")
    """Contains information required to register the SCA device."""


class RegisterScarequestDict(TypedDict):
    name: NotRequired[str]
    payment_instrument_id: str
    strong_customer_authentication: DelegatedAuthenticationData1 | DelegatedAuthenticationData1Dict
