from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssociationInitiateRequest(SdkBaseModel):
    ids: list[str]
    """The list of unique identifiers of the resources that you are associating with the SCA device.

    Maximum: 5 strings."""

    type_: Literal["PaymentInstrument"] = Field(default="PaymentInstrument", alias="type")
    """The type of resource that you are associating with the SCA device.

    Possible value: **PaymentInstrument**"""


class AssociationInitiateRequestDict(TypedDict):
    ids: list[str]
    type_: Literal["PaymentInstrument"]
