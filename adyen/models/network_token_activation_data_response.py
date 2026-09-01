from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NetworkTokenActivationDataResponse(SdkBaseModel):
    sdk_input: Optional[str] = Field(default=UNSET, alias="sdkInput")
    """A block of data that contains the activation data for a network token. This ``sdkInput`` is required to
    initialize Adyen's SDK for network token provisioning.

    For more information, see the repositories for Adyen's SDKs for network token provisioning:
    * `Adyen Apple Pay Provisioning SDK <https://github.com/Adyen/adyen-apple-pay-provisioning-ios>`__.
    * `Adyen Google Wallet Provisioning SDK <https://github.com/Adyen/adyen-issuing-android>`__"""


class NetworkTokenActivationDataResponseDict(TypedDict):
    sdk_input: NotRequired[str]
