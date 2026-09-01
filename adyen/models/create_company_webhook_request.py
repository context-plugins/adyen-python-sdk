from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_settings1 import AdditionalSettings1, AdditionalSettings1Dict
from .enums.communication_format import CommunicationFormatOrStr
from .enums.encryption_protocol import EncryptionProtocolOrStr
from .enums.filter_merchant_account_type import FilterMerchantAccountTypeOrStr
from .enums.network_type import NetworkTypeOrStr


class CreateCompanyWebhookRequest(SdkBaseModel):
    accepts_expired_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsExpiredCertificate")
    """Indicates if expired SSL certificates are accepted. Default value: **false**."""

    accepts_self_signed_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsSelfSignedCertificate")
    """Indicates if self-signed SSL certificates are accepted. Default value: **false**."""

    accepts_untrusted_root_certificate: Optional[bool] = Field(default=UNSET, alias="acceptsUntrustedRootCertificate")
    """Indicates if untrusted SSL certificates are accepted. Default value: **false**."""

    active: bool
    """Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events
    related an account."""

    additional_settings: Optional[AdditionalSettings1] = Field(default=UNSET, alias="additionalSettings")
    """Additional shopper and transaction information to be included in your `standard webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__. Find out more about the
    available `additional settings <https://docs.adyen.com/development-resources/webhooks/additional-settings>`__."""

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

    filter_merchant_account_type: FilterMerchantAccountTypeOrStr = Field(alias="filterMerchantAccountType")
    """Shows how merchant accounts are filtered when configuring the webhook.

    Possible values:
    * **allAccounts** : Includes all merchant accounts, and does not require specifying ``filterMerchantAccounts``.
    * **includeAccounts** : The webhook is configured for the merchant accounts listed in ``filterMerchantAccounts``.
    * **excludeAccounts** : The webhook is not configured for the merchant accounts listed in
        ``filterMerchantAccounts``."""

    filter_merchant_accounts: list[str] = Field(alias="filterMerchantAccounts")
    """A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion
    is based on the value defined for ``filterMerchantAccountType``.

    Required if ``filterMerchantAccountType`` is either:
    * **includeAccounts**
    * **excludeAccounts**

    Not needed for ``filterMerchantAccountType``: **allAccounts**."""

    network_type: Optional[NetworkTypeOrStr] = Field(default=UNSET, alias="networkType")
    """Network type for Terminal API notification webhooks. Possible values:
    * **public**
    * **local**

    Default Value: **public**."""

    password: Optional[str] = UNSET
    """Password to access the webhook URL."""

    populate_soap_action_header: Optional[bool] = Field(default=UNSET, alias="populateSoapActionHeader")
    """Indicates if the SOAP action header needs to be populated. Default value: **false**.

    Only applies if ``communicationFormat``: **soap**."""

    type_: str = Field(alias="type")
    """The type of webhook that is being created. Possible values are:

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
    - **rreq-notification**
    - **terminal-settings**
    - **terminal-boarding**

    Find out more about `standard webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__ and `other types of webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#other-webhooks>`__."""

    url: str
    """Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**."""

    username: Optional[str] = UNSET
    """Username to access the webhook URL."""


class CreateCompanyWebhookRequestDict(TypedDict):
    accepts_expired_certificate: NotRequired[bool]
    accepts_self_signed_certificate: NotRequired[bool]
    accepts_untrusted_root_certificate: NotRequired[bool]
    active: bool
    additional_settings: NotRequired[AdditionalSettings1 | AdditionalSettings1Dict]
    communication_format: CommunicationFormatOrStr
    description: NotRequired[str]
    encryption_protocol: NotRequired[EncryptionProtocolOrStr]
    filter_merchant_account_type: FilterMerchantAccountTypeOrStr
    filter_merchant_accounts: list[str]
    network_type: NotRequired[NetworkTypeOrStr]
    password: NotRequired[str]
    populate_soap_action_header: NotRequired[bool]
    type_: str
    url: str
    username: NotRequired[str]
