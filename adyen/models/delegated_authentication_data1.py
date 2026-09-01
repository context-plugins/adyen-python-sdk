from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DelegatedAuthenticationData1(SdkBaseModel):
    """Contains information required to register the SCA device."""

    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to register the SCA device. You obtain this information by using
    our authentication SDK."""


class DelegatedAuthenticationData1Dict(TypedDict):
    sdk_output: str
