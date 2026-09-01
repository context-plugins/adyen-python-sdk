from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Referenced(SdkBaseModel):
    enable_standalone_refunds: Optional[bool] = Field(default=UNSET, alias="enableStandaloneRefunds")
    """Indicates whether referenced refunds are enabled on the standalone terminal."""


class ReferencedDict(TypedDict):
    enable_standalone_refunds: NotRequired[bool]
