from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssociationInitiateResponse(SdkBaseModel):
    sdk_input: Optional[str] = Field(default=UNSET, alias="sdkInput")
    """A string that you must pass to the authentication SDK to continue with the association process."""


class AssociationInitiateResponseDict(TypedDict):
    sdk_input: NotRequired[str]
