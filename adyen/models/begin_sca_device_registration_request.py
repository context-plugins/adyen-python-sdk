from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BeginScaDeviceRegistrationRequest(SdkBaseModel):
    name: str
    """The name of the SCA device that you are registering. You can use it to help your users identify the device."""

    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to register the SCA device. You obtain this information by using
    Adyen's authentication SDK."""


class BeginScaDeviceRegistrationRequestDict(TypedDict):
    name: str
    sdk_output: str
