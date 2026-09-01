from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DelegatedAuthenticationData(SdkBaseModel):
    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to register the SCA device. You obtain this information by using
    our authentication SDK."""


class DelegatedAuthenticationDataDict(TypedDict):
    sdk_output: str
