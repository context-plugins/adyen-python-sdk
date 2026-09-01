from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssociatedPaymentMethod(SdkBaseModel):
    enabled: bool
    """Indicates whether the payment method is enabled (**true**) or disabled (**false**)."""

    id: str
    """The identifier of the payment method."""

    type_: str = Field(alias="type")
    """Payment method `variant <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__."""


class AssociatedPaymentMethodDict(TypedDict):
    enabled: bool
    id: str
    type_: str
