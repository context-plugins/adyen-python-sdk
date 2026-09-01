from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .stored_payment_method_resource import StoredPaymentMethodResource, StoredPaymentMethodResourceDict


class ListStoredPaymentMethodsResponse(SdkBaseModel):
    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """Your merchant account."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3
    characters.
    > Your reference must not include personally identifiable information (PII), for example name or email address."""

    stored_payment_methods: Optional[list[StoredPaymentMethodResource]] = Field(
        default=UNSET, alias="storedPaymentMethods"
    )
    """List of all stored payment methods."""


class ListStoredPaymentMethodsResponseDict(TypedDict):
    merchant_account: NotRequired[str]
    shopper_reference: NotRequired[str]
    stored_payment_methods: NotRequired[list[StoredPaymentMethodResource | StoredPaymentMethodResourceDict]]
