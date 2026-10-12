from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allowed_origin import AllowedOrigin, AllowedOriginDict
from .api_credential_links2 import ApiCredentialLinks2, ApiCredentialLinks2Dict


class MeApiCredential(SdkBaseModel):
    links: Optional[ApiCredentialLinks2] = Field(default=UNSET, alias="_links")
    """References to resources linked to the API credential."""

    active: bool
    """Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration."""

    allowed_ip_addresses: list[str] = Field(alias="allowedIpAddresses")
    """List of IP addresses from which your client can make requests.

    If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which
    is not on the list, you get a security error."""

    allowed_origins: Optional[list[AllowedOrigin]] = Field(default=UNSET, alias="allowedOrigins")
    """List containing the `allowed origins
    <https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins>`__ linked to the API
    credential."""

    client_key: str = Field(alias="clientKey")
    """Public key used for `client-side authentication
    <https://docs.adyen.com/development-resources/client-side-authentication>`__. The client key is required for Drop-in
    and Components integrations."""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Name of the company linked to the API credential."""

    description: Optional[str] = UNSET
    """Description of the API credential."""

    id: str
    """Unique identifier of the API credential."""

    roles: list[str]
    """List of `roles <https://docs.adyen.com/development-resources/api-credentials#roles-1>`__ for the API
    credential."""

    subject_dn: Optional[str] = Field(default=UNSET, alias="subjectDN")
    """The subject DN of the certificate issued by Adyen."""

    username: str
    """The name of the `API credential <https://docs.adyen.com/development-resources/api-credentials>`__, for example
    **ws@Company.TestCompany**."""


class MeApiCredentialDict(TypedDict):
    links: NotRequired[ApiCredentialLinks2Dict]
    active: bool
    allowed_ip_addresses: list[str]
    allowed_origins: NotRequired[list[AllowedOriginDict]]
    client_key: str
    company_name: NotRequired[str]
    description: NotRequired[str]
    id: str
    roles: list[str]
    subject_dn: NotRequired[str]
    username: str
