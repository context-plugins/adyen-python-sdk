from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CalculatePciStatusResponse(SdkBaseModel):
    signing_required: Optional[bool] = Field(default=UNSET, alias="signingRequired")
    """Indicates if the user is required to sign PCI questionnaires. If **false**, they do not need to sign any
    questionnaires."""


class CalculatePciStatusResponseDict(TypedDict):
    signing_required: NotRequired[bool]
