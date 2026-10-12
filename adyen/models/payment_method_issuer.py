from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PaymentMethodIssuer(SdkBaseModel):
    disabled: bool = False
    """A boolean value indicating whether this issuer is unavailable. Can be ``true`` whenever the issuer is offline."""

    id: str
    """The unique identifier of this issuer, to submit in requests to /payments."""

    name: str
    """A localized name of the issuer."""


class PaymentMethodIssuerDict(TypedDict):
    disabled: NotRequired[bool]
    id: str
    name: str
