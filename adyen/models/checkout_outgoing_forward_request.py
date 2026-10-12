from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.http_method_model import HttpMethodModelOrStr


class CheckoutOutgoingForwardRequest(SdkBaseModel):
    body: str
    """The request body that you want Adyen to forward to the third party on your behalf, in string format.

    Include key value pairs to specify the payment details, and use `placeholders
    <https://docs.adyen.com/online-payments/tokenization/forward-payment-details#placeholders>`__ for the values. Adyen
    replaces the placeholders with the payment details when making the request to the third party.

    When forwarding a network token, include a `condition
    <https://docs.adyen.com/online-payments/tokenization/forward-payment-details#conditional-placeholders>`__ that
    checks if the network token exists, and informs Adyen of which fields to send depending on the outcome."""

    credentials: Optional[str] = UNSET
    """Your credentials that are needed to authenticate with the third party."""

    headers: Optional[dict[str, str]] = UNSET
    """The request headers that will be included in the request Adyen makes to the third party on your behalf. Supports
    the ``{{credentials}}`` `placeholder
    <https://docs.adyen.com/online-payments/tokenization/forward-payment-details#placeholders>`__."""

    http_method: HttpMethodModelOrStr = Field(alias="httpMethod")
    """The HTTP method to use for the request Adyen makes on your behalf to the third party."""

    url_suffix: Optional[str] = Field(default=UNSET, alias="urlSuffix")
    """The suffix that Adyen needs to append to the ``baseUrl`` to construct the destination URL that belongs to the
    third party. This is usually the endpoint name for the request, for example, **/payments**."""


class CheckoutOutgoingForwardRequestDict(TypedDict):
    body: str
    credentials: NotRequired[str]
    headers: NotRequired[dict[str, str]]
    http_method: HttpMethodModelOrStr
    url_suffix: NotRequired[str]
