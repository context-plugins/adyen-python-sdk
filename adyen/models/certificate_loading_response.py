from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CertificateLoadingResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the communication session."""

    installation_id: Optional[str] = Field(default=UNSET, alias="installationId")
    """The unique identifier of the SDK installation. If you create the `Terminal API
    <https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/>`__ transaction request on your backend,
    use this as the ``POIID`` in the ``MessageHeader`` of the request."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The unique identifier of your merchant account."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """The data that the SDK uses to authenticate responses from the Adyen payments platform. Pass this value to your
    POS app."""

    store: Optional[str] = UNSET
    """The reference of the store that the transactions are processed for."""


class CertificateLoadingResponseDict(TypedDict):
    id: NotRequired[str]
    installation_id: NotRequired[str]
    merchant_account: NotRequired[str]
    sdk_data: NotRequired[str]
    store: NotRequired[str]
