from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateCompanyApiCredentialRequest(SdkBaseModel):
    allowed_origins: Optional[list[str]] = Field(default=UNSET, alias="allowedOrigins")
    """List of `allowed origins
    <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ for the new API
    credential."""

    associated_merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="associatedMerchantAccounts")
    """List of merchant accounts that the API credential has access to."""

    description: Optional[str] = UNSET
    """Description of the API credential."""

    roles: Optional[list[str]] = UNSET
    """List of `roles <https://docs.adyen.com/development-resources/api-credentials#roles-1>`__ for the API credential.
    Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials."""


class CreateCompanyApiCredentialRequestDict(TypedDict):
    allowed_origins: NotRequired[list[str]]
    associated_merchant_accounts: NotRequired[list[str]]
    description: NotRequired[str]
    roles: NotRequired[list[str]]
