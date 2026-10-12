from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssociationFinaliseResponse(SdkBaseModel):
    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """The unique identifier of the SCA device you associated with a resource."""

    ids: Optional[list[str]] = UNSET
    """The list of unique identifiers of the resources that you associated with the SCA device."""

    type_: Literal["PAYMENT_INSTRUMENT"] = Field(default="PAYMENT_INSTRUMENT", alias="type")
    """The type of resource that you associated with the SCA device."""


class AssociationFinaliseResponseDict(TypedDict):
    device_id: NotRequired[str]
    ids: NotRequired[list[str]]
    type_: Literal["PAYMENT_INSTRUMENT"]
