from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInstrument2(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description of the resource."""

    id: Optional[str] = UNSET
    """The unique identifier of the resource."""

    reference: Optional[str] = UNSET
    """The reference for the resource."""

    token_type: Optional[str] = Field(default=UNSET, alias="tokenType")
    """The type of wallet that the network token is associated with."""


class PaymentInstrument2Dict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    reference: NotRequired[str]
    token_type: NotRequired[str]
