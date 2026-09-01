from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssociationDelegatedAuthenticationData(SdkBaseModel):
    sdk_output: str = Field(alias="sdkOutput")
    """A base64-encoded block with the data required to authenticate the request. You obtain this information by using
    our authentication SDK."""


class AssociationDelegatedAuthenticationDataDict(TypedDict):
    sdk_output: str
