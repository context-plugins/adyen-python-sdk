from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source9 import FundingSource9OrStr
from .input_detail import InputDetail, InputDetailDict
from .payment_method_group2 import PaymentMethodGroup2, PaymentMethodGroup2Dict
from .payment_method_issuer import PaymentMethodIssuer, PaymentMethodIssuerDict
from .payment_method_upiapps import PaymentMethodUpiapps, PaymentMethodUpiappsDict


class PaymentMethod(SdkBaseModel):
    apps: Optional[list[PaymentMethodUpiapps]] = UNSET
    """A list of apps for this payment method."""

    brand: Optional[str] = UNSET
    """Brand for the selected gift card. For example: plastix, hmclub."""

    brands: Optional[list[str]] = UNSET
    """List of possible brands. For example: visa, mc."""

    configuration: Optional[dict[str, str]] = UNSET
    """The configuration of the payment method."""

    funding_source: Optional[FundingSource9OrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source of the payment method."""

    group: Optional[PaymentMethodGroup2] = UNSET
    """The group where this payment method belongs to."""

    input_details: Optional[list[InputDetail]] = Field(default=UNSET, alias="inputDetails")
    """All input details to be provided to complete the payment with this payment method."""

    issuers: Optional[list[PaymentMethodIssuer]] = UNSET
    """A list of issuers for this payment method."""

    name: Optional[str] = UNSET
    """The displayable name of this payment method."""

    promoted: Optional[bool] = UNSET
    """Indicates whether this payment method should be promoted or not."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The unique payment method code."""


class PaymentMethodDict(TypedDict):
    apps: NotRequired[list[PaymentMethodUpiappsDict]]
    brand: NotRequired[str]
    brands: NotRequired[list[str]]
    configuration: NotRequired[dict[str, str]]
    funding_source: NotRequired[FundingSource9OrStr]
    group: NotRequired[PaymentMethodGroup2Dict]
    input_details: NotRequired[list[InputDetailDict]]
    issuers: NotRequired[list[PaymentMethodIssuerDict]]
    name: NotRequired[str]
    promoted: NotRequired[bool]
    type_: NotRequired[str]
