from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdminRequest2(SdkBaseModel):
    """Content of the Admin Request message."""

    service_identification: Optional[str] = Field(default=UNSET, alias="ServiceIdentification")
    """Identification of the administrative service to process."""


class AdminRequest2Dict(TypedDict):
    service_identification: NotRequired[str]
