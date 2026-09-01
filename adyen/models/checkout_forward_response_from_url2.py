from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutForwardResponseFromUrl2(SdkBaseModel):
    """The details of the response Adyen received from the third party."""

    body: Optional[str] = UNSET
    """The body of the response Adyen received from the third party, in string format."""

    headers: Optional[dict[str, str]] = UNSET
    """The HTTP headers of the response Adyen received from the third party."""

    status: Optional[int] = UNSET
    """The HTTP status of the response Adyen received from the third party."""


class CheckoutForwardResponseFromUrl2Dict(TypedDict):
    body: NotRequired[str]
    headers: NotRequired[dict[str, str]]
    status: NotRequired[int]
