from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FinishScaDeviceRegistrationRequest(SdkBaseModel):
    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to register the SCA device. You obtain this information by using
    Adyen's authentication SDK."""


class FinishScaDeviceRegistrationRequestDict(TypedDict):
    sdk_output: str
