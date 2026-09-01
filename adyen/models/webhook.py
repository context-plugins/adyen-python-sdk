from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_settings_response1 import AdditionalSettingsResponse1, AdditionalSettingsResponse1Dict
from .enums.communication_format import CommunicationFormatOrStr
from .enums.encryption_protocol import EncryptionProtocolOrStr
from .enums.filter_merchant_account_type1 import FilterMerchantAccountType1OrStr
from .enums.network_type2 import NetworkType2OrStr
from .webhook_links2 import WebhookLinks2, WebhookLinks2Dict


class Webhook(SdkBaseModel):
    links: Optional[WebhookLinks2] = Field(default=UNSET, alias="_links")
    """References to resources connected with this webhook."""

    accepts_expired_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsExpiredCertificate")
    """Indicates if expired SSL certificates are accepted. Default value: **false**."""

    accepts_self_signed_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsSelfSignedCertificate")
    """Indicates if self-signed SSL certificates are accepted. Default value: **false**."""

    accepts_untrusted_root_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsUntrustedRootCertificate")
    """Indicates if untrusted SSL certificates are accepted. Default value: **false**."""

    account_reference: Optional[str] = Field(default=UNSET, alias="accountReference")
    """Reference to the account the webook is set on."""

    active: bool
    """Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about
    events related an account."""

    additional_settings: Optional[AdditionalSettingsResponse1] = Field(default=UNSET, alias="additionalSettings")
    """Additional shopper and transaction information to be included in your `standard webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__. Find out more about the
    available `additional settings <https://docs.adyen.com/development-resources/webhooks/additional-settings>`__."""

    certificate_alias: Optional[str] = Field(default=UNSET, alias="certificateAlias")
    """The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will
    match this alias."""

    communication_format: CommunicationFormatOrStr = Field(alias="communicationFormat")
    """Format or protocol for receiving webhooks. Possible values:
    * **soap**
    * **http**
    * **json**"""

    description: Optional[str] = UNSET
    """Your description for this webhook configuration."""

    encryption_protocol: Optional[EncryptionProtocolOrStr] = Field(default=UNSET, alias="encryptionProtocol")
    """SSL version to access the public webhook URL specified in the ``url`` field. Possible values:
    * **TLSv1.3**
    * **TLSv1.2**
    * **HTTP** - Only allowed on Test environment.

    If not specified, the webhook will use ``sslVersion``: **TLSv1.2**."""

    filter_merchant_account_type: Optional[FilterMerchantAccountType1OrStr] = Field(
        default=UNSET, alias="filterMerchantAccountType"
    )
    """Shows how merchant accounts are included in company-level webhooks. Possible values:
    * **includeAccounts**
    * **excludeAccounts**
    * **allAccounts**: Includes all merchant accounts, and does not require specifying ``filterMerchantAccounts``."""

    filter_merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="filterMerchantAccounts")
    """A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion
    is based on the value defined for ``filterMerchantAccountType``.

    Required if ``filterMerchantAccountType`` is either:
    * **includeAccounts**
    * **excludeAccounts**

    Not needed for ``filterMerchantAccountType``: **allAccounts**."""

    has_error: Optional[bool] = Field(default=UNSET, alias="hasError")
    """Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**,
    troubleshoot the configuration using the `testing endpoint
    <https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookid}/test>`__."""

    has_password: Optional[bool] = Field(default=UNSET, alias="hasPassword")
    """Indicates if the webhook is password protected."""

    hmac_key_check_value: Optional[str] = Field(default=UNSET, alias="hmacKeyCheckValue")
    """The `checksum <https://en.wikipedia.org/wiki/Key_checksum_value>`__ of the HMAC key generated for this webhook.
    You can use this value to uniquely identify the HMAC key configured for this webhook."""

    id: Optional[str] = UNSET
    """Unique identifier for this webhook."""

    network_type: Optional[NetworkType2OrStr] = Field(default=UNSET, alias="networkType")
    """Network type for Terminal API details webhooks."""

    populate_soap_action_header: Optional[bool] = Field(default=UNSET, alias="populateSoapActionHeader")
    """Indicates if the SOAP action header needs to be populated. Default value: **false**.

    Only applies if ``communicationFormat``: **soap**."""

    type_: str = Field(alias="type")
    """The type of webhook. Possible values are:

    - **standard**
    - **account-settings-notification**
    - **banktransfer-notification**
    - **boletobancario-notification**
    - **directdebit-notification**
    - **ach-notification-of-change-notification**
    - **direct-debit-notice-of-change-notification**
    - **pending-notification**
    - **ideal-notification**
    - **ideal-pending-notification**
    - **report-notification**
    - **terminal-api-notification**
    - **terminal-settings**
    - **terminal-boarding**

    Find out more about `standard webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__ and `other types of webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#other-webhooks>`__."""

    url: str
    """Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**."""

    username: Optional[str] = UNSET
    """Username to access the webhook URL."""


class WebhookDict(TypedDict):
    links: NotRequired[WebhookLinks2 | WebhookLinks2Dict]
    accepts_expired_certificate: NotRequired[bool]
    accepts_self_signed_certificate: NotRequired[bool]
    accepts_untrusted_root_certificate: NotRequired[bool]
    account_reference: NotRequired[str]
    active: bool
    additional_settings: NotRequired[AdditionalSettingsResponse1 | AdditionalSettingsResponse1Dict]
    certificate_alias: NotRequired[str]
    communication_format: CommunicationFormatOrStr
    description: NotRequired[str]
    encryption_protocol: NotRequired[EncryptionProtocolOrStr]
    filter_merchant_account_type: NotRequired[FilterMerchantAccountType1OrStr]
    filter_merchant_accounts: NotRequired[list[str]]
    has_error: NotRequired[bool]
    has_password: NotRequired[bool]
    hmac_key_check_value: NotRequired[str]
    id: NotRequired[str]
    network_type: NotRequired[NetworkType2OrStr]
    populate_soap_action_header: NotRequired[bool]
    type_: str
    url: str
    username: NotRequired[str]
