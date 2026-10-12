from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class DetailsRequestAuthenticationData1(SdkBaseModel):
    """Data for 3DS authentication."""

    authentication_only: bool = Field(default=False, alias="authenticationOnly")
    """Required to trigger the `authentication-only flow
    <https://docs.adyen.com/online-payments/3d-secure/authentication-only/>`__. If set to **true**, you will only
    perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**."""


class DetailsRequestAuthenticationData1Dict(TypedDict):
    authentication_only: NotRequired[bool]
