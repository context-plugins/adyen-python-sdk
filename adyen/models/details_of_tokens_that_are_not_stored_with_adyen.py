from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DetailsOfTokensThatAreNotStoredWithAdyen(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The card expiry month. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The card expiry year. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the card holder."""

    number: Optional[str] = UNSET
    """The card number. Only collect raw card data if you are `fully PCI compliant
    <https://docs.adyen.com/development-resources/pci-dss-compliance-guide>`__."""

    stored_payment_method_id: str = Field(alias="storedPaymentMethodId")
    """Identifier used to fetch the token from the external service"""

    subtype: Literal["hilton"] = "hilton"
    """The external service from which to fetch the token. Supported only for specific companies. Contact Adyen if you
    want to use this feature."""

    type_: Literal["externalToken"] = Field(default="externalToken", alias="type")
    """The type of token. Allowed value: **externalToken**."""


class DetailsOfTokensThatAreNotStoredWithAdyenDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    holder_name: NotRequired[str]
    number: NotRequired[str]
    stored_payment_method_id: str
    subtype: Literal["hilton"]
    type_: Literal["externalToken"]
