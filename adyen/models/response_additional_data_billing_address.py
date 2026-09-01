from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataBillingAddress(SdkBaseModel):
    billing_address_city: Optional[str] = Field(default=UNSET, alias="billingAddress.city")
    """The billing address city passed in the payment request."""

    billing_address_country: Optional[str] = Field(default=UNSET, alias="billingAddress.country")
    """The billing address country passed in the payment request.

    Example: NL"""

    billing_address_house_number_or_name: Optional[str] = Field(default=UNSET, alias="billingAddress.houseNumberOrName")
    """The billing address house number or name passed in the payment request."""

    billing_address_postal_code: Optional[str] = Field(default=UNSET, alias="billingAddress.postalCode")
    """The billing address postal code passed in the payment request.

    Example: 1011 DJ"""

    billing_address_state_or_province: Optional[str] = Field(default=UNSET, alias="billingAddress.stateOrProvince")
    """The billing address state or province passed in the payment request.

    Example: NH"""

    billing_address_street: Optional[str] = Field(default=UNSET, alias="billingAddress.street")
    """The billing address street passed in the payment request."""


class ResponseAdditionalDataBillingAddressDict(TypedDict):
    billing_address_city: NotRequired[str]
    billing_address_country: NotRequired[str]
    billing_address_house_number_or_name: NotRequired[str]
    billing_address_postal_code: NotRequired[str]
    billing_address_state_or_province: NotRequired[str]
    billing_address_street: NotRequired[str]
