from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sdk_interface import SdkInterfaceOrStr
from .enums.sdk_ui_type import SdkUiTypeOrStr


class DeviceRenderOptions(SdkBaseModel):
    """Display options for the 3D Secure 2 SDK. Optional and only for ``deviceChannel`` **app**."""

    sdk_interface: Optional[SdkInterfaceOrStr] = Field(default=UNSET, alias="sdkInterface")
    """Supported SDK interface types. Allowed values:
    * native
    * html
    * both"""

    sdk_ui_type: Optional[list[SdkUiTypeOrStr]] = Field(default=UNSET, alias="sdkUiType")
    """UI types supported for displaying specific challenges. Allowed values:
    * text
    * singleSelect
    * outOfBand
    * otherHtml
    * multiSelect"""


class DeviceRenderOptionsDict(TypedDict):
    sdk_interface: NotRequired[SdkInterfaceOrStr]
    sdk_ui_type: NotRequired[list[SdkUiTypeOrStr]]
