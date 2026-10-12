from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .file1 import File1, File1Dict
from .file2 import File2, File2Dict
from .file3 import File3, File3Dict
from .file4 import File4, File4Dict


class Profile(SdkBaseModel):
    auth_type: str = Field(alias="authType")
    """The type of Wi-Fi network. Possible values: **wpa-psk**, **wpa2-psk**, **wpa-eap**, **wpa2-eap**."""

    auto_wifi: Optional[bool] = Field(default=UNSET, alias="autoWifi")
    """Indicates whether to automatically select the best authentication method available. Does not work on older
    terminal models."""

    bss_type: str = Field(alias="bssType")
    """Use **infra** for infrastructure-based networks. This applies to most networks. Use **adhoc** only if the
    communication is p2p-based between base stations."""

    channel: Optional[int] = UNSET
    """The channel number of the Wi-Fi network. The recommended setting is **0** for automatic channel selection."""

    default_profile: Optional[bool] = Field(default=UNSET, alias="defaultProfile")
    """Indicates whether this is your preferred wireless network. If **true**, the terminal will try connecting to this
    network first."""

    domain_suffix: Optional[str] = Field(default=UNSET, alias="domainSuffix")
    """Specifies the server domain name for EAP-TLS and EAP-PEAP WiFi profiles on Android 11 and above."""

    eap: Optional[str] = UNSET
    """For ``authType`` **wpa-eap** or **wpa2-eap**. Possible values: **tls**, **peap**, **leap**, **fast**"""

    eap_ca_cert: Optional[File1] = Field(default=UNSET, alias="eapCaCert")
    """For ``authType`` **wpa-eap** or **wpa2-eap**. The root certificate from the CA that signed the certificate of the
    RADIUS server that is part of your wireless network."""

    eap_client_cert: Optional[File2] = Field(default=UNSET, alias="eapClientCert")
    """For ``eap`` **tls**. The certificate chain for the terminals. All terminals in the same network will use the same
    EAP client certificate."""

    eap_client_key: Optional[File3] = Field(default=UNSET, alias="eapClientKey")
    """For ``eap`` **tls**. The RSA private key for the client. Include the lines BEGIN RSA PRIVATE KEY and END RSA
    PRIVATE KEY."""

    eap_client_pwd: Optional[str] = Field(default=UNSET, alias="eapClientPwd")
    """For ``eap`` **tls**. The password of the RSA key file, if that file is password-protected."""

    eap_identity: Optional[str] = Field(default=UNSET, alias="eapIdentity")
    """For ``authType`` **wpa-eap** or **wpa2-eap**. The EAP-PEAP username from your MS-CHAP account. Must match the
    configuration of your RADIUS server."""

    eap_intermediate_cert: Optional[File4] = Field(default=UNSET, alias="eapIntermediateCert")
    """For ``eap`` **tls**. The EAP intermediate certificate."""

    eap_pwd: Optional[str] = Field(default=UNSET, alias="eapPwd")
    """For ``eap`` **peap**. The EAP-PEAP password from your MS-CHAP account. Must match the configuration of your
    RADIUS server."""

    hidden_ssid: Optional[bool] = Field(default=UNSET, alias="hiddenSsid")
    """Indicates if the network doesn't broadcast its SSID. Mandatory for Android terminals, because these terminals
    rely on this setting to be able to connect to any network."""

    name: Optional[str] = UNSET
    """Your name for the Wi-Fi profile."""

    psk: Optional[str] = UNSET
    """For ``authType`` **wpa-psk or **wpa2-psk**. The password to the wireless network."""

    ssid: str
    """The name of the wireless network."""

    wsec: str
    """The type of encryption. Possible values: **auto**, **ccmp** (recommended), **tkip**"""


class ProfileDict(TypedDict):
    auth_type: str
    auto_wifi: NotRequired[bool]
    bss_type: str
    channel: NotRequired[int]
    default_profile: NotRequired[bool]
    domain_suffix: NotRequired[str]
    eap: NotRequired[str]
    eap_ca_cert: NotRequired[File1Dict]
    eap_client_cert: NotRequired[File2Dict]
    eap_client_key: NotRequired[File3Dict]
    eap_client_pwd: NotRequired[str]
    eap_identity: NotRequired[str]
    eap_intermediate_cert: NotRequired[File4Dict]
    eap_pwd: NotRequired[str]
    hidden_ssid: NotRequired[bool]
    name: NotRequired[str]
    psk: NotRequired[str]
    ssid: str
    wsec: str
