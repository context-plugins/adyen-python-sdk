from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssociationDelegatedAuthenticationData1(SdkBaseModel):
    """Contains authentication information required to associate the resource with the SCA device."""

    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to authenticate the request. You obtain this information by using
    our authentication SDK."""


class AssociationDelegatedAuthenticationData1Dict(TypedDict):
    sdk_output: str
